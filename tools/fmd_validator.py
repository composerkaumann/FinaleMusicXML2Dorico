#!/usr/bin/env python3
"""Minimal Finale MusicXML → Dorico validation core."""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from xml.etree import ElementTree as ET


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    message: str
    part_id: str
    measure: str
    expected_duration: int
    actual_duration: int
    overflow: int
    divisions: int
    observed_extents: dict[str, int] | None = None
    underflow: int | None = None
    voice: str | None = None
    tuplet_number: str | None = None
    note_index: int | None = None


@dataclass
class ActiveTuplet:
    expected_duration: Fraction | None
    actual_duration: int = 0
    nested: bool = False


NOTE_TYPE_QUARTERS = {
    "whole": Fraction(4),
    "half": Fraction(2),
    "quarter": Fraction(1),
    "eighth": Fraction(1, 2),
    "16th": Fraction(1, 4),
    "32nd": Fraction(1, 8),
    "64th": Fraction(1, 16),
    "128th": Fraction(1, 32),
    "256th": Fraction(1, 64),
    "512th": Fraction(1, 128),
    "1024th": Fraction(1, 256),
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def child(element: ET.Element, name: str) -> ET.Element | None:
    return next((item for item in element if local_name(item.tag) == name), None)


def child_text(element: ET.Element, name: str) -> str | None:
    item = child(element, name)
    return item.text.strip() if item is not None and item.text else None


def musicxml_bytes(path: Path) -> bytes:
    if path.suffix.lower() != ".mxl":
        return path.read_bytes()

    with zipfile.ZipFile(path) as archive:
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = next(
            (
                item
                for item in container.iter()
                if local_name(item.tag) == "rootfile"
                and item.get("full-path")
            ),
            None,
        )
        if rootfile is None:
            raise ValueError("MXL container does not identify a MusicXML rootfile")
        return archive.read(rootfile.get("full-path"))


def duration_value(element: ET.Element) -> int:
    text = child_text(element, "duration")
    if text is None:
        return 0
    return int(text)


def expected_duration(divisions: int, beats: int, beat_type: int) -> int:
    value = Fraction(divisions * 4 * beats, beat_type)
    if value.denominator != 1:
        raise ValueError(
            f"time signature produces non-integral duration: {value}"
        )
    return value.numerator


def measure_extent(measure: ET.Element) -> int:
    """Return the furthest rhythmic cursor position reached in a measure."""

    cursor = 0
    furthest = 0
    previous_note_start = 0

    for item in measure:
        name = local_name(item.tag)
        if name == "note":
            duration = duration_value(item)
            is_chord = child(item, "chord") is not None
            is_grace = child(item, "grace") is not None
            if is_chord:
                furthest = max(furthest, previous_note_start + duration)
            else:
                previous_note_start = cursor
                if not is_grace:
                    cursor += duration
                    furthest = max(furthest, cursor)
        elif name == "backup":
            cursor -= duration_value(item)
        elif name == "forward":
            cursor += duration_value(item)
            furthest = max(furthest, cursor)

    return furthest


def measure_contains_tuplet(measure: ET.Element) -> bool:
    return any(local_name(item.tag) == "tuplet" for item in measure.iter())


def measure_contains_rest(measure: ET.Element) -> bool:
    return any(
        local_name(item.tag) == "rest" for item in measure.iter()
    )


def tiny_untyped_note_findings(
    measure: ET.Element, part_id: str, divisions: int
) -> list[Finding]:
    """Warn on very short pitched notes with no notation type or tuplet ratio."""

    findings: list[Finding] = []
    notes = (item for item in measure if local_name(item.tag) == "note")
    for index, note in enumerate(notes, start=1):
        if (
            child(note, "pitch") is None
            or child(note, "grace") is not None
            or child(note, "type") is not None
            or child(note, "time-modification") is not None
        ):
            continue
        duration = duration_value(note)
        if (
            duration <= 0
            or Fraction(duration, divisions) >= NOTE_TYPE_QUARTERS["1024th"]
        ):
            continue
        findings.append(
            Finding(
                rule_id="FMD006",
                severity="warning",
                message=(
                    f"Note {index} in measure {measure.get('number', '')}, "
                    f"part {part_id}, has no notation type or tuplet ratio "
                    f"and lasts {duration}/{divisions} of a quarter note, "
                    f"shorter than a 1024th note. Dorico may quantize it."
                ),
                part_id=part_id,
                measure=measure.get("number", ""),
                expected_duration=(divisions + 255) // 256,
                actual_duration=duration,
                overflow=0,
                divisions=divisions,
                voice=child_text(note, "voice") or "1",
                note_index=index,
            )
        )
    return findings


def tuplet_group_findings(
    measure: ET.Element, part_id: str, divisions: int
) -> list[Finding]:
    """Find complete, non-nested tuplets shorter than their explicit span."""

    findings: list[Finding] = []
    active: dict[tuple[str, str], ActiveTuplet] = {}

    for note in (item for item in measure if local_name(item.tag) == "note"):
        voice = child_text(note, "voice") or "1"
        notations = child(note, "notations")
        markers = (
            [
                item
                for item in notations
                if local_name(item.tag) == "tuplet"
            ]
            if notations is not None
            else []
        )

        for marker in markers:
            if marker.get("type") != "start":
                continue
            key = (voice, marker.get("number", "1"))
            modification = child(note, "time-modification")
            normal_type = (
                child_text(modification, "normal-type")
                if modification is not None
                else None
            )
            normal_notes_text = (
                child_text(modification, "normal-notes")
                if modification is not None
                else None
            )
            expected: Fraction | None = None
            if normal_type in NOTE_TYPE_QUARTERS and normal_notes_text:
                normal_notes = int(normal_notes_text)
                normal_dots = sum(
                    local_name(item.tag) == "normal-dot"
                    for item in modification
                )
                if normal_notes > 0:
                    dotted_multiplier = 2 - Fraction(1, 2**normal_dots)
                    expected = (
                        divisions
                        * NOTE_TYPE_QUARTERS[normal_type]
                        * normal_notes
                        * dotted_multiplier
                    )
            active[key] = ActiveTuplet(expected_duration=expected)
            same_voice = [
                state for (item_voice, _), state in active.items()
                if item_voice == voice
            ]
            if len(same_voice) > 1:
                for state in same_voice:
                    state.nested = True

        if child(note, "chord") is None and child(note, "grace") is None:
            for (item_voice, _), state in active.items():
                if item_voice == voice:
                    state.actual_duration += duration_value(note)

        for marker in markers:
            if marker.get("type") != "stop":
                continue
            number = marker.get("number", "1")
            state = active.pop((voice, number), None)
            if (
                state is None
                or state.nested
                or state.expected_duration is None
                or state.expected_duration.denominator != 1
                or state.actual_duration >= state.expected_duration
            ):
                continue
            expected = state.expected_duration.numerator
            findings.append(
                Finding(
                    rule_id="FMD005",
                    severity="warning",
                    message=(
                        f"Tuplet {number} in voice {voice} of measure "
                        f"{measure.get('number', '')}, part {part_id}, "
                        f"declares a span of {expected} divisions but "
                        f"its notes cover only {state.actual_duration}."
                    ),
                    part_id=part_id,
                    measure=measure.get("number", ""),
                    expected_duration=expected,
                    actual_duration=state.actual_duration,
                    overflow=0,
                    divisions=divisions,
                    underflow=expected - state.actual_duration,
                    voice=voice,
                    tuplet_number=number,
                )
            )

    return findings


def validate(path: Path) -> list[Finding]:
    root = ET.fromstring(musicxml_bytes(path))
    if local_name(root.tag) != "score-partwise":
        raise ValueError("only score-partwise MusicXML is currently supported")

    findings: list[Finding] = []
    measure_extents: dict[
        int, list[tuple[str, str, int, int, int]]
    ] = {}
    for part in (item for item in root if local_name(item.tag) == "part"):
        part_id = part.get("id", "")
        divisions: int | None = None
        beats: int | None = None
        beat_type: int | None = None

        measures = [
            item for item in part if local_name(item.tag) == "measure"
        ]
        for measure_index, measure in enumerate(measures):
            attributes = child(measure, "attributes")
            if attributes is not None:
                divisions_text = child_text(attributes, "divisions")
                if divisions_text is not None:
                    divisions = int(divisions_text)
                time = child(attributes, "time")
                if time is not None:
                    beats_text = child_text(time, "beats")
                    beat_type_text = child_text(time, "beat-type")
                    if beats_text is not None and beat_type_text is not None:
                        beats = int(beats_text)
                        beat_type = int(beat_type_text)

            if divisions is None or beats is None or beat_type is None:
                continue

            expected = expected_duration(divisions, beats, beat_type)
            actual = measure_extent(measure)
            measure_number = measure.get("number", "")
            measure_extents.setdefault(measure_index, []).append(
                (
                    part_id,
                    measure_number,
                    expected,
                    actual,
                    divisions,
                )
            )
            findings.extend(tiny_untyped_note_findings(measure, part_id, divisions))
            findings.extend(tuplet_group_findings(measure, part_id, divisions))
            if actual > expected:
                overflow = actual - expected
                fatal_rest_fill = (
                    measure_contains_tuplet(measure)
                    and measure_contains_rest(measure)
                )
                findings.append(
                    Finding(
                        rule_id="FMD004" if fatal_rest_fill else "FMD001",
                        severity="fatal" if fatal_rest_fill else "warning",
                        message=(
                            (
                                f"Measure {measure_number} in part "
                                f"{part_id} contains a tuplet and rests "
                                f"but extends to {actual} divisions; "
                                f"expected at most {expected}."
                            )
                            if fatal_rest_fill
                            else (
                                f"Measure {measure_number} in part "
                                f"{part_id} extends to {actual} divisions; "
                                f"expected at most {expected}."
                            )
                        ),
                        part_id=part_id,
                        measure=measure_number,
                        expected_duration=expected,
                        actual_duration=actual,
                        overflow=overflow,
                        divisions=divisions,
                    )
                )
            elif (
                actual < expected
                and measure.get("implicit") != "yes"
                and measure_contains_tuplet(measure)
            ):
                underflow = expected - actual
                findings.append(
                    Finding(
                        rule_id="FMD003",
                        severity="fatal",
                        message=(
                            f"Measure {measure_number} in part {part_id} "
                            f"contains a tuplet but reaches only {actual} "
                            f"of {expected} divisions."
                        ),
                        part_id=part_id,
                        measure=measure_number,
                        expected_duration=expected,
                        actual_duration=actual,
                        overflow=0,
                        divisions=divisions,
                        underflow=underflow,
                    )
                )

    for rows in measure_extents.values():
        if len(rows) < 2:
            continue
        expected_values = {row[2] for row in rows}
        observed = {row[0]: row[3] for row in rows}
        if len(expected_values) != 1 or len(set(observed.values())) == 1:
            continue

        expected = rows[0][2]
        shortest = min(observed.values())
        longest = max(observed.values())
        part_summary = ", ".join(
            f"{part_id}={extent}" for part_id, extent in observed.items()
        )
        findings.append(
            Finding(
                rule_id="FMD002",
                severity="warning",
                message=(
                    f"Measure {rows[0][1]} has conflicting rhythmic "
                    f"extents across parts ({part_summary}); all parts "
                    f"declare a duration of {expected}."
                ),
                part_id=",".join(observed),
                measure=rows[0][1],
                expected_duration=expected,
                actual_duration=longest,
                overflow=longest - shortest,
                divisions=rows[0][4],
                observed_extents=observed,
            )
        )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Detect Dorico-risk structures in Finale MusicXML exports."
    )
    parser.add_argument("file", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    try:
        findings = validate(args.file)
    except (OSError, ET.ParseError, ValueError, zipfile.BadZipFile) as error:
        print(f"Input error: {error}", file=sys.stderr)
        return 2

    if args.as_json:
        print(json.dumps([asdict(item) for item in findings], indent=2))
    elif findings:
        for item in findings:
            print(f"{item.severity.upper()} {item.rule_id}: {item.message}")
    else:
        print("No findings.")

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

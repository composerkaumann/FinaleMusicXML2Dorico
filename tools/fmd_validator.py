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


def validate(path: Path) -> list[Finding]:
    root = ET.fromstring(musicxml_bytes(path))
    if local_name(root.tag) != "score-partwise":
        raise ValueError("only score-partwise MusicXML is currently supported")

    findings: list[Finding] = []
    for part in (item for item in root if local_name(item.tag) == "part"):
        part_id = part.get("id", "")
        divisions: int | None = None
        beats: int | None = None
        beat_type: int | None = None

        for measure in (
            item for item in part if local_name(item.tag) == "measure"
        ):
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
            if actual > expected:
                overflow = actual - expected
                findings.append(
                    Finding(
                        rule_id="FMD001",
                        severity="warning",
                        message=(
                            f"Measure {measure.get('number', '')} in part "
                            f"{part_id} extends to {actual} divisions; "
                            f"expected at most {expected}."
                        ),
                        part_id=part_id,
                        measure=measure.get("number", ""),
                        expected_duration=expected,
                        actual_duration=actual,
                        overflow=overflow,
                        divisions=divisions,
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

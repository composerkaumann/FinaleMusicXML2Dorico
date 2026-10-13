from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from fmd_validator import validate  # noqa: E402


class MeasureDurationTests(unittest.TestCase):
    def test_base_has_no_findings(self) -> None:
        self.assertEqual(validate(ROOT / "BASE/FMD-BASE.musicxml"), [])

    def test_fatal_01_detects_overfilled_measure(self) -> None:
        findings = validate(ROOT / "FATAL-01/FATAL-01.musicxml")

        self.assertEqual(len(findings), 1)
        finding = findings[0]
        self.assertEqual(finding.rule_id, "FMD001")
        self.assertEqual(finding.severity, "warning")
        self.assertEqual(finding.part_id, "P1")
        self.assertEqual(finding.measure, "2")
        self.assertEqual(finding.expected_duration, 8)
        self.assertEqual(finding.actual_duration, 10)
        self.assertEqual(finding.overflow, 2)
        self.assertEqual(finding.divisions, 2)

    def test_fatal_01a_detects_cross_part_disagreement(self) -> None:
        findings = validate(ROOT / "FATAL-01a/FATAL-01a.musicxml")

        self.assertEqual([item.rule_id for item in findings], ["FMD001", "FMD002"])
        mismatch = findings[1]
        self.assertEqual(mismatch.severity, "warning")
        self.assertEqual(mismatch.measure, "2")
        self.assertEqual(mismatch.expected_duration, 8)
        self.assertEqual(mismatch.actual_duration, 10)
        self.assertEqual(mismatch.overflow, 2)
        self.assertEqual(mismatch.observed_extents, {"P1": 10, "P2": 8})

    def test_fatal_02_detects_incomplete_tuplet_measure(self) -> None:
        findings = validate(ROOT / "FATAL-02/FATAL-02.musicxml")

        self.assertEqual(len(findings), 1)
        finding = findings[0]
        self.assertEqual(finding.rule_id, "FMD003")
        self.assertEqual(finding.severity, "fatal")
        self.assertEqual(finding.part_id, "P1")
        self.assertEqual(finding.measure, "2")
        self.assertEqual(finding.expected_duration, 24)
        self.assertEqual(finding.actual_duration, 16)
        self.assertEqual(finding.underflow, 8)

    def test_fatal_02a_full_measure_has_no_findings(self) -> None:
        self.assertEqual(
            validate(ROOT / "FATAL-02a/FATAL-02a.musicxml"),
            [],
        )

    def test_fatal_02b_detects_overfilling_rest_after_tuplet(self) -> None:
        findings = validate(ROOT / "FATAL-02b/FATAL-02b.musicxml")

        self.assertEqual(len(findings), 1)
        finding = findings[0]
        self.assertEqual(finding.rule_id, "FMD004")
        self.assertEqual(finding.severity, "fatal")
        self.assertEqual(finding.part_id, "P1")
        self.assertEqual(finding.measure, "2")
        self.assertEqual(finding.expected_duration, 24)
        self.assertEqual(finding.actual_duration, 28)
        self.assertEqual(finding.overflow, 4)

    def test_fatal_03_detects_incomplete_timeline_after_voice_2_launch(self) -> None:
        findings = validate(ROOT / "FATAL-03/FATAL-03.musicxml")

        self.assertEqual(len(findings), 1)
        finding = findings[0]
        self.assertEqual(finding.rule_id, "FMD003")
        self.assertEqual(finding.severity, "fatal")
        self.assertEqual(finding.part_id, "P1")
        self.assertEqual(finding.measure, "2")
        self.assertEqual(finding.expected_duration, 24)
        self.assertEqual(finding.actual_duration, 16)
        self.assertEqual(finding.underflow, 8)

    def test_fatal_04_complete_voice_2_tuplet_has_no_findings(self) -> None:
        self.assertEqual(
            validate(ROOT / "FATAL-04/FATAL-04.musicxml"),
            [],
        )

    def test_fatal_04a_warns_for_incomplete_half_note_tuplet_span(self) -> None:
        findings = validate(ROOT / "FATAL-04a/FATAL-04a.musicxml")

        self.assertEqual(len(findings), 1)
        finding = findings[0]
        self.assertEqual(finding.rule_id, "FMD005")
        self.assertEqual(finding.severity, "warning")
        self.assertEqual(finding.part_id, "P1")
        self.assertEqual(finding.measure, "2")
        self.assertEqual(finding.voice, "1")
        self.assertEqual(finding.tuplet_number, "1")
        self.assertEqual(finding.expected_duration, 24)
        self.assertEqual(finding.actual_duration, 12)
        self.assertEqual(finding.underflow, 12)

    def test_fatal_04b_correct_tuplet_definition_has_no_findings(self) -> None:
        self.assertEqual(
            validate(ROOT / "FATAL-04b/FATAL-04b.musicxml"),
            [],
        )

    def test_explicit_matching_normal_type_has_no_findings(self) -> None:
        source = (ROOT / "FATAL-04a/FATAL-04a.musicxml").read_text()
        self.assertEqual(source.count("<normal-type>half</normal-type>"), 3)
        corrected = source.replace(
            "<normal-type>half</normal-type>",
            "<normal-type>quarter</normal-type>",
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "matching-normal-type.musicxml"
            path.write_text(corrected)
            self.assertEqual(validate(path), [])

    def test_fatal_06a_warns_for_tiny_untyped_note(self) -> None:
        findings = validate(ROOT / "FATAL-06/FATAL-06a.musicxml")

        self.assertEqual(len(findings), 1)
        finding = findings[0]
        self.assertEqual(finding.rule_id, "FMD006")
        self.assertEqual(finding.severity, "warning")
        self.assertEqual(finding.part_id, "P1")
        self.assertEqual(finding.measure, "2")
        self.assertEqual(finding.voice, "1")
        self.assertEqual(finding.note_index, 2)
        self.assertEqual(finding.divisions, 1024)
        self.assertEqual(finding.expected_duration, 4)
        self.assertEqual(finding.actual_duration, 1)

    def test_fatal_06b_normalized_quarter_without_type_has_no_findings(self) -> None:
        self.assertEqual(
            validate(ROOT / "FATAL-06/FATAL-06b.musicxml"),
            [],
        )

    def test_untyped_1024th_note_at_boundary_has_no_findings(self) -> None:
        source = (ROOT / "FATAL-06/FATAL-06a.musicxml").read_text()
        corrected = source.replace("<duration>1</duration>", "<duration>4</duration>")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untyped-1024th.musicxml"
            path.write_text(corrected)
            self.assertEqual(validate(path), [])

    def test_tiny_note_with_explicit_tuplet_ratio_has_no_findings(self) -> None:
        source = (ROOT / "FATAL-06/FATAL-06a.musicxml").read_text()
        replacement = (
            "<duration>1</duration>\n"
            "        <voice>1</voice>\n"
            "        <time-modification>\n"
            "          <actual-notes>4</actual-notes>\n"
            "          <normal-notes>1</normal-notes>\n"
            "          <normal-type>1024th</normal-type>\n"
            "        </time-modification>"
        )
        corrected = source.replace(
            "<duration>1</duration>\n        <voice>1</voice>",
            replacement,
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tiny-tuplet.musicxml"
            path.write_text(corrected)
            self.assertEqual(validate(path), [])


if __name__ == "__main__":
    unittest.main()

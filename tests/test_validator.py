from pathlib import Path
import sys
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


if __name__ == "__main__":
    unittest.main()

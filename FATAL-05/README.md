# FATAL-05 cross-staff triplet exported as separate parts

## Test and Dorico result

The author created a cross-staff triplet in Finale and imported the export
into Dorico 6.2.31. The reported import retained all notes on the source staff;
the cross-staff layout was not preserved.

This case is **not fatal**. Loss of that layout does not demonstrate that
Dorico ignores correctly encoded cross-staff information: this export does
not contain the intended staff reassignment.

The original filenames are [FMD-05.musx](FMD-05.musx) and
[FMD-05.musicxml](FMD-05.musicxml). The comparison reference is
[BASE/FMD-BASE-2STAFF.musicxml](../BASE/FMD-BASE-2STAFF.musicxml).

## Actual XML

- MusicXML 4.0 partwise contains two separate parts, P1 and P2, each with
  four measures, rather than the intended single multi-staff part.
- P1 uses `divisions=6`; P2 uses `divisions=2`. Both are in 4/4.
- P1 measure 2 contains G4–C4–G4 quarter notes, all in Voice 1, each with
  3:2 `time-modification` and duration 4. The triplet starts and stops
  on notes in the same voice.
- P1 measure 2 reaches only 12/24 division units, or two quarter-note beats.
  The planned final C4 half note, or a rest replacing it, is absent from
  the XML. The reason for its absence was not established.
- P2 contains whole-measure rests throughout; its measure 2 lasts 8 division
  units, or four quarter-note beats.
- No note has a `staff` element, and neither part has a `staves` element.
  All triplet notes belong to P1. The middle C4 stem's `default-y=-75`
  is a layout coordinate, not a staff assignment.
- P1 measures 1, 3, and 4 match the reference after duration normalization.
  P2's note/rest material also matches the reference.

MusicXML uses `staff` for staff assignment and `staves` for the number
of staves in a part. This export does not assign the middle C4 to a second
staff within P1. A genuine single-part cross-staff test remains in the
[test plan](../TEST_PLAN.md).

## Known validator false positive

The current `FMD003` rule reports a fatal finding for P1 measure 2 because
the tuplet-bearing timeline ends at 12 instead of 24. The author's Dorico
6.2.31 observation does not support that severity: no note loss or interrupted
import was reported.

This is a counterexample to the claim that every underfilled measure
containing a triplet causes a fatal import. FMD003 needs refinement, and
differences between observed Dorico versions need controlled investigation.
The earlier FATAL-02 and FATAL-03 results in 6.2.30 remain separate observations.

No new cross-staff fatal rule was added, and the validator was not changed
for this case. The discrepancy is recorded in the metadata.

## Evidence and source provenance

The Dorico result is an author report; no screenshot is preserved.
The MUSX was saved two seconds after the analyzed export, so exact
source/export parity is not established. The preserved XML is the
basis of the analysis.

## References

- [MusicXML 4.0 staff](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/staff/)
- [MusicXML 4.0 staves](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/staves/)

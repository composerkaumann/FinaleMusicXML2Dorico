# FATAL-04 complete triplet in Finale Voice 2

## Purpose

Test whether a complete triplet entered in Finale 27.4.1 Voice 2 imports
correctly into Dorico 6.2.30. FATAL-03 moved only the final triplet note
to Voice 2, and that exported note lost its tuplet association. Here the
entire triplet is entered in Voice 2 from the outset.

`FATAL-04` is a case ID; the observed result is a successful import.

## Finale preparation

1. Duplicate `BASE/FMD-BASE.musx` as `FATAL-04/FATAL-04.musx`.
2. In measure 2 only, enter four C4 quarter notes in Voice 1.
3. In Speedy Entry, move to the first Voice 1 C4 and press apostrophe
   (`'`) to start Voice 2 there. Confirm that Speedy Entry shows `V2`.
4. Set the entry pitch to G4. Press `Option+3` and enter three G4 quarter
   notes as a 3:2 triplet in Voice 2, followed by a G4 half note in that voice.
   Voice 2 now also lasts four quarter-note beats.
5. Save and export uncompressed `FATAL-04/FATAL-04.musicxml`, then import
   it into Dorico and inspect both voices and measures 2–4.

Do not use Edit Frame flags, layers, or Fill with Rests. This case contains
two voices entered normally in measure 2.

## XML checks and result

The preserved export has the intended structure:

- `divisions=6`; 4/4 requires 24 division units.
- Voice 1 contains four C4 quarter notes: `6 + 6 + 6 + 6`.
- Voice 2 contains three G4 triplet quarter notes: `4 + 4 + 4`,
  followed by a G4 half note lasting 12.
- Each voice independently reaches 24 units.
- The triplet starts and stops on Voice 2 notes; all three have 3:2
  `time-modification`.
- The XML is well-formed and uses `backup` elements between voices.
- Measures 1, 3, and 4 match BASE after normalizing division units.
- The validator reports no findings.

## Dorico result

The author reports an ideal import in Dorico 6.2.30. No screenshot is
preserved for this case.

A complete, correctly timed Finale Voice 2 triplet is not inherently fatal.
This successful control helps constrain future rules for the more specific
broken structure in FATAL-03.

## References

- [Finale for Mac Multiple voices](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Multiple_voices.htm)
- [Finale for Mac Tuplets](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Tuplets.htm)

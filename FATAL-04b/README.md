# FATAL-04b correct triplet with a simultaneous Voice 2 half note

## Purpose

Test a correctly defined Voice 1 quarter-note triplet in the second half
of measure 2, simultaneous with an ordinary Voice 2 half note. This is the
control for FATAL-04a: the intended difference is the tuplet definition's
note unit, not the entered music.

`FATAL` is a series ID; this control imports correctly.

## Finale preparation

1. Duplicate `FATAL-04a/FATAL-04a.musx` as
   `FATAL-04b/FATAL-04b.musx`. Both cases derive from BASE.
2. Open Tuplet Definition for the Voice 1 triplet and set both note-value
   choices to `Quarter(s)`: **three quarters in the space of two quarters**.
   Leave all notes, voices, and positions unchanged.
3. Save `FATAL-04b.musx`, export uncompressed `FATAL-04b.musicxml`,
   and import it into Dorico.

Do not use Edit Frame flags or Fill with Rests. If Finale moves the Voice 2
half note or changes Voice 1, describe the actual result rather than silently
repairing it.

## XML checks and result

- `divisions=6`; 4/4 requires 24 division units.
- The Voice 1 C4 half note lasts 12; the three G4 triplet quarter notes
  last `4 + 4 + 4`. The timeline ends at 24.
- The Voice 2 E4 half note starts at offset 12 and ends at 24.
- The triplet starts and stops in Voice 1. All three G4 notes have
  3:2 `time-modification` without an explicit `normal-type`,
  consistent with their `quarter` note value.
- Compared with FATAL-04a, the XML differs only by omission of three
  `<normal-type>half</normal-type>` elements.
- Measures 1, 3, and 4 match BASE after normalizing division units.
- The validator reports no findings.

## Dorico result

Dorico 6.2.30 imports the file successfully. The author reports an initial
rest in the downstem voice: this is the expected representation of Voice 2
starting later in the measure, not an extra beat or an import error.
The extra beats and hidden time signature seen in 04a were not reported.

A correct Voice 1 quarter-note triplet with a simultaneous ordinary Voice 2
half note does not cause the error observed in 04a.

## Source provenance

The MUSX file was saved after the analyzed MusicXML export. Exact
source/export state parity is not established by timestamps.

## References

- [Finale for Mac Multiple voices](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Multiple_voices.htm)
- [Finale for Mac Tuplet Definition](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/TPDLG.htm)

# FATAL-04a quarter-note triplet with a half-note definition

## Purpose

Test what Finale 27.4.1 exports when Voice 1 contains a quarter-note triplet
in the second half of measure 2, simultaneous with an ordinary Voice 2
half note, but the triplet definition is **three half notes in the space
of two half notes**.

The ratio is still 3:2, but the definition's note unit differs from the
entered notes. FATAL-04b uses the same music and simultaneous Voice 2 note
with the correct definition. The observed classification here is
**warning**, not fatal.

## Finale preparation

1. Duplicate `BASE/FMD-BASE.musx` as `FATAL-04a/FATAL-04a.musx`.
2. In measure 2 only, enter a C4 half note in Voice 1, followed by three
   G4 quarter notes as an ordinary 3:2 triplet.
3. Launch Voice 2 from the first G4 triplet note, at beat 3, and enter
   an ordinary E4 half note there. Do not make it a tuplet.
4. Open Tuplet Definition for the Voice 1 triplet. Change both note-value
   choices from `Quarter(s)` to `Half(s)`, retaining the numbers 3 and 2.
   Leave the three G4 notes and the Voice 2 E4 half note unchanged.
   Do not add rests.
5. Save `FATAL-04a.musx`, export uncompressed `FATAL-04a.musicxml`,
   and import it into Dorico.

To edit an existing triplet, use the Tuplet Tool, click its first note,
and double-click the handle. If Finale rearranges the measure after the
edit, preserve and describe that result. Do not use Edit Frame flags
or Fill with Rests.

## XML inspection

Check the durations and start positions in both voices, active division
units, measure extent, G4 `type` and `time-modification`, any
`normal-type`, tuplet start/stop and display units, and the `backup`
elements. Compare with FATAL-04b and with the BASE control measures.

## XML result

- The XML is well-formed, with `divisions=6` and a declared 4/4 duration of 24.
- Voice 1 has a C4 half note lasting 12, followed by G4 quarter notes
  lasting `4 + 4 + 4`. Its timeline ends exactly at 24.
- The Voice 2 E4 half note starts at offset 12, beat 3, and ends at 24.
  `backup` elements separate the voices.
- All three G4 notes have 3:2 `time-modification` and
  `normal-type=half`, while `type` remains `quarter`. They cover two
  beats, but the half-note definition describes four beats.
- Measure 2 contains no time-signature change in the XML.
- Measures 1, 3, and 4 match BASE after normalizing division units.
- `FMD005` reports one warning: the declared group span is 24 division
  units, but its notes cover 12.

This is a tuplet-definition inconsistency despite a complete overall
measure timeline. FATAL-04b differs only by omission of the three
`<normal-type>half</normal-type>` elements, isolating this XML difference
from the presence of the simultaneous Voice 2 half note.

## Dorico result

Dorico 6.2.30 completes the import. The author reports extra beats and a
hidden time signature in measure 2. The screenshot shows added rests and a
time-signature signpost; measures 3 and 4 remain. The exact number of added
beats was not established from the screenshot.

Classification: **warning**. The import continues, but measure 2 changes.

Evidence: [FATAL-04aDorico.png](FATAL-04aDorico.png).

The MUSX source was saved after the analyzed MusicXML export. Timestamps
alone do not establish exact source/export parity; the analysis refers
to the preserved XML.

## References

- [Finale for Mac Tuplet Definition](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/TPDLG.htm)
- [Finale for Mac Multiple voices](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/Multiple_voices.htm)
- [MusicXML 4.0 time-modification](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/time-modification/)
- [MusicXML 4.0 tuplet](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/tuplet/)

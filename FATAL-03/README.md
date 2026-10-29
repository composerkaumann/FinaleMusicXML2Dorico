# FATAL-03 Voice 2 Launch disrupts triplet import

## Purpose and original hypothesis

The original hypothesis was that Finale 27.4.1 would export a triplet's
start and stop with the same `number` on notes with different `voice`
values. That target signature was **not produced**. The export nevertheless
caused a different fatal import failure, described below.

## Finale preparation

1. Duplicate `BASE/FMD-BASE.musx` as `FATAL-03/FATAL-03.musx`.
2. In measure 2 only, enter three C4 quarter notes as a 3:2 triplet in Voice 1.
3. Follow them with a C4 half note. Initially this fills 4/4 exactly:
   two beats of triplet material followed by two beats of half note.
4. Open Edit Frame for measure 2: use Speedy Entry, close the entry frame,
   and Option-click the measure. Select the third triplet entry and enable
   both `Voice 2` and `V2 Launch`. The author observed that enabling
   `Voice 2` alone immediately rearranged the measure.
5. Save and export uncompressed `FATAL-03/FATAL-03.musicxml`.

Edit Frame is a low-level editor; the export determines which structure was
actually produced.

## Intended XML checks

The original target was a matching tuplet number with start and stop
attached to notes in different voices of the same part and measure.
Timeline durations and `backup`/`forward` elements were to be checked
separately, and measures 1, 3, and 4 compared with BASE after normalizing
`divisions`.

## Actual XML result

The XML is well-formed, but does not contain that target signature:

- The triplet starts on the first C4 quarter note in Voice 1.
- The third C4 quarter note is in Voice 2, without `time-modification`
  or a tuplet stop marker.
- The triplet stops on a half rest in Voice 1.
- The timeline ends at 16 division units, although 4/4 requires 24.

The existing `FMD003` rule detects the underfill. No additional rule was
introduced, and this file does not establish that Finale can export the
original cross-voice start/stop hypothesis. That remains a
[pending experiment](../TEST_PLAN.md).

Measures 1, 3, and 4 match the reference rhythm after normalization.

## Dorico result

In Dorico 6.2.30, the third triplet note becomes a rest and measures 3 and 4
disappear. Those measures exist in the MusicXML, so their loss occurs during
import. The author confirmed the result; no screenshot is preserved.

The case is fatal, but it does not isolate whether the subsequent measure
loss is caused by the displaced Voice 2 note, the Voice 1 tuplet stop on a
half rest, the underfilled timeline, or their combination.

## Source provenance

After the analyzed MusicXML export, `FATAL-03.musx` was saved again. Its
internal `score.dat` changed, and no new MusicXML export was made. Exact
parity between the current source and the preserved export is therefore
unverified. The Dorico observation and validator finding refer to the
existing MusicXML.

## References

- [Finale for Mac Edit Frame](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/SPFRMDLG.htm)
- [MusicXML 4.0 tuplet](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/tuplet/)
- [MusicXML 4.0 voice](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/voice/)

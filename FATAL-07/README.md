# FATAL-07 balanced Human Playback hidden trill notes

## Result

The author reports that both 07a and 07b open in Dorico 6.2.31, which ignores
07b's hidden notes. Both cases are nonfatal, and the validator reports no
findings.

The XML comparison confirms a Human Playback hidden-note sequence in 07b.
Its timeline is balanced; hidden notes alone do not justify a fatal rule.

## Control without applied Human Playback

[FATAL-07a.musx](FATAL-07a.musx) derives from the single-staff BASE.
Measure 2 contains a C4 half note with a trill mark, followed by a G4
half note. The [07a export](FATAL-07a.musicxml) contains:

- `divisions=2`.
- Durations `4 + 4 = 8`, or four quarter-note beats.
- Two visible notes in Voice 1.
- One `trill-mark`.
- No hidden notes or cue notes.

## Version with applied Human Playback

[FATAL-07b.musx](FATAL-07b.musx) is a copy of 07a with Apply Human Playback
applied to measure 2. The [07b export](FATAL-07b.musicxml) contains:

- `divisions=1024`; 4/4 requires 4096 division units.
- A visible C4 half note lasting 2048, now with `cue` and
  `type size="full"`. Its exact cue interpretation in Dorico was
  not separately verified.
- A `backup` of 2048, returning the cursor to the measure's start.
- Fourteen hidden notes in Voice 2, alternating C4 and D4.
- `print-object="no"` and `print-spacing="no"` on all 14 notes,
  with no `type`.
- Thirteen durations of 146 and a final duration of 150:
  `13 × 146 + 150 = 2048`, exactly two quarter-note beats.
- The visible G4 half note in Voice 1 then lasts 2048.
- The complete timeline ends at 4096, with no underfill or overflow.
- The trill mark is retained.

Measures 1, 3, and 4 match BASE in both exports after normalizing durations.
In addition to the changed division units, 07b places measure 1's tempo 120
in a separate `sound` element; the tempo value itself is unchanged.

## Validator conclusion

No new warning or fatal rule was added. Both files are regression controls:
a correctly timed Human Playback hidden-note sequence must remain unflagged.

Hidden notes still participate in timeline calculations together with
`backup` elements. The validator does not discard them as a general
exception, since their durations could break the timeline in another file.

This pair did not reproduce disruptive rhythmic residue. It does not
establish that all possible Human Playback exports are safe; that remains
a separate [planned investigation](../TEST_PLAN.md).

## Evidence and source provenance

The Dorico result is an author report; no screenshots or comparison exports
from Dorico are preserved. The later control measures were not separately
described in that particular report. Their equality is established in the
MusicXML, not independently in Dorico.

Both variants have separate MUSX and MusicXML files. Their sources were
saved after their respective exports: two seconds later for 07a and four
seconds later for 07b. Timestamps alone do not establish exact state parity;
the analysis uses the preserved MusicXML.

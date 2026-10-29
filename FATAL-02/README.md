# FATAL-02 tuplet timeline mismatch

## Purpose

Investigate a 3:2 triplet whose definition and edited member note values no
longer describe the same group. Voice 2, cross-staff notation, and hidden
notes are excluded to keep this case separate from the other experiments.

## Finale preparation

Duplicate `BASE/FMD-BASE.musx` and change only measure 2:

1. Enter three C4 quarter notes as a 3:2 triplet in Voice 1.
2. Change the third triplet note to a half note.
3. Leave the definition at three quarter notes in the space of two quarters.
4. Do not add another voice, cross-staff notes, hidden notes, or rests.
   Do not use Fill with Rests; that is the separate FATAL-02b condition.
5. Save [FATAL-02.musx](FATAL-02.musx) and export
   [FATAL-02.musicxml](FATAL-02.musicxml).

If Finale displays an export warning, continue the export and record it.
Whether a warning appeared in this particular test was not recorded.

## XML inspection

Check the active `divisions`, expected 4/4 duration, actual measure extent,
each note's `duration` and `type`, the 3:2 `time-modification`, and the
`notations/tuplet` start and stop boundaries. Compare measures 3 and 4 with
the reference material.

MusicXML represents intended duration, time modification, and displayed
tuplet boundaries separately.

## Dorico result

Dorico 6.2.30 completes the import but loses musical content:

- The first and second exported C4 notes remain.
- The third exported C4 half note disappears.
- Dorico inserts rests in place of missing time.

The result is shown in
[FATAL-02exportresult.png](FATAL-02exportresult.png).

## Classification

- Rule: `FMD003`.
- Severity: `fatal`.
- Category: `tuplet-timeline`.
- Current heuristic: a non-implicit measure containing a tuplet ends before
  the duration implied by its active time signature.

This file has an expected duration of 24 and an actual extent of 16 division
units, leaving a shortfall of 8. The observed loss of a note establishes the
case's fatal classification; the insertion of rests alone would not do so.
The broader heuristic has a known false positive in
[FATAL-05](../FATAL-05/README.md).

## Source provenance

The recorded MUSX checksum was corrected during the English documentation
update to match the source already present in Git. Neither the source nor
the export was modified. This checksum correction does not establish exact
source/export parity; the preserved MusicXML remains the import evidence.

# FATAL-06 manually edited Finale entry durations

## Test setup

Four C4 quarter notes were entered in measure 2 of the original single-staff
BASE. Only the second note's duration was edited through Edit Frame:

- Zero-duration attempt: Finale does not retain a Duration value of 0.
- 06a: Duration = 1 EDU.
- 06b: Duration = 1025 EDU.

A Finale quarter note is 1024 EDU. No MusicXML export was produced for the
rejected zero duration. The two positive-duration exports are preserved as
[FATAL-06a.musicxml](FATAL-06a.musicxml) and
[FATAL-06b.musicxml](FATAL-06b.musicxml).

## XML and Dorico results

| Variant | Entered second-note duration | XML divisions | Exported second-note duration | Note type | Classification |
| --- | --- | --- | --- | --- | --- |
| 06a | 1 EDU | 1024 | 1, or 1/1024 of a quarter note | Absent | Warning |
| 06b | 1025 EDU | 2 | 2, or one quarter note | Absent | Successful control |

In 06a, the very short duration survives export. Measure 2 contains
`1024 + 1 + 1024 + 1024 = 3073` division units, compared with the declared
4/4 duration of 4096. The second note has no `grace`, `type`, or
`time-modification`. Its duration equals a 4096th note.

The author reports unusual durations in Dorico and suspects that the importer
rounded them to nearby notatable values. The exact imported durations were
not recorded, and no Dorico export or screenshot is preserved. Measures 3
and 4 reportedly remained correct. This is a **warning**, not fatal.

In 06b, the second note's exported duration is already exactly a quarter note.
The difference between 1025 EDU and an ordinary 1024 EDU quarter note does
not survive MusicXML export: `2 + 2 + 2 + 2 = 8` fills 4/4 exactly.
The difference therefore cannot be attributed to normalization by Dorico.
The author reports four quarter notes and correct later measures.
Classification: **none**.

In both exports, measures 1, 3, and 4 match BASE after normalizing division
units. There is one part, with all notes in Voice 1. The Dorico version is
recorded as 6.2.31, the last version reported in the same test session;
the author did not repeat the number with the 06 results.

## Detection rule FMD006

FMD006 reports a warning for a pitched, non-grace note that:

- Has neither `type` nor `time-modification`.
- Has a positive duration shorter than a 1024th note.

06a produces one finding on the second note of P1 measure 2; 06b produces
none. Separate unit tests check the 1024th-note boundary and a shorter note
with an explicit tuplet ratio; neither should produce this finding.

MusicXML `type` is optional. Its absence alone is not an error.
The shortest directly named graphical note value is `1024th`.
This rule identifies a risk observed in this corpus, not an XSD violation.
The original zero-duration condition could not be produced through Finale.

## Source provenance

One shared [FATAL-06.musx](FATAL-06.musx) was saved after both XML exports.
Separate 06a and 06b MUSX snapshots are not preserved. Exact parity between
that shared source and either export is unverified; each variant's analysis
uses its preserved MusicXML.

## References

- [Finale Edit Frame and EDU](https://usermanuals.finalemusic.com/FinaleMac/Content/Finale/SPFRMDLG.htm)
- [MusicXML 4.0 note and optional type](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/note/)
- [MusicXML 4.0 note-type-value](https://www.w3.org/2021/06/musicxml40/musicxml-reference/data-types/note-type-value/)

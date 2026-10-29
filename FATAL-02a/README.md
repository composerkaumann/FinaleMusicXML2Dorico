# FATAL-02a full-measure mixed-duration tuplet

## Purpose

Compare FATAL-02 with a measure that is filled exactly while retaining a
mixed-duration 3:2 tuplet. This helps distinguish the observed behavior from
a general claim that all mixed-duration tuplets are fatal.

## Finale preparation

Duplicate `FATAL-02.musx` as `FATAL-02a.musx`. Change only the third C4
triplet note in measure 2 from a half note to a whole note.

The resulting material is:

- First C4: quarter note, 3:2.
- Second C4: quarter note, 3:2.
- Third C4: whole note, 3:2.
- The same tuplet starts on the first note and stops on the third.
- No rests are added.

With `divisions=6`, the expected durations are
`4 + 4 + 16 = 24`, exactly filling a 4/4 measure.

## XML and Dorico result

Dorico 6.2.30 imports the file successfully:

- All three tuplet notes remain.
- The exported measure timeline is exactly 24/24 division units.
- Measures 3 and 4 remain.
- The validator reports no findings.

Evidence: [Fatal02aDorico.png](Fatal02aDorico.png).

A mixed-duration 3:2 tuplet is therefore not inherently fatal. This successful
comparison does not establish that every fully filled tuplet measure will
import correctly, or identify the sole cause of FATAL-02.

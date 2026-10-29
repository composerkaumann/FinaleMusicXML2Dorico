# FATAL-02b overfilling rest after an incomplete tuplet

## Finale preparation

Measure 2 initially contains the same material as FATAL-02:

- C4 quarter note, 3:2.
- C4 quarter note, 3:2.
- C4 half note, 3:2.
- The tuplet starts on the first note and stops on the third.

Finale's Fill with Rests was then applied. It added a half rest even though
the available space no longer matched a half-note duration.

## XML result

- `divisions=6`.
- Expected duration of the 4/4 measure: 24.
- Tuplet note durations: `4 + 4 + 8 = 16`.
- Added half-rest duration: 12.
- Actual measure extent: 28.
- Overflow: 4 division units.

Only 8 division units were available before the added rest, but Finale
exported a rest lasting 12.

## Dorico result

Dorico 6.2.30 completes the import but loses the third exported C4 half note
and displays rests instead. The result is documented in
[Fatal02bDorico.png](Fatal02bDorico.png).

## Classification

- Rule: `FMD004`.
- Severity: `fatal`.
- Category: `tuplet-rest-fill-timeline`.

The current rule detects a measure containing tuplets and rests whose
timeline exceeds the active meter. The fatal classification is confirmed
for this particular export; the heuristic does not establish that all
overfilled measures containing tuplets and rests cause note loss.

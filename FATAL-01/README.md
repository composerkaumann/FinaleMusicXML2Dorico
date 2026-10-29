# FATAL-01 measure duration mismatch

## Test

Measure 2 contains three C4 quarter notes followed by one C4 half note:
five quarter-note beats in a 4/4 measure.

Finale displayed a warning during MusicXML export; export was continued.

## XML result

- `divisions=2`.
- Expected duration of the 4/4 measure: `8`.
- Note durations: `2 + 2 + 2 + 4`.
- Actual timeline extent: `10`.
- Overflow: `2`, or one quarter-note beat.
- The XML is well-formed.
- Measures 1, 3, and 4 are identical to the BASE export.

## Classification

- Rule: `FMD001`.
- Severity: `warning`.
- Category: `rhythmic-timeline`.
- Fatal in the observed Dorico 6.2.30 import: no.

The rule applies when the furthest position reached by a part's measure
timeline exceeds the duration implied by the active time signature.

## Dorico result

Dorico 6.2.30 completed the import and inserted a hidden local time-signature
change in measure 2. Measures 3 and 4 remained correct.

In this single-part test, isolated measure overflow did not interrupt the
import. Dorico retained five beats by changing the local meter.

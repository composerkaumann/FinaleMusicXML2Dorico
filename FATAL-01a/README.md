# FATAL-01a conflicting measure durations between parts

## Purpose

Test how Dorico handles different durations in the same measure of two
simultaneous instruments.

## Finale test

A two-instrument copy was made from FMD-BASE. In measure 2:

- P1 contains three C4 quarter notes and one C4 half note: five beats.
- P2 contains four C4 quarter notes: four beats.

Measures 1, 3, and 4 are rhythmically complete in both instruments.

Files: [FATAL-01a.musx](FATAL-01a.musx) and
[FATAL-01a.musicxml](FATAL-01a.musicxml).

## XML result

- Both parts declare a 4/4 measure duration of 8 division units.
- P1 measure 2 reaches 10 units.
- P2 measure 2 reaches 8 units.
- The difference is 2 units, or one quarter-note beat.
- The XML is well-formed.

The validator reports `FMD001` for the overflow in P1 and `FMD002` for the
difference between parts. Both findings have severity `warning`.

## Dorico result

Dorico 6.2.30 completed the import and added a quarter rest to the second staff.

This is consistent with Dorico using the longer P1 timeline of 10 units and
padding P2 with the missing 2 units. That explanation is an inference from
the XML and the observed result, not a traced importer operation.

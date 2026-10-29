# Finale 27.4.1 to MusicXML to Dorico Validator

A controlled test corpus and prototype validator for MusicXML exported from
Finale 27.4.1. The project investigates structures that can cause Dorico to
lose notes, omit subsequent measures, or otherwise import music incorrectly.

The corpus contains small, purpose-built test cases created by the project
author, not excerpts from third-party scores. It includes failures, warnings,
and successful controls. The `FATAL-` folder prefix is a historical test ID,
**not a claim that every file causes a fatal import**.

[GitHub repository](https://github.com/composerkaumann/FinaleMusicXML2Dorico)

## For Steinberg reviewers

Start with the preserved MusicXML exports below. They are the inputs underlying
the recorded Dorico observations. Where source/export parity is uncertain,
regenerating an export from the Finale source may produce a different file.

| Observed failure | Input and analysis | Comparison | Dorico version |
| --- | --- | --- | --- |
| An exported C4 half note disappears | [FATAL-02 XML](FATAL-02/FATAL-02.musicxml), [analysis](FATAL-02/README.md) | [FATAL-02a](FATAL-02a/README.md) fills the measure | 6.2.30 |
| Fill with Rests overfills the measure and an exported note disappears | [FATAL-02b XML](FATAL-02b/FATAL-02b.musicxml), [analysis](FATAL-02b/README.md) | [FATAL-02a](FATAL-02a/README.md) is a successful control, not a single-variable pair | 6.2.30 |
| The third triplet note becomes a rest and measures 3–4 disappear | [FATAL-03 XML](FATAL-03/FATAL-03.musicxml), [analysis](FATAL-03/README.md) | [FATAL-04](FATAL-04/README.md) tests a complete Voice 2 triplet, not a single-variable pair | 6.2.30 |

Each case folder includes an English analysis and machine-readable metadata.
Four screenshots document selected imports. Other observations are explicitly
identified as author-reported results. No new Finale or Dorico imports were
performed for the English documentation update of 29 October 2026.

For this project, **fatal** includes musical data loss even when Dorico
completes the import. Added rests, hidden time-signature changes, and layout
differences are classified separately rather than automatically called fatal.

The [test plan](TEST_PLAN.md) describes pending experiments and original
hypotheses that existing exports did not establish. These are not completed
tests or confirmed failures.

## Architecture and scope

Validation operates on the actual exported MusicXML, because the relevant
input is what Finale writes and Dorico receives. The existing Python core
has a CLI and can read uncompressed MusicXML and compressed `.mxl` containers.
It is a research prototype, not a complete MusicXML validator or a guarantee
of successful Dorico import.

The longer-term design is one validation core shared by a web validator and
Finale integration on Windows and macOS. A future Finale plug-in would export
MusicXML, run validation, display findings, and navigate to the relevant
measure, staff, or entry. The plug-ins and web interface are not implemented.

## Corpus design

Each test isolates a specific edit in measure 2 of a four-measure reference.
Measures 1, 3, and 4 contain control material. Most cases use one staff;
FATAL-01a adds a second instrument, and FATAL-05 uses the two-staff reference.
Variants may be derived from an earlier test to form a comparison pair.

The project author performs the Finale and Dorico operations manually:

1. Duplicate the reference or the documented comparison case.
2. Make the intended edit in measure 2.
3. Save `.musx` and export uncompressed `.musicxml`.
4. Import the export into Dorico.
5. Record what changes or disappears, including later control measures.

XML analysis, metadata, classification, and justified detection rules are
then added to the repository. XML well-formedness, timeline consistency,
and observed Dorico behavior are separate kinds of evidence.

## Reference files

The author used Finale 27.4.1 for Mac; the exports identify the application
as Finale 27.4. The main reference is
[FMD-BASE.musx](BASE/FMD-BASE.musx) and
[FMD-BASE.musicxml](BASE/FMD-BASE.musicxml):

- MusicXML 4.0, `score-partwise`, one part, four measures in 4/4.
- `divisions=2`; the expected measure duration is 8 division units.
- Measure 1: four C4 quarter notes.
- Measure 2: a whole-measure rest, duration 8, ready for the test edit.
- Measure 3: G4–F4–E4–D4 quarter notes.
- Measure 4: C4–E4–G4–C5 eighth notes followed by a G4 half note.

The [two-staff reference](BASE/FMD-BASE-2STAFF.musicxml) exports as two
separate single-staff parts, not one multi-staff part. P1 matches the original
reference material; P2 contains whole-measure rests. Detailed descriptions
and checksums are in [metadata.json](BASE/metadata.json) and
[metadata-2staff.json](BASE/metadata-2staff.json).

## Case catalogue

The repository contains 16 MusicXML exports: two references and 14 test
exports. It also contains 15 Finale source files and four evidence screenshots.
The rejected zero-duration attempt has no MusicXML export; 06a and 06b share
one preserved Finale source snapshot.

| Case and analysis | Test condition | Observed Dorico result | Classification |
| --- | --- | --- | --- |
| [FATAL-01](FATAL-01/README.md) | Five quarter-note beats in 4/4 | 6.2.30 adds a hidden local time signature; measures 3–4 remain intact | Warning |
| [FATAL-01a](FATAL-01a/README.md) | Simultaneous parts contain five and four beats | 6.2.30 adds a quarter rest to the shorter part | Warning |
| [FATAL-02](FATAL-02/README.md) | Underfilled measure with a mixed-duration 3:2 triplet | 6.2.30 loses the exported C4 half note and inserts rests | Fatal |
| [FATAL-02a](FATAL-02a/README.md) | Mixed-duration triplet fills the measure exactly | 6.2.30 preserves the notes and measures 3–4 | Successful control |
| [FATAL-02b](FATAL-02b/README.md) | Fill with Rests adds a half rest longer than the available space | 6.2.30 loses the exported C4 half note | Fatal |
| [FATAL-03](FATAL-03/README.md) | Voice 2 Launch on the last triplet entry | 6.2.30 replaces that note with a rest; measures 3–4 disappear | Fatal; precise cause not isolated |
| [FATAL-04](FATAL-04/README.md) | Complete, correctly timed triplet in Finale Voice 2 | Correct import in 6.2.30 | Successful control |
| [FATAL-04a](FATAL-04a/README.md) | Quarter-note triplet has a half-note definition, with simultaneous Voice 2 half note | 6.2.30 adds beats, rests, and a hidden time signature; import continues | Warning |
| [FATAL-04b](FATAL-04b/README.md) | Same material with the correct triplet definition | Correct import in 6.2.30; initial downstem-voice rest is expected | Successful control |
| [FATAL-05](FATAL-05/README.md) | Cross-staff attempt; export contains two separate parts and no staff reassignment | 6.2.31 retains the notes on the source staff | Nonfatal; known validator false positive |
| [FATAL-06](FATAL-06/README.md) | Attempt to set an entry duration to zero | Finale does not retain zero; no export to import | Input rejected by Finale |
| [FATAL-06a](FATAL-06/README.md) | Second note has duration 1 EDU | Unusual durations in 6.2.31; later measures remain intact | Warning |
| [FATAL-06b](FATAL-06/README.md) | Second note entered as 1025 EDU | Export already contains four exact quarter notes; Dorico import is correct | Successful control |
| [FATAL-07a](FATAL-07/README.md) | Trill without applied Human Playback | Correct import in 6.2.31 | Successful control |
| [FATAL-07b](FATAL-07/README.md) | Human Playback adds 14 hidden notes on a balanced timeline | 6.2.31 reportedly ignores the hidden notes | Successful control |

The 06 results use the last reported Dorico version in that test session,
6.2.31; the version number was not repeated with that observation. The case
analyses retain any additional evidence and source/export limitations.

## Running the validator

Run from the repository root using Python 3.10 or later. The core uses only
the Python standard library.

```sh
python3 tools/fmd_validator.py BASE/FMD-BASE.musicxml
python3 tools/fmd_validator.py FATAL-02/FATAL-02.musicxml --json
python3 -m unittest discover -s tests -v
```

Exit codes are `0` for no findings, `1` for findings of any severity, and `2`
for an input error. `--json` produces machine-readable findings, not an
independent statement that Dorico will lose data.

| Rule | Current heuristic | Reported severity |
| --- | --- | --- |
| FMD001 | Measure extent exceeds the duration implied by its time signature | Warning |
| FMD002 | Parts with the same declared duration have different measured extents | Warning |
| FMD003 | A non-implicit measure containing a tuplet is underfilled | Fatal; known false positive in FATAL-05 |
| FMD004 | A measure containing a tuplet and rests is overfilled | Fatal; heuristic based on FATAL-02b |
| FMD005 | A complete, non-nested group within one measure covers less time than its explicit `normal-type` definition | Warning |
| FMD006 | A pitched non-grace note without `type` or `time-modification` is shorter than a 1024th note | Warning |

## Known limitations and provenance

- **FMD003 overclassifies FATAL-05.** Dorico 6.2.31 did not exhibit the fatal
  behavior predicted by the heuristic. Underfill plus a tuplet is not a
  sufficient general test for fatality. The earlier 6.2.30 observations remain
  separate results, not a controlled comparison of Dorico versions.
- FMD002 compares raw division values rather than fully normalizing different
  part-local units. Nested or cross-measure tuplets, some implicit tuplet
  encodings, and decimal durations are not fully handled. Only
  `score-partwise` is supported, and no full XSD validation is performed.
- FMD004 is also a corpus-derived heuristic, not proof that every overfilled
  measure with tuplets and rests loses notes in Dorico.
- Several `.musx` snapshots were saved after their analyzed XML exports.
  FATAL-03 was resaved without re-exporting; 06a and 06b have no separate
  source snapshots. The preserved MusicXML is the basis of the observations,
  and source/export equivalence must not be assumed from the filenames.
- Metadata contains SHA-256 checksums for all 35 corpus assets. The English
  documentation update corrects the previously mismatched FATAL-02 MUSX
  checksum and truncated FATAL-03 XML checksum; it does not change either file
  or establish new source/export parity.

## Pending tests and research

[The test plan](TEST_PLAN.md) gives preparation instructions, XML targets,
controls, and Dorico checks for experiments that remain to be performed.
It also records unfulfilled original hypotheses, including cross-voice
tuplet boundaries and genuine cross-staff encoding within one part.

[The 13 October 2026 research note](research/2026-10-13-fatal-import-candidates.md)
and [public-sample audit](research/2026-10-13-public-sample-audit.json) catalogue
external reports separately from the author's test corpus. Historical forum
reports are not newly confirmed failures in the tested Dorico versions.
These research records link to external examples; the external score files
are not part of this repository.

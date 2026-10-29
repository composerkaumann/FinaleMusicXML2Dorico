# Research into Dorico import interruption and note loss

Research date: 13 October 2026. The target workflow is actual MusicXML exports
from Finale 27.4.1 into Dorico 6.2.31. This research did not change the
validator or add completed cases to the controlled corpus.

The strongest next Finale candidate is a tuplet definition using a smaller
note unit than the entered music. External cases also show that a complete
measure duration does not establish a consistent tuplet structure. Beyond
rhythm, one recent hang involved 1651 identical dynamics in a single measure.

Here, fatal includes note loss, omission of subsequent music, refusal to
open, and an import hang or crash. An added rest, hidden time-signature
change, or layout difference alone is not considered fatal.

## Evidence and scope

The descriptions distinguish reported symptoms, proposed or diagnosed
causes, and the project's own XML inspection. None of the external samples
was imported into Dorico 6.2.31 by this research. They are candidates, not
newly confirmed local fatal cases.

Sources included Steinberg forums and official Dorico materials, MakeMusic
community/support pages, Finale Forum, IRCAM/OpenMusic, Opusmodus, and
Reaper/Cockos-related reports. Some Finale Forum pages were available only
as indexed text, and the Cockos page stopped at a browser check. Private
Facebook groups and support tickets were outside the search.

Public attachments were inspected in a temporary directory. The external
score files are not included in this repository. Their checksums, locations,
and measured observations are preserved in
[public-sample-audit.json](2026-10-13-public-sample-audit.json).
They are separate from the author's purpose-built test corpus.

The [pending test plan](../TEST_PLAN.md) develops these candidates into
preparation instructions and identifies unresolved original hypotheses.

## Research candidates

| ID | Structure | Export origin | Evidence | Dorico 6.2.31 status |
| --- | --- | --- | --- | --- |
| C01 | Definition uses a smaller unit than the entered notes | Finale | Problem localized; repaired import confirmed | Not retested locally |
| C02 | Group rounding compensated outside the tuplet | MuseScore | Dorico team diagnosis and public XML | Historical; not retested locally |
| C03 | Inconsistent tuplets in simultaneous voices | Soundslice OMR | Dorico developer diagnosis and public XML | Not retested locally |
| C04 | Excessive identical dynamics at one position | MuseScore; failure reportedly survives Finale re-export | Original/fixed pair and multiple users | Exact reported build unknown |
| C05 | Hidden Human Playback residue with inconsistent timing | Finale | Official Dorico guidance and user recollection | Balanced local 07b succeeds |

### C01 smaller note unit in the definition

A 2021 Finale import omitted the last 12 measures while retaining chord
symbols. Another user reproduced the problem; deleting measure 41 of the
vocal part repaired the import. Finale's Check Region for Durations had
reported no problem. The identified triplet was defined as 3:2 32nd notes
when it should have been 3:2 16th notes.
[Case and confirmation](https://forums.steinberg.net/t/xml-issue/746844).

This is the opposite direction from local 04a, where a larger definition
unit caused extra beats but did not interrupt import. The original failing
XML was not inspected in this research. The thread provides a Finale source
and a repaired export, not an independently checked original failing XML.
The exact historical Dorico version is unspecified.

A possible controlled experiment uses a half note followed by a correct
quarter-note triplet in measure 2, then changes only the definition to
three eighths in the time of two eighths. No Voice 2, hidden notes, or
Fill with Rests should be added. The actual export must establish whether
the timeline remains four beats; that must not be assumed.

Future checks should compare actual group extent with its definition in
both directions. Current FMD005 checks only certain groups shorter than
an explicit `normal-type` span.

### C02 rounding corrections outside the group

In a 2016–2017 MuseScore case, Daniel Spreadbury reproduced a Dorico crash.
His account of Richard's diagnosis identified 17:12 groups in measures 78/79
and a 25:12 group in measure 99. The exporter compensated rounding after
the group with `forward` or `backup`. The reported consequences were a
crash for an underfull group and corruption of the subsequent voice stream
for an overfull group.
[Dorico team analysis](https://forums.steinberg.net/t/problem-opening-large-musicxml-files/85024).

Inspection of the public XML confirmed `divisions=480`: twelve 32nd notes
occupy 720 division units. Measures 78/79 contain `17 × 42 = 714`, followed
by `forward=6`. Measure 99 contains `25 × 29 = 725`, then `backup=5`;
its 21:12 group contains `21 × 34 = 714`, then `forward=6`. These
calculations come from the attachment. The exact 25:12 note duration is
720/25 = 28.8, rather than the 24.8 stated in the forum post.

A whole measure can be complete while its group members fail to cover
their declared span. Finale's actual export of correct 7:4 or 17:12 groups
needs investigation. The ratios and integer rounding are not inherently
errors. This is a historical non-Finale case; current Dorico behavior may
differ.

### C03 inconsistent tuplets in multiple voices

In a 2024 Soundslice OMR export, measures after 16 were blank in Dorico.
Richard Lanyon identified incorrect tuplets in piano measure 15: a lower
right-hand voice intended as ordinary rhythm was also encoded with a
tuplet. The user confirmed the OMR error. Changing import preferences did
not repair the result.
[Developer diagnosis and public XML](https://forums.steinberg.net/t/musicxml-import-fails-in-dorico-but-is-ok-in-musescore/930724).

The inspected P2 measure 15 uses `divisions=96` and active 3/4. Its
maximum timeline extent is exactly 288 units. On the upper staff,
3:2 `time-modification` occurs in voices 1, 2, and 3. For example, the
Voice 2 G4 eighth note lasts 32 units, not an ordinary eighth's 48.
This measure has no explicit `notations/tuplet` start/stop markers;
that absence alone does not establish an XSD error.

The candidate is a partial or misplaced tuplet association, not the mere
presence of simultaneous voices. Local 04b is a successful two-voice
control. Soundslice's encoding does not establish that Finale Voice 2
Launch can produce the same structure; a native Finale export is needed.

### C04 excessive identical dynamics

On 5–6 August 2026, users reported an import hanging at 55%, requiring a
force quit. The failure reportedly persisted after re-export through both
Finale and Sibelius. Jeff Cox removed repeated `p` dynamics from cello
measure 108, and other users opened the repaired file successfully.
[Original/fixed pair and user checks](https://forums.steinberg.net/t/musicxml-import-problem/1038436).

The project's inspection found 1651 identical dynamics `direction`
elements in P21 measure 108, compared with one in the fixed file. Removing
1650 duplicates makes the parsed trees equal when tags, attributes, trimmed
text, and child order are compared. This is not a raw-byte comparison.
Both files identify MuseScore Studio 4.7.3 as their exporter. The Finale
re-export itself was not inspected.

This is a distinct non-rhythmic risk. The exact Dorico build, internal hang
mechanism, and dangerous repetition threshold remain unknown. An initial
validator check should be a justified density/duplicate warning, not a
claim that any two overlapping dynamics cause a fatal failure.

### C05 inconsistent Human Playback residue

Dorico's official Finale migration guide associates missing subsequent
music in some cases with hidden/grey Human Playback notes. It describes
notes added before playback and removed afterward that can sometimes
remain and introduce timing problems in MusicXML.
[Official explanation and cleanup guidance](https://blog.dorico.com/2024/09/finale-dorico-musicxml/).

In the project's forum thread, dan_kreider also recalled interrupted imports
associated with hidden playback notes, explicitly calling the recollection
anecdotal. Gretchenegen mentioned cue-note and fingering conversions, not
interrupted import. Neither reply supplies a new controlled fatal file.
[Replies in the project thread](https://forums.steinberg.net/t/seeking-musicxml-examples-of-serious-dorico-import-failures-finale-preflight-project/1042155).

Local 07b contains 14 hidden notes on a balanced timeline and reportedly
imports correctly in Dorico 6.2.31. A useful next case needs inconsistent
timing or another demonstrably different export structure.
`print-object="no"` alone does not justify a fatal finding, and successful
07b does not prove that all Human Playback residue is safe.

## Finale forums and other communities

A 2017 MakeMusic community report concerns Finale 25.4.0.155 on Mac:
Sibelius crashed and Dorico gave a parser error. Changing the extension
did not solve the original poster's problem; the file was sent to support.
No precise cause or public sample was established. This is a lead, not
a Finale 27.4.1 detection rule.
[MakeMusic discussion](https://makemusic.zendesk.com/hc/en-us/community/posts/115007007147-musicxml-v25-4-problem).

Accessible Finale Forum discussions mainly concerned migration layout and
notation workarounds. A fermata on a whole-measure rest in 4/8, for example,
prompted suggestions of a hidden 8:4 tuplet or a deliberately overfilled
measure. Such visually motivated techniques can create unusual rhythmic
structures, but the thread did not confirm a fatal Dorico import. This
search found no new precisely diagnosed current-version fatal case there.
[Rest and fermata discussion](https://www.finaleforum.com/viewtopic.php?t=23390),
[migration discussion](https://www.finaleforum.com/viewtopic.php?t=23098).

MakeMusic documents duplicated articulations in older files using
Implode/Explode or SmartScore-derived material. This is a separate Finale
data-quality issue, not evidence that articulations produce the C04 hang.
[MakeMusic support](https://makemusic.zendesk.com/hc/en-us/articles/360011131634-Articulations-Duplicated-and-Stacked-in-Finale-v26).

A 2019 IRCAM OpenMusic export displayed only some measures in Dorico.
The exporter developer confirmed and fixed bad instrument references
and a tuplet type of `nil`. This supports schema and reference checks,
but does not establish the same defect in Finale. Repeated valid
`instrument id` references are not prohibited by that account.
[Developer replies and repair confirmation](https://discussion.forum.ircam.fr/t/musicxml-and-dorico-vs-finale/20269).

In a 2021 Reaper export, unescaped ampersands in horn names prevented XML
parsing; encoding them as `&amp;` fixed the parser error. The problem
was invalid serialization, not the use of an ampersand in a name.
[Diagnosis and repair](https://forums.steinberg.net/t/fatal-error-cropped-up-first-time-for-no-apparent-reason/714367).

A 2024 Opusmodus thread reported that only six of eleven measures imported
into Dorico 5, without a precise XML diagnosis or repaired comparison pair.
Another application opening a file does not itself prove valid MusicXML
or establish the exact cause of Dorico's behavior.
[Opusmodus discussion](https://opusmodus.com/forums/topic/3682-dorico-5-xml/).

## Recent reports and version boundaries

A March 2026 Finale 27 to Dorico 6.2 report describes partial import.
Exporting parts separately localized the problem to a few first- and
second-violin measures. Tuplets were suggested by respondents, not confirmed
as the XML cause. This establishes a report of the symptom in the 6.2
generation, not continued failure of every historical example.
[Finale 27 and Dorico 6.2 report](https://forums.steinberg.net/t/musicxml-conversion-failed-partially/1026366).

Some related issues have already been fixed:

| Fix | Version | Official history location |
| --- | --- | --- |
| Import of mixed-note-value tuplets in Finale XML | 5.1.70 | Dorico 5, page 11 |
| Rare import crash with malformed rehearsal marks | 5.1.80 | Dorico 5, page 6 |
| Crashes importing flows, MusicXML, or MIDI into an existing project | 6.0.22 | Dorico 6, page 53 |
| Custom-clef import crash with Japanese/Chinese application language | 6.1 | Dorico 6, page 50 |

[Dorico 5 version history](https://blog.dorico.com/wp-content/uploads/Dorico_5.1.80_Version_History.pdf),
[Dorico 6 version history](https://blog.dorico.com/wp-content/uploads/2026/06/Dorico_6.2.30_Version_History.pdf).

The 5.1.70 fix does not mean that every malformed mixed-duration tuplet is
safe. Local 02/02b/03 are separate observations in Dorico 6.2.30. Likewise,
a difference between importing into an existing project and opening a new
file is not by itself an intrinsic fatal XML signature; record the context.

A schema error message is not automatically musical data loss. In a 2024
Dorico export, an empty `direction-type` generated a validation message,
but Richard Lanyon did not regard that empty element itself as causing bad
musical effects. The associated segno export defect was fixed in 5.1.60.
[Developer explanation](https://forums.steinberg.net/t/musicxml-export-import-problem/938722).

## Implications for the validator

The public samples were checked using core revision
`6f271290c08c21e9766d6d2929bf788055d695c7`:

| Sample | Current core findings | Important limitation |
| --- | --- | --- |
| C04 original and fixed XML | Zero for both | Repeated dynamics are not checked |
| C02 MuseScore XML | 12 overall; zero in measures 78/79/99 | The diagnosed groups are not identified |
| C03 Soundslice XML | 23 overall; zero in P2 measure 15 | The diagnosed multi-voice cause is not identified |

Findings elsewhere do not establish that the reported cause has been found.
These counts are neither an accuracy metric nor a Dorico import test.

The analysis suggests the following future work; no new rules were
implemented by this research:

1. Separate XML parsing, version-appropriate schema checks, and instrument/
   part references from prediction of Dorico behavior.
2. Use exact rational time, part-local division units, and the semantics of
   `note`, `chord`, `grace`, `backup`, and `forward`. Normalize
   units before comparing durations between parts.
3. Inspect groups and voices, including nested and cross-measure tuplets
   where needed. Consider `time-modification`, not only explicit
   `notations/tuplet` markers. A staff change need not be a voice change.
4. Include hidden notes in timeline calculations without treating their
   presence alone as an error. Retain 07b as a successful control.
5. Investigate excessive identical `direction` elements at one position;
   no general fatal threshold has been established.
6. Locate findings by part ID, measure sequence index and displayed measure
   number, voice, staff, entry index, and rational position within the measure.
   This supports the future Finale navigation layer; an XML voice is not
   necessarily a Finale layer.

MusicXML 4.0's `divisions` type is based on `decimal`: a positive
`duration` need not be an integer. The core's current `int()` assumption
is an implementation limitation, not proof that decimal durations are
invalid XML. The standard also distinguishes intended duration from
notated duration; their difference alone is not necessarily a tuplet error.
[W3C divisions](https://www.w3.org/2021/06/musicxml40/musicxml-reference/data-types/divisions/),
[positive-divisions](https://www.w3.org/2021/06/musicxml40/musicxml-reference/data-types/positive-divisions/),
[duration](https://www.w3.org/2021/06/musicxml40/musicxml-reference/elements/duration/).

Keep the FMD003 false positive in FATAL-05 visible. This research does not
justify blanket rules that an underfilled tuplet measure or multiple
voices always cause a fatal import.

## Suggested investigation order

1. C01: smaller-unit definition in a single-voice measure.
2. C02: Finale rounding in correct 7:4, then if needed 17:12 groups;
   first establish the actual export pattern.
3. C03: a control pair with partial or misplaced tuplet associations.
4. C04: dynamics accumulation, beginning with a small comparison before
   attempting very large counts.
5. C05: a reproducible inconsistent playback residue, if a native example
   becomes available; repeating correct Apply Human Playback adds no new type.

Each new Finale experiment remains a separate reference-derived file.
C01–C05 are research candidate IDs, not completed FATAL case numbers.
Classification and a detection rule require the actual export and
the author's Dorico result.

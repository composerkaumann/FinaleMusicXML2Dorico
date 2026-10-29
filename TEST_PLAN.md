# Pending tests and unresolved hypotheses

These experiments have not yet been completed in the controlled corpus.
They describe what remains to be built or verified, not additional confirmed
Dorico failures. The project author performs all Finale and Dorico operations
manually. This plan does not add new score files or change existing results.

The project currently has three confirmed data-loss cases, several warnings,
and successful controls. See the [case catalogue](README.md#case-catalogue)
for completed work and the
[research note](research/2026-10-13-fatal-import-candidates.md) for the external
reports behind the research candidates.

## Original series coverage

| Original topic | Completed work | What remains unresolved |
| --- | --- | --- |
| FATAL-01 measure duration mismatch | 01 and 01a recover with meter/rest changes | No fatal result established for these isolated conditions |
| FATAL-02 tuplet timeline mismatch | 02 and 02b lose a note; 02a imports correctly | Refine the heuristic using controls such as 05; underfill alone is insufficient |
| FATAL-03 tuplet start/stop voice mismatch | Voice 2 Launch causes data loss in the existing export | Both actual start and stop are in Voice 1; the originally targeted cross-voice boundary is still untested |
| FATAL-04 Finale Voice 2 and tuplets | 04 and 04b succeed; wrong larger-unit definition in 04a produces a warning | Smaller-unit definitions and other inconsistent multi-voice encodings remain untested |
| FATAL-05 cross-staff tuplet and ambiguous voice | Existing attempt imports nonfatally | XML contains two separate single-staff parts and no staff reassignment; a genuine single-part cross-staff example is still needed |
| FATAL-06 illegal duration | Finale rejects zero; 1 EDU and 1025 EDU variants are documented | No zero-duration export was produced in this corpus; a hand-edited XML would belong to a separate synthetic-input category |
| FATAL-07 Human Playback residue | Balanced 07a/07b controls succeed | No disruptive rhythmic residue has been reproduced |

## Preparation and evidence requirements

For each new case, duplicate the documented reference and change only
measure 2. Keep measures 1, 3, and 4 as controls. Use a separate file for each
condition and a separate source snapshot for each variant; do not repeat
the shared-source limitation of 06a/06b.

Save the source and preserve the exact analyzed MusicXML export. If Finale
becomes unsaved after exporting, retain the export and record any subsequent
save. A later save is not proof that the source still reproduces that export.
Do not silently replace an analyzed export with a new one.

Record the actual application versions, export warnings, and Dorico import
options. In Dorico, inspect the suspect note/group, rests, hidden meter
changes, and measures 3 and 4. Save a screenshot where useful. An import
completing without a dialog does not establish that its notes survived.

Inspect the XML before classifying the case. If Finale does not export the
target structure, record that outcome rather than claiming the intended
condition was tested. Do not add a detection rule solely because a planned
condition looks suspicious.

## Planned experiments

| Plan ID | Condition | Starting point | Status |
| --- | --- | --- | --- |
| PLAN-01 | Tuplet definition uses a smaller note unit than the entered notes | Single-staff BASE | Planned; research C01 |
| PLAN-02 | Tuplet rounding and correction outside the group | Single-staff BASE; one ratio per file | Planned; research C02 |
| PLAN-03 | Partial or misplaced tuplet structure in simultaneous voices | Correct two-voice material such as 04b | Planned; research C03 |
| PLAN-04 | Excessive identical dynamics at one rhythmic position | Single-staff BASE | Planned; research C04 |
| PLAN-05 | Human Playback residue with an inconsistent timeline | 07a as a clean reference | Planned; research C05 |
| PLAN-06 | Matching tuplet start/stop number across different XML voices | Full-measure single-staff reference | Planned; original FATAL-03 hypothesis |
| PLAN-07 | Genuine cross-staff tuplet within one multi-staff part | New verified multi-staff reference required | Planned; original FATAL-05 scope |
| PLAN-08 | Same preserved exports retested in one recorded Dorico version | Existing corpus, unchanged bytes | Planned; version comparison |

Plan IDs are descriptions, not assigned FATAL case numbers. Candidate IDs
C01–C05 refer to the historical research note. New corpus IDs should be
assigned as the experiments are actually performed, retaining their order.

### PLAN-01 smaller note unit in the definition

Purpose: test the opposite direction from 04a, where the definition used
half notes for entered quarter notes. An external Finale report describes
subsequent note loss with a definition using 32nds instead of 16ths.

Preparation:

1. Create a clean control in measure 2: a C4 half note followed by three
   C4 quarter notes in a correctly defined 3:2 triplet.
2. Save and export this control, then duplicate it for the variant.
3. Change only the triplet definition to three eighth notes in the space
   of two eighth notes. Leave the entered note values unchanged.
4. Do not add Voice 2, hidden notes, or Fill with Rests. Preserve whatever
   structure Finale actually exports after the definition change.

XML checks: actual/normal note counts and units; explicit `normal-type`;
displayed tuplet values; start/stop positions; note durations; group and
measure spans. Do not assume the measure remains four beats after the edit.

Dorico checks: the final triplet note, added rests or beats, hidden meter,
and measures 3–4. Compare with the correctly defined single-voice control.
No outcome or severity is assigned in advance.

### PLAN-02 rounding within and outside a tuplet

Purpose: determine how Finale 27.4.1 exports a correctly entered tuplet whose
individual durations do not divide evenly, and whether it produces the
external correction pattern described in research C02.

Preparation:

1. First use a correct 7:4 sixteenth-note group occupying one quarter-note
   beat in measure 2, followed by three ordinary quarter notes.
2. Save its own source and export; do not deliberately corrupt it.
3. If a larger ratio is needed, make a separate BASE-derived case with a
   17:12 32nd-note group occupying one and a half quarter-note beats,
   followed by a half note and an eighth note.
4. Keep each ratio in a separate file. Do not use Fill with Rests to mask
   an unintended duration mismatch.

XML checks: exact rational group span, the sum of member durations,
distribution of rounding between notes, and any adjacent `forward`/`backup`
that compensates outside the group. Correct rounding is not itself an error.
If Finale exports a different pattern, record it instead of forcing the
historical MuseScore encoding into the native Finale corpus.

Dorico checks: all group members, the following ordinary notes, and later
measures. A correctly imported export is a valuable additional control.

### PLAN-03 inconsistent tuplet structure in multiple voices

Purpose: distinguish valid simultaneous voices from a tuplet association
that covers only part of a voice or is attached to unintended notes.

Preparation: begin with a fully filled, correctly timed two-voice control,
such as the 04b pattern. Preserve its source and export before attempting a
variant. In the variant, attempt only the misplaced/partial tuplet condition
in measure 2. The exact native Finale editing procedure is not yet established;
it must not be presented as a proven way to generate the Soundslice example.

XML checks: voice identity, note onset and duration, `time-modification` on
every affected note, tuplet boundaries where present, and the cursor moves
between voices. A whole-measure extent of four beats does not establish
that the individual groups are consistent. Conversely, tuplets in both
voices can be perfectly valid.

Dorico checks: notes in both voices, subsequent measures, and whether a
reported failure is distinct from the existing FATAL-03 underfill. Any extra
change to the timeline must be recorded as a possible confounding factor.

### PLAN-04 repeated dynamics at one position

Purpose: investigate a non-rhythmic import hang associated with a very large
number of identical dynamics, not ordinary duplicate expressions.

Preparation: use a normal, fully filled measure 2 with one dynamic as the
control. Create separate variants with additional copies of that same dynamic
at the same rhythmic position, if the native Finale workflow preserves them.
Keep notes, meter, and voices unchanged. Check small counts first; the number
of copies needed to expose a problem in this environment is unknown.

XML checks: the number and equality of `direction` elements, dynamics and
sound values, offsets, and assignment to voices/staves. Confirm that the
export really contains the intended repetitions.

Dorico checks: completion versus unusually slow import or a hang. Record
the tested count and elapsed time; do not define a universal fatal threshold
from one example. Use score copies and save unrelated work before any stress
test. If native Finale does not preserve the condition, it remains unproduced
in this corpus; a synthetic XML stress case would be identified separately.

### PLAN-05 disruptive Human Playback residue

Purpose: find a hidden-note sequence that actually disrupts the rhythmic
timeline, rather than repeating the successful balanced 07b control.

Preparation: retain 07a as the clean trill reference. A new variant is useful
only if a reproducible Finale operation produces different residual playback
data. The workflow producing such a stale or inconsistent residue is not
established. Do not assume that applying Human Playback normally, interrupting
playback, or merely hiding a note will generate a failure.

XML checks: hidden-note and cue-note flags, durations, voices, backup/forward
moves, and the group/measure timeline including all hidden notes. Compare
against 07a and the balanced 07b structure.

Dorico checks: whether hidden playback notes are ignored, become visible, or
cause visible notes or later measures to disappear. Hidden-note presence
without data loss or a contradictory timeline is not a new fatal condition.

### PLAN-06 cross-voice start and stop boundaries

Purpose: investigate the original FATAL-03 hypothesis that a matching tuplet
number starts on a note in one XML voice and stops in another.

Preparation: begin from a complete, single-staff triplet measure. Attempt
the voice reassignment only in measure 2, preserving a correct comparison
export. The known Voice 2 Launch experiment is not sufficient: its actual
start and stop both remained in XML Voice 1, and it also underfilled the
measure. No proven native procedure for the target encoding is available.

XML checks: confirm the same part, matching tuplet number, and genuinely
different start/stop voices. Separately check all note durations and cursor
positions. If there is no such signature, mark the target as not produced.

Dorico checks: the affected group and measures 3–4. Do not ascribe any failure
solely to the voice boundary when the export also changes durations or leaves
another tuplet incomplete.

### PLAN-07 cross-staff tuplet within one part

Purpose: test an actual multi-staff part with a triplet note assigned to the
other staff. The existing FATAL-05 export did not encode this condition.

Prerequisite: create and verify a new four-measure, 4/4 reference that exports
as **one part with two staves**. The existing file named FMD-BASE-2STAFF
exports as two separate parts and is not a substitute. Keep the main
reference control material and document the additional staff's content.

Preparation: in measure 2, enter a correct G4–C4–G4 quarter-note triplet
followed by a C4 half note. Save a non-cross-staff control, then duplicate
it and move only the middle triplet note to the other staff using Finale's
cross-staff notation. Do not simultaneously move it to another voice or layer.

XML checks: one part, two declared staves, explicit target `staff` on the
cross-staff note, consistent voice identity, a retained final half note,
complete group and measure timelines, and unchanged control measures.
Layout coordinates alone do not meet the target.

Dorico checks: note retention, staff placement, voice continuity, and later
measures. A second variant with missing/ambiguous voice information should
be attempted only after the correctly encoded control is understood; it
would be a separate case, not an extra edit to the same experiment.

### PLAN-08 retest the same exports in a recorded Dorico build

Purpose: determine whether the different observed versions matter without
confounding them with new Finale exports.

Use the unchanged FATAL-02, 02b, 03, and 05 MusicXML files. Include successful
controls 02a, 04, 04b, and 07b. Record the exact installed Dorico build and
import settings for every result; do not presume that a version mentioned in
an earlier session is still installed. No upgrade is part of this plan.

Compare note loss, replacement rests, hidden time signatures, and the later
control measures. If a newer import differs, preserve a separate result record
and screenshot rather than overwriting the original 6.2.30/6.2.31 observation.

## Completion record for each experiment

A completed record should include the source and exact export paths,
SHA-256 checksums, application versions, the actual XML signature, observed
Dorico behavior, screenshot/export evidence where available, comparison with
its control, and a classification justified by that result. Failed attempts
to produce the intended XML are still useful and should be documented as such.

Only then should the experiment become a completed case or justify a new
validator rule. A fatal finding must distinguish observed musical data loss
or import failure from recovery by added rests or a changed local meter.

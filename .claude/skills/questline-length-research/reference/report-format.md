# Report format

The layout below is what the Genshin Impact Archon Quest report used,
and what a report is written against.
A report's markdown is hand-written;
everything derived from `analysis.json` sits in an HTML-comment placeholder
that `scripts/gen_docs.py` rewrites in place on every run,
so a re-harvest refreshes every figure without touching the prose.
The markers are shown below where they belong.

## Files

```
<report>/README.md                     index, game-specific method, caveats
<report>/00-<chapter-slug>.md          one per chapter, numbered in story order
<report>/report.py                     game configuration and structure
<report>/claims.py                     what the prose asserts about the data
<report>/data/wiki.json                which wiki, and how it records versions
<report>/data/analysis.json            accepted and rejected candidates, with reasons
<report>/data/acts.tsv                 act list extracted from the wiki
<report>/data/versions.json            act to release version, as sourced
```

## Chapter file

Lines in a `gen:` region are rewritten wholesale on every run,
so there is nothing to author inside one;
what is shown between the markers is what the filler puts there.

```markdown
<!--gen:heading-->
# <Chapter number>: <Chapter title>

**Region:** X | **Game versions:** A - B | **Entries:** N | **Estimated chapter length: H h MM min**
<!--/gen-->

(The words "Region" and "chapter" here are `region_label` and `container`
from the report's `report.py`, which default to those two.)

<two to five lines of story framing, one clause per line,
with any figure in it written as an f: marker:
<!--f:len_Act_II-->2 h 10 min<!--/f-->>

## At a glance

<!--gen:glance-->
| Act | Title | Estimate | Middle half | Uploads | Confidence |
| --- | --- | --- | --- | --- | --- |
| Act I | ... | 2 h 32 min | 2 h 11 min - 2 h 48 min | 9 | medium |
<!--/gen-->

**Total: <!--f:total-->H h MM min<!--/f-->**

## Pacing

<why this chapter times out the way it does: quest part counts, set pieces,
traversal load, acts that are outliers and why;
every figure in it an f: marker,
as in <!--f:len_Act_V-->4 h 50 min<!--/f--> >

## Acts

<!--gen:act-heading act="Act I"-->
### Act I - [<Act title>](<wiki URL>)
<!--/gen-->

<one or two lines on what happens, no spoiler warning theatre, just the beats,
any figure again an f: marker:
<!--f:parts_Act_I-->three<!--/f--> >
<!--gen:stats act="Act I"-->
<the derived superlative sentence, where the ranking gives one>

- **Estimated length:** 2 h 32 min
- **Sampled range:** 2 h 11 min to 2 h 48 min for the middle half (full spread 1 h 36 min to 3 h 08 min) across 9 playthrough uploads (5 further candidates screened out)
- **Confidence:** medium
- **Adventure Rank gate:** 40
- **Released in:** Luna VII (6.6)
- **Stability:** median -3% against an earlier, independent query set
- **Measured from the uploader's chapter markers:** 4 of 9 uploads
- **Quest parts (3):** Part one (34 min); Part two (56 min); Part three
<!--/gen-->

<!--gen:evidence act="Act I"-->
<details>
<summary>Evidence</summary>

| Length | Video title | Uploader | Views | Uploaded | URL |
| --- | --- | --- | --- | --- | --- |
| 1 h 36 min | ... | ... | 12,345 | 2026-05-20 | <https://www.youtube.com/watch?v=...> |

</details>
<!--/gen-->

## Sources

- Questline structure, act titles, quest parts and gates: <wiki links>
- Durations: the YouTube uploads listed under each act above.
See [README.md](README.md) for the method and its limits.
```

## Report `README.md`

```markdown
# <!--f:game-->Genshin Impact<!--/f--> <Questline>: How Long Each <Unit> Takes

<two to four lines saying what the report covers,
one clause per line>

**Total for the whole main questline: <!--f:grand_total-->H h MM min<!--/f-->** (<!--f:n_report_entries-->45<!--/f--> entries counting <!--f:units-->acts<!--/f-->, preludes and interludes, measured against <!--f:n_videos-->489<!--/f--> accepted uploads out of <!--f:n_candidates-->698<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->act<!--/f--> medians,
so treat it as an order of magnitude
rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |    <- the two headers are `container` and `region_label`
| --- | --- | --- | --- | --- | --- |
| Prologue: ... | Mondstadt | 1.0 | 3 | 2 h 53 min | [00-prologue-mondstadt.md](00-prologue-mondstadt.md) |
<!--/gen-->

## Longest and shortest <units>

<!--gen:extremes-->
| | Act | Estimate |
| --- | --- | --- |
| longest | Chapter IV, Act V: ... | 4 h 50 min |
| shortest | Chapter I, Act IV - Prelude: ... | 36 min |
<!--/gen-->

## Method

<what the repository README covers, linked, and then what this game
words differently: its structure page, its searches, its compilation
and partial phrasings>

The figures it screens and grades on:

<!--gen:thresholds-->
- <the screening depths, the marker coverage floor, the outlier bounds,
  the sample floor and the two confidence factors,
  each quoted from the pipeline's own constants>
<!--/gen-->

## Limits of this report

<what this game limits beyond the shared list, with any figure
written as an f: marker>

Data collected <!--f:date-->2026-08-18<!--/f-->.
```

## Conventions

- Estimates and ranges as `H h MM min`, minutes only under an hour.
- Escape `|` inside video titles as `\|` or the evidence table breaks.
- Wrap URLs in `<...>` so they autolink without a display-text duplicate.
- Keep the evidence tables inside `<details>`,
  otherwise the chapter file is unreadable at a glance.
- Report the screened-out count per act.
  A reader who sees "9 accepted, 5 screened out"
  knows the filtering was real without having to open the JSON.
- Order chapters by story order in the filename prefix, not alphabetically.
- The shared procedure and the shared caveats live once, in the repository
  README, which every report links to. A report's own method section carries
  only what its game words differently (its wiki page, its searches, its
  compilation and partial phrasings, all written out in its `README.md`)
  and the thresholds, which are filled from the pipeline's own constants.
- Surround every `gen:` block with a blank line and keep it out of a paragraph;
  a value inside a sentence uses the inline `f:` form, on one line.
  The one exception the reports themselves make is `gen:stats`,
  whose opener follows the act note's last line directly,
  because the derived superlative sentence belongs to that paragraph.
  It costs a paragraph break in the rendered page,
  which is the price of the region starting where the sentence does.
- Nothing inside a `gen:` region survives a run,
  annotations and explanations included.
  The `- **<gate>:**` bullet appears only where `report.py` names a `gate_label`,
  and a `~` on a view count marks one still rounded as the search listing gave it;
  both are the filler's doing, so neither can be documented from inside the block.

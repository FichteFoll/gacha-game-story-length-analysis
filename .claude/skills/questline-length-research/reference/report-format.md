# Report format

The layout below is what the Genshin Impact Archon Quest report used.
Generate it from `analysis.json` with a script rather than by hand,
so a re-harvest can regenerate every file.

## Files

```
<output>/README.md                     index, method, caveats
<output>/00-<chapter-slug>.md          one per chapter, numbered in story order
<output>/data/analysis.json            accepted and rejected candidates, with reasons
<output>/data/acts.tsv                 act list extracted from the wiki
<output>/data/versions.json            act to release version, as sourced
```

## Chapter file

```markdown
# <Chapter number>: <Chapter title>

**Region:** X | **Game versions:** A - B | **Entries:** N | **Estimated chapter length: H h MM min**

<two to five lines of story framing, one clause per line>

## At a glance

| Act | Title | Estimate | Middle half | Uploads | Confidence |
| --- | --- | --- | --- | --- | --- |
| Act I | ... | 2 h 32 min | 2 h 11 min - 2 h 48 min | 9 | medium |

**Total: H h MM min**

## Pacing

<why this chapter times out the way it does: quest part counts, set pieces,
traversal load, acts that are outliers and why>

## Acts

### Act I - [<Act title>](<wiki URL>)

<one or two lines on what happens, no spoiler warning theatre, just the beats>

- **Estimated length:** 2 h 32 min
- **Sampled range:** 2 h 11 min to 2 h 48 min for the middle half (full spread 1 h 36 min to 3 h 08 min) across 9 playthrough uploads (5 further candidates screened out)
- **Confidence:** medium
- **Adventure Rank gate:** 40
- **Released in:** Luna VII (6.6)
- **Stability:** median -3% against an earlier, independent query set
- **Measured from the uploader's chapter markers:** 4 of 9 uploads
- **Quest parts (3):** Part one (34 min); Part two (56 min); Part three

<details>
<summary>Evidence</summary>

| Length | Video title | Uploader | Views | Uploaded | URL |
| --- | --- | --- | --- | --- | --- |
| 1 h 36 min | ... | ... | 12,345 | 2026-05-20 | <https://www.youtube.com/watch?v=...> |

A `~` on a view count marks one that is still the rounded figure
from the search listing rather than an exact one.

</details>

## Sources

- Questline structure, act titles, quest parts and gates: <wiki links>
- Durations: the YouTube uploads listed under each act above.
See [README.md](README.md) for the method and its limits.
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

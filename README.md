# Gacha Game Story Length Analysis

How long the story questlines of gacha games take,
chapter by chapter and act by act,
measured from YouTube playthrough uploads
because the publishers document no playtimes.

Every figure here is an estimate derived from evidence that is kept alongside it:
each act lists the uploads it was measured from,
with runtime, uploader, view count, upload date and URL,
and the rejected candidates are kept too,
each with the reason it was rejected.
The prose around them is written by hand,
but its numbers are not:
each sits in a placeholder that the pipeline fills from that evidence,
and what the words claim beyond the numbers is asserted against it.

## Reports

| Game | Questline | Report |
| --- | --- | --- |
| Genshin Impact | Archon Quests | [genshin-impact/README.md](genshin-impact/README.md) |
| Honkai: Star Rail | Trailblaze Missions | [honkai-star-rail/README.md](honkai-star-rail/README.md) |
| Zenless Zone Zero | Phaethon's Story | [zenless-zone-zero/README.md](zenless-zone-zero/README.md) |
| Arknights: Endfield | Main Missions | [arknights-endfield/README.md](arknights-endfield/README.md) |

Each report opens with its own totals, its chapter index,
its longest and shortest entries,
and the caveats that apply to that game in particular.
The vocabulary differs by game:
Genshin Impact numbers acts, Honkai: Star Rail numbers missions,
Zenless Zone Zero numbers chapters, Arknights: Endfield numbers processes,
and each report uses the word its game and its uploaders use.

## How the numbers are made

The same pipeline produces every report,
and the steps below are shared by all of them.
What differs per game is named in that game's own Method section,
together with the exact thresholds the screening and the ratings use.

1. **Structure from the wiki.**
The chapter and act list, the titles, the quest parts
and the level gates come from the game's community wiki,
which is a Fandom wiki for every game here but Arknights: Endfield.
Fandom serves a Cloudflare challenge to plain HTTP clients,
so the pages are read through the MediaWiki API
(`/api.php?action=query&prop=revisions&rvprop=content`) instead.

2. **Durations from playthrough uploads.**
Every act is searched for on YouTube several ways:
by its title, by chapter plus act number,
and by the patch branding that recent uploads carry instead of act titles.
Recently released acts are searched deeper,
because they have far fewer uploads to draw on.
Each result is collected with its runtime, title, uploader,
view count and URL.

3. **A second pass over the candidates worth measuring.**
The search listing gives rounded view counts and no upload date,
so every candidate that was not discarded outright
is fetched again in full.
That yields exact view counts and upload dates,
and the uploader's own chapter markers.
YouTube rate-limits these requests,
so the pass covers as many as it manages
and the rest keep their figures from the search listing.

4. **Locating the act inside the upload.**
Where an uploader marked out their video with chapter markers,
the markers are matched against the act's quest parts,
its title and its number,
and the act is measured from those markers
rather than from the video's total runtime.
That drops the uploader's pre-roll and detours from the measurement,
turns an upload covering two acts into evidence for each of them,
and, where enough uploads marked the same quest part,
gives that part its own median.
A marker set that covers too little of a single-act upload is ignored:
those markers were something other than the quest parts,
and trusting them would under-measure the act.

5. **Screening.**
A candidate is discarded when its title marks it as something other than
a hands-on playthrough of exactly that act:
cutscene reels, cinematic edits, lore explainers, guides and reaction videos;
livestreams and let's-plays, whose idle chatter inflates runtime;
multi-act compilations,
unless their chapter markers located this act inside them;
uploads covering part of an act rather than all of it,
in the games whose uploaders split acts that way;
and uploads whose title does not name the act
either by name or by chapter plus act number.
Of the survivors, the outliers are dropped
as truncated or padded uploads.

6. **Estimate.**
The published figure is the **median** of the accepted uploads.
Where the sample carries it, the published range is the **middle half**
(the interquartile range), with the full spread given alongside it:
one padded upload widens a min-max range that is otherwise tight,
and says more about that uploader than about the act.
On a thin sample the range is simply the minimum and maximum,
and the confidence rating cannot rise above *low*.
From there, confidence follows how wide the middle half is,
and an act whose median moved against an earlier, independent set of queries
is *low* whatever its sample size says:
a figure that moves when the queries change was never settled.

## What these numbers do and do not mean

- They measure **video runtime of someone playing the act**,
which is the closest available proxy for how long the act takes.
They are not official figures;
the publishers do not document questline lengths.
- Runtime includes the traversal, dialogue and combat
that a player cannot skip,
but it also includes whatever detours the uploader took,
and it excludes the time a first-time player spends
re-reading dialogue or dying to a boss.
Treat the median as a middle estimate and the range as the real spread.
- Uploaders play at different speeds,
skip cutscenes to different degrees,
and record on different game versions.
Acts that were rebalanced or shortened after release
may be measured against older, longer uploads.
- The newest acts of any game have the fewest uploads to draw on,
so their figures are the softest,
and their confidence ratings say so.
- Each report names the further limits of its own game.

## Repository layout

One top-level directory per report,
holding the published markdown and the evidence it rests on:

- `README.md`, the index, the method and the game's caveats,
and one markdown file per chapter, linked from it.
Each act section carries a collapsed evidence table
with runtime, video title, uploader, view count, upload date and URL
for every accepted upload.
A view count prefixed with `~` came from the search listing
and is rounded; the rest are exact.
- `data/analysis.json` holds the same evidence in machine-readable form,
including the rejected candidates and the reason each was rejected.
- `data/acts.tsv` is the act list extracted from the wiki,
and `data/quest_parts.json` the quest parts of each act,
in the order the wiki gives them.
- `data/evidence/` holds the raw harvest, one file per act,
before any screening was applied,
and `data/enriched.tsv` the full metadata of the candidates
the second pass reached.
- `data/versions.json` maps each act to its release version,
as categorized on the wiki,
and `data/version_index.json` gives each version
its patch number and release date.
Both are fetched before the harvest,
because the harvest searches for version-branded upload titles.
- `data/baseline.json` holds the per-act medians
from the first, independent set of queries,
which is what the stability figure is measured against.
- `data/wiki.json`, `data/game.txt`, `data/chapter_keys.json`,
`data/query_templates.txt` and `data/compilations.txt`
are the inputs the pipeline is steered with,
joined by `data/partials.txt` where the game's uploaders split acts
across videos,
and by `data/act_keys.json` where a chapter has two acts of the same name.
- `report.py` is the game's configuration and structure,
and `claims.py` the assertions the prose is checked against.

The published markdown itself is hand-written.
Wherever a figure or a generated block belongs in it,
the file carries a placeholder written as an HTML comment,
and the pipeline rewrites the contents of those placeholders,
leaving the prose around them as it was written.

The scripts live once, in the `questline-length-research` skill
(`.claude/skills/questline-length-research/scripts/`),
shared by every report and specific to none:
`fetch_versions.py` and `harvest.sh` collect the candidates,
`topup.sh` widens a thin act's pool,
`analyze.py` screens them and computes the statistics,
`enrich.sh` fetches exact metadata and chapter markers for the survivors,
and `gen_docs.py` fills the marked regions of the markdown from `analysis.json`.
Adding a game is a new report directory, never a change to a script.

## Reproducing a report

From a report directory:

```bash
SKILL=../.claude/skills/questline-length-research/scripts
python3 $SKILL/analyze.py data --compare data/baseline.json
python3 $SKILL/gen_docs.py .
```

That round trip rewrites every derived figure and every generated table
in the tracked markdown from the harvested evidence,
and leaves the authored prose around them untouched:
on unchanged evidence it reproduces the tracked files byte for byte.
Re-running the harvest itself needs `yt-dlp` and takes tens of minutes;
the harvest, enrichment and top-up scripts are all resumable.

Every figure in the published prose sits in a placeholder
filled from `analysis.json` rather than written by hand,
and the claims the prose makes in words
("the longest act in the game", "the chapter centrepiece")
are asserted in each report's `claims.py` before any file is written.
A claim that no longer holds fails the build
and names the sentence to fix.

## License

Dedicated to the public domain under [CC0 1.0](LICENSE).
The measurements and the prose are free to use without attribution.
The linked YouTube uploads belong to their uploaders,
and the questline structure is taken from the games' Fandom wikis,
which publish under CC BY-SA.

# Honkai: Star Rail Trailblaze Missions: How Long Each Mission Takes

Duration estimates for every Trailblaze Mission of the main storyline,
from the Herta Space Station to Planarcadia,
each one backed by the YouTube playthroughs it was measured from,
plus the Trailblaze Continuances told alongside it,
which are measured the same way but kept apart from the main questline's figures.

**Total for the whole main questline: <!--f:grand_total-->130 h 31 min<!--/f-->** (<!--f:n_report_entries-->27<!--/f--> entries counting missions, measured against <!--f:n_videos-->359<!--/f--> accepted uploads out of <!--f:n_candidates-->838<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->mission<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Herta Space Station | Herta Space Station | 1.0 | 1 | 2 h 19 min | [00-herta-space-station.md](00-herta-space-station.md) |
| Jarilo-VI | Jarilo-VI: Belobog and the Underworld | 1.0 | 2 | 6 h 32 min | [01-jarilo-vi.md](01-jarilo-vi.md) |
| The Xianzhou Luofu | The Xianzhou Luofu | 1.0 - 1.3 | 3 | 6 h 39 min | [02-xianzhou-luofu.md](02-xianzhou-luofu.md) |
| Penacony | Penacony, the Land of Dreams | 2.0 - 2.7 | 5 | 23 h 21 min | [03-penacony.md](03-penacony.md) |
| Amphoreus | Amphoreus, the Eternal Land | 3.0 - 3.7 | 8 | 52 h 32 min | [04-amphoreus.md](04-amphoreus.md) |
| Planarcadia | Planarcadia | 4.0 - 4.7 | 8 | 39 h 08 min | [05-planarcadia.md](05-planarcadia.md) |
| Trailblaze Continuance | Worlds already visited | 1.4 - 4.5 | 9 | 34 h 38 min | [x1-trailblaze-continuance.md](x1-trailblaze-continuance.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->missions<!--/f-->

<!--gen:extremes-->
| | Mission | Estimate |
| --- | --- | --- |
| longest | Amphoreus, Mission 1: Heroic Saga of Flame-Chase | 8 h 20 min |
| longest | Penacony, Mission 3: In Our Time | 7 h 56 min |
| longest | Planarcadia, Mission 1: Welcome to Arcadia | 7 h 55 min |
| longest | Amphoreus, Mission 3: Through the Petals in the Land of Repose | 7 h 48 min |
| longest | Amphoreus, Mission 4: The Fall at Dawn's Rise | 7 h 21 min |
| shortest | The Xianzhou Luofu, Mission 3: Karmic Clouds Faded, War Banners Folded | 1 h 09 min |
| shortest | The Xianzhou Luofu, Mission 2: Topclouded Towerthrust | 2 h 01 min |
| shortest | Herta Space Station, Mission 1: Today Is Yesterday's Tomorrow | 2 h 19 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Honkai: Star Rail<!--/f-->:

- **Structure:** the chapter and mission list, the mission titles, the quest parts
and the Level gates come from the
[Trailblaze Mission page](https://honkai-star-rail.fandom.com/wiki/Trailblaze_Mission)
and the individual chapter and mission pages of the Honkai: Star Rail Wiki.
- **Searches:** For every mission, YouTube was searched four ways:
by world plus mission title, by mission title alone,
and twice by the patch branding recent uploads use instead of mission titles
("Honkai: Star Rail 4.4 Planarcadia Trailblaze Mission Walkthrough").
The continuances were searched the same way,
and then once more by the patch number and "Trailblaze Continuance",
the wording most of their uploads go by.
- **Compilations:** multi-mission uploads such as
"Full Amphoreus Trailblaze Quest" or "100% all missions",
which count only where their chapter markers
located this mission inside them.
- **Partial uploads:** uploads covering part of a mission rather than all of it,
which in this game means both the numbered kind ("Part 3")
and the kind titled after a single quest part of the mission,
unless their runtime says they cover the mission after all.
Two channels number their own sessions rather than the mission's parts
(Agent Potango's running "Part 122", TheXGamer's "(Part 1).")
and are screened out for good, whatever their runtime.
- **Trailblaze Continuance:** Versions 3.4, 4.4 and 4.5 each shipped
a Trailblaze Mission and a Trailblaze Continuance,
and the two run about as long,
so an upload naming only the patch number cannot tell them apart.
For those three versions, `data/act_aliases.json` counts such an upload
for the mission where it says "Trailblaze Mission", "Trailblaze Quest" or "Main Story",
and for the continuance where it says "Continuance"
(or, for the two Fate crossovers, "Fate collab").
The two halves of *Finest Duel Under the Pristine Blue*
carry the same title, and `data/act_keys.json` tells them apart
by the patch number, a "(I)" or "(II)", or a part number.
- **A runtime floor** (`data/min_minutes.txt`) sits under the shortest mission.
A new mission's first day brings dozens of single-scene clips
that name it and say nothing else about themselves,
and with no floor they outnumber the complete runs and become the median.

The figures it screens and grades on:

<!--gen:thresholds-->
- Missions released within the last four versions are searched twice as deep,
because they have far fewer uploads to draw on.
- A marker set covering less than 60 percent
of a single-mission upload is ignored,
as marking something other than the quest parts.
- Of the uploads that survive screening,
anything below half or above 1.8 times the median
is dropped as truncated or padded.
- From eight uploads on, the published range is the **middle half**
(the interquartile range), with the full spread alongside it;
below that it is the minimum and maximum.
- Confidence is *high* when the middle half spans a factor under 1.25
and *medium* under 1.5.
It is *low* on fewer than eight uploads,
and *low* for any mission whose median moved by 10 percent or more
against the medians of 2026-10-17 (`analyze.py --compare`),
whatever its sample size says.
- Missions resting on fewer than three uploads are published with their figures
but take no part in any ranking,
so none of them is called the longest or the shortest of anything.
<!--/gen-->

## Limits of this report

Beyond the limits every report in this repository shares,
listed in the [repository README](../README.md):

- The 1.0 missions are the hardest of all to measure.
The uploads that exist are the oldest on YouTube,
and the convention then was to cut a mission into scene-length videos,
so *In the Withering Wintry Night* in particular
rests on a small pool of genuinely complete runs.
- Planarcadia is the newest content sampled.
Walkthrough channels covered it thoroughly,
so the pools of its earlier missions are not thin,
but they have had the least time to settle,
and the accepted uploads of its opening mission
still disagree widely.
- *To Roll the Stars in Astropolis* (Version 4.5)
and *Dance With the Beast Before Moonrise* (Version 4.6)
leave Planarcadia for Astropolis,
but the wiki files both as Planarcadia chapters
and lists them under Planarcadia/Astropolis,
so this report counts them with Planarcadia.
- *Now, Lay Laughter to All Stars* (Version 4.7)
shipped on the day this report was collected.
Every upload behind it went up within hours of release,
by the channels fastest to post a complete run,
so its pool is the youngest in the report,
it rates *low* on sample size alone,
and its figures are the most likely to move on a re-harvest.
- *Memories are the Prelude to Dreams* is a Finality Mission:
supplemental Penacony story released long after the world was finished.
The Trial of Equilibrium missions are level-cap trials
rather than story.
Neither is part of the main progression,
so both are outside this report's scope.
- The Trailblaze Continuances are filed as a chapter of their own,
[x1-trailblaze-continuance.md](x1-trailblaze-continuance.md),
because the wiki types them apart from the Trailblaze Missions
and they are optional to the main progression.
Their total is in the chapter table above,
but not in the total for the main questline,
and they take no part in the rankings or the extremes table.
- Uploaders number the continuances their own way,
usually within a world ("Act V: Continuance II" for Astropolis's second),
where this report numbers them across the game, as the wiki does.
A title giving such a number is therefore read as naming another continuance,
which costs *How to Lose Your Way to the Top* an upload or so.
- The continuance pools were enriched only partly:
YouTube's bot check stopped the second pass
before it reached the candidates the last top-up searches found,
so those count with their search-listing runtime and no chapter markers.
- The stability figures here are measured against the medians of 2026-10-17,
taken after that day's screening changes,
rather than against the first, independent set of queries.
They say how far a figure has moved since,
not how much it depends on the queries,
so an act unsettled before that date is no longer flagged by drift alone.

Data collected <!--f:date-->2026-11-11<!--/f-->.

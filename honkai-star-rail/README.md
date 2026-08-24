# Honkai: Star Rail Trailblaze Missions: How Long Each Mission Takes

Duration estimates for every Trailblaze Mission of the main storyline,
from the Herta Space Station to Planarcadia,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: <!--f:grand_total-->118 h 21 min<!--/f-->** (<!--f:n_report_entries-->24<!--/f--> entries counting missions, measured against <!--f:n_videos-->240<!--/f--> accepted uploads out of <!--f:n_candidates-->652<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->mission<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Herta Space Station | Herta Space Station | 1.0 | 1 | 2 h 19 min | [00-herta-space-station.md](00-herta-space-station.md) |
| Jarilo-VI | Jarilo-VI: Belobog and the Underworld | 1.0 | 2 | 6 h 32 min | [01-jarilo-vi.md](01-jarilo-vi.md) |
| The Xianzhou Luofu | The Xianzhou Luofu | 1.0 - 1.3 | 3 | 6 h 45 min | [02-xianzhou-luofu.md](02-xianzhou-luofu.md) |
| Penacony | Penacony, the Land of Dreams | 2.0 - 2.7 | 5 | 22 h 48 min | [03-penacony.md](03-penacony.md) |
| Amphoreus | Amphoreus, the Eternal Land | 3.0 - 3.7 | 8 | 52 h 14 min | [04-amphoreus.md](04-amphoreus.md) |
| Planarcadia | Planarcadia | 4.0 - 4.4 | 5 | 27 h 43 min | [05-planarcadia.md](05-planarcadia.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->missions<!--/f-->

<!--gen:extremes-->
| | Mission | Estimate |
| --- | --- | --- |
| longest | Amphoreus, Mission 1: Heroic Saga of Flame-Chase | 8 h 20 min |
| longest | Planarcadia, Mission 1: Welcome to Arcadia | 8 h 01 min |
| longest | Penacony, Mission 3: In Our Time | 7 h 46 min |
| longest | Amphoreus, Mission 3: Through the Petals in the Land of Repose | 7 h 40 min |
| longest | Amphoreus, Mission 4: The Fall at Dawn's Rise | 7 h 20 min |
| shortest | The Xianzhou Luofu, Mission 3: Karmic Clouds Faded, War Banners Folded | 1 h 16 min |
| shortest | The Xianzhou Luofu, Mission 2: Topclouded Towerthrust | 2 h 00 min |
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
- **Compilations:** multi-mission uploads such as
"Full Amphoreus Trailblaze Quest" or "100% all missions",
which count only where their chapter markers
located this mission inside them.
- **Partial uploads:** uploads covering part of a mission rather than all of it,
which in this game means both the numbered kind ("Part 3")
and the kind titled after a single quest part of the mission,
unless their runtime says they cover the mission after all.

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
against the earlier, independent set of queries (`analyze.py --compare`),
whatever its sample size says.
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
so the pools are not thin,
but they have had the least time to settle,
and the accepted uploads of its opening mission
still disagree by a factor of two.
- Astropolis and its mission *To Roll the Stars in Astropolis*
are still upcoming content at the time of writing (Version 4.5),
so there is nothing to measure yet.
- *Memories are the Prelude to Dreams* is a Finality Mission:
supplemental Penacony story released long after the world was finished.
The Trial of Equilibrium missions are level-cap trials
rather than story.
Neither is part of the main progression,
so both are outside this report's scope.

Data collected <!--f:date-->2026-08-18<!--/f-->.

# Genshin Impact Archon Questline: How Long Each Act Takes

Duration estimates for every main act of the Archon Quest storyline,
from the Mondstadt Prologue to Chapter VII,
each one backed by the YouTube playthroughs it was measured from.

**Total for the whole main questline: <!--f:grand_total-->112 h 37 min<!--/f-->** (<!--f:n_report_entries-->45<!--/f--> entries counting acts, preludes and interludes, measured against <!--f:n_videos-->486<!--/f--> accepted uploads out of <!--f:n_candidates-->698<!--/f--> candidates).
That figure is the sum of the per-<!--f:unit-->act<!--/f--> medians, so treat it as an order of magnitude rather than a number anyone actually clocked end to end.

## Chapters

<!--gen:chapters-->
| Chapter | Region | Versions | Entries | Estimated length | Detail |
| --- | --- | --- | --- | --- | --- |
| Prologue: The Outlander Who Caught the Wind | Mondstadt | 1.0 | 3 | 2 h 53 min | [00-prologue-mondstadt.md](00-prologue-mondstadt.md) |
| Chapter I: Farewell, Archaic Lord | Liyue | 1.0 - 1.4 | 5 | 6 h 42 min | [01-chapter-i-liyue.md](01-chapter-i-liyue.md) |
| Chapter II: Omnipresence Over Mortals | Inazuma | 1.6 - 2.6 | 5 | 8 h 12 min | [02-chapter-ii-inazuma.md](02-chapter-ii-inazuma.md) |
| Chapter III: Truth Amongst the Pages of Purana | Sumeru | 3.0 - 3.5 | 6 | 16 h 04 min | [03-chapter-iii-sumeru.md](03-chapter-iii-sumeru.md) |
| Chapter IV: Masquerade of the Guilty | Fontaine | 4.0 - 4.7 | 6 | 17 h 16 min | [04-chapter-iv-fontaine.md](04-chapter-iv-fontaine.md) |
| Chapter V: Incandescent Ode of Resurrection | Natlan | 5.0 - 5.7 | 7 | 17 h 28 min | [05-chapter-v-natlan.md](05-chapter-v-natlan.md) |
| Song of the Welkin Moon (unofficially Chapter VI) | Nod-Krai, later Sumeru | 5.8 - Luna VII (6.x) | 11 | 35 h 33 min | [06-song-of-the-welkin-moon-nod-krai.md](06-song-of-the-welkin-moon-nod-krai.md) |
| Chapter VII: Everwinter Without Mercy | Snezhnaya | 7.0 | 2 | 8 h 29 min | [07-chapter-vii-snezhnaya.md](07-chapter-vii-snezhnaya.md) |
<!--/gen-->

## Longest and shortest <!--f:units-->acts<!--/f-->

<!--gen:extremes-->
| | Act | Estimate |
| --- | --- | --- |
| longest | Chapter IV, Act V: Masquerade of the Guilty | 4 h 50 min |
| longest | Song of the Welkin Moon, Act I: A Dance of Snowy Tides and Hoarfrost Groves | 4 h 43 min |
| longest | Chapter VII, Act II: Wraith's Nocturne | 4 h 27 min |
| longest | Chapter III, Act V: Akasha Pulses, the Kalpa Flame Rises | 4 h 27 min |
| longest | Song of the Welkin Moon, Act X: Truth Amongst the Pages of Purana | 4 h 13 min |
| shortest | Chapter I, Act IV - Prelude: Bough Keeper: Dainsleif | 36 min |
| shortest | Chapter II, Act II: Stillness, the Sublimation of Shadow | 50 min |
| shortest | Prologue, Act I: The Outlander Who Caught the Wind | 52 min |
<!--/gen-->

## Method

The pipeline, the evidence vault it leaves behind
and what these numbers do and do not mean
are described in the [repository README](../README.md).
Specific to <!--f:game-->Genshin Impact<!--/f-->:

- **Structure:** the chapter and act list, the act titles, the quest parts
and the Adventure Rank gates come from the
[Archon Quest page](https://genshin-impact.fandom.com/wiki/Archon_Quest)
and the individual chapter and act pages of the Genshin Impact Wiki.
- **Searches:** For every act, YouTube was searched four ways:
by chapter plus act label plus act title, by act title alone,
and twice by the patch branding recent uploads use instead of act titles
("Genshin Impact 6.6 Act 10 ...").
- **Compilations:** multi-act uploads such as
"Acts 9 & 10" or "Full Sumeru Archon Quest",
which count only where their chapter markers
located this act inside them.

The figures it screens and grades on:

<!--gen:thresholds-->
- Acts released within the last four versions are searched twice as deep,
because they have far fewer uploads to draw on.
- A marker set covering less than 60 percent
of a single-act upload is ignored,
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
and *low* for any act whose median moved by 10 percent or more
against the earlier, independent set of queries (`analyze.py --compare`),
whatever its sample size says.
<!--/gen-->

## Limits of this report

Beyond the limits every report in this repository shares,
listed in the [repository README](../README.md):

- The newest acts (Nod-Krai's later acts, Chapter VII)
have the fewest uploads to draw on,
so their figures are the softest.
They are marked *low* or *medium* confidence accordingly.
- Interlude Chapter acts
(*The Crane Returns on the Wind*, *Perilous Trail*,
*Inversion of Genesis*, *Paralogism*)
are Archon Quests but not part of the main chapter progression,
so they are outside this report's scope.

Data collected <!--f:date-->2026-08-18<!--/f-->.

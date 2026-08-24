"""What this report's prose asserts about the data, as checkable claims.

Every figure in the markdown is an `f:` marker filled from `analysis.json`, so
no number here can go stale. The words around them can: "the larger half of the
game", "the odd one out at under an hour", "the outlier of the whole report" are
all claims that would survive a re-harvest unchallenged. Each one is written
down next to the sentence it guards, and `gen_docs.py` checks the lot before it
writes a single file.
"""
from assertions import (count_above, is_extreme, median_between,
                        largest_chapter, rank_at_most, total_ratio_between)

CLAIMS = [
    # 01-chapter-i.md, Pacing
    rank_at_most(
        "ch1", "Process I", 2,
        "The chapter's weight sits in *The Broken Lands* and "
        "*Path of Ascension*, its two longest entries",
        scope="chapter"),
    rank_at_most(
        "ch1", "Process III", 2,
        "The chapter's weight sits in *The Broken Lands* and "
        "*Path of Ascension*, its two longest entries",
        scope="chapter"),
    count_above(
        "ch1", 120, 2,
        "and they are two of the five entries here to run past two hours"),
    median_between(
        "ch1", "Process II", 40, 59,
        "*The Turbid Heavens* is the odd one out at under an hour"),

    # 02-chapter-ii.md, Pacing
    largest_chapter(
        "ch2", "Chapter II is the larger half of the game"),
    total_ratio_between(
        "ch2", ["ch1"], 1.5, 2.2,
        "close to twice Chapter I over seven entries rather than five"),
    count_above(
        "ch2", 120, 2,
        "Two of those entries run past two hours "
        "and the rest sit between one and two"),
    median_between(
        "ch2", "Process V", 60, 120,
        "Two of those entries run past two hours "
        "and the rest sit between one and two"),
    rank_at_most(
        "ch2", "Process III", 3,
        "so the shape is three big stops with short connective tissue "
        "between them: *The Long Feud* ..., *Ruins in the Miasma* ..., "
        "and *The Way of Water* introducing Wuling in between",
        scope="chapter"),
    rank_at_most(
        "ch2", "Process VII", 3,
        "so the shape is three big stops with short connective tissue "
        "between them: *The Long Feud* ..., *Ruins in the Miasma* ..., "
        "and *The Way of Water* introducing Wuling in between",
        scope="chapter"),
    rank_at_most(
        "ch2", "Process II", 3,
        "so the shape is three big stops with short connective tissue "
        "between them: *The Long Feud* ..., *Ruins in the Miasma* ..., "
        "and *The Way of Water* introducing Wuling in between",
        scope="chapter"),
    is_extreme(
        "ch2", "Process VII", "max",
        "*Ruins in the Miasma* is the outlier of the whole report "
        "at over four hours",
        scope="global"),
    median_between(
        "ch2", "Process VII", 240, 359,
        "*Ruins in the Miasma* is the outlier of the whole report "
        "at over four hours"),
]

"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (count_above, is_extreme, median_between, none_above,
                        rank_at_most, sample_at_most, total_ratio_between)
from facts import RANK_SAMPLES

CLAIMS = [
    # README.md
    sample_at_most("v5", "Chapter 43", 1,
                   "and its figure rests on a single upload"),

    # 01-graffiti-art-to-eternal-engine.md
    count_above("v4", 240, 2,
                "in a report whose later chapters run for four and five"),
    is_extreme("v1", "Chapter 9", "max",
               "Chapters 9 and 10, are also the two longest of the ten"),
    rank_at_most("v1", "Chapter 10", 2,
                 "Chapters 9 and 10, are also the two longest of the ten",
                 scope="chapter"),
    is_extreme("v1", "Chapter 5", "min",
               "and the shortest chapter of the launch run"),
    sample_at_most("v1", "Chapter 7", 5,
                   "and its pool is the thinnest of the launch run"),

    # 02-nona-ouroboros-to-across-the-ruined-sea.md
    none_above("v1", 120,
               "Chapter 12 is the first chapter in the game to pass two hours"),
    median_between("v2", "Chapter 11", 1, 119,
                   "Chapter 12 is the first chapter in the game to pass two hours"),
    median_between("v2", "Chapter 12", 120, 600,
                   "Chapter 12 is the first chapter in the game to pass two hours"),
    sample_at_most("v2", "Chapter 18", 1,
                   "Rests on a single complete upload"),

    # 03-spiral-of-chronos-to-stars-ensnared.md
    total_ratio_between("v3", ["v1", "v2"], 0.8, 1.2,
                        "almost as much as the first twenty chapters "
                        "put together"),
    sample_at_most("v3", "Chapter 26", 0,
                   "Its pool holds no complete upload at all"),
    sample_at_most("v3", "Chapter 21", 1,
                   "and it rests on a single upload"),
    sample_at_most("v3", "Chapter 25", 2,
                   "Rests on two uploads that happen to agree closely"),
    sample_at_most("v3", "Chapter 27", 1, "Rests on a single upload"),
    sample_at_most("v3", "Chapter 28", 1, "Rests on a single upload"),

    # 04-shapers-ripples-to-steering-by-light.md
    sample_at_most("v4", "Chapter 38", 2,
                   "but it rests on two uploads"),
    sample_at_most("v4", "Chapter 38", RANK_SAMPLES - 1,
                   "too few for it to be ranked against the rest of the report"),
    median_between("v4", "Chapter 35", 1, 90,
                   "Chapter 35 comes out under the hour and a half"),
    sample_at_most("v4", "Chapter 35", 1,
                   "the one upload of it that survived screening"),
    sample_at_most("v4", "Chapter 42", 3,
                   "What survived screening is three uploads "
                   "that each cover part of it"),

    # 05-anchored-in-faith.md
    median_between("v5", "Chapter 43", 1, 90,
                   "is a fraction of the three hours and more"),
    count_above("v4", 180, 7,
                "that most chapters of Volume 4 run to"),
    sample_at_most("v5", "Chapter 43", 1,
                   "The one upload that survived screening went up "
                   "on release day"),

    # 06-ex-frozen-darkness-to-inscription-of-labyrinth.md
    is_extreme("vex", "Chapter EX-04", "max", "The longest of the EX chapters"),
    sample_at_most("vex", "Chapter EX-04", 3,
                   "which rests on three uploads"),
]

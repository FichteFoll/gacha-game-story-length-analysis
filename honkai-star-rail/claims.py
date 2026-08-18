"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (count_above, is_extreme, largest_chapter, none_above,
                        rank_at_most, total_ratio_between)

CLAIMS = [
    total_ratio_between("herta", ["jarilo"], 0.2, 0.6,
                        "the shortest chapter in the report by a wide margin"),

    is_extreme("jarilo", "Mission 1", "max",
               "The opener is the longer of the two"),

    is_extreme("luofu", "Mission 1", "max", "A long opening mission and then a "
               "steep taper"),
    is_extreme("luofu", "Mission 3", "min", "the shortest entry in the game",
               scope="global"),

    count_above("penacony", 180, 3,
                "{n_above_3h} of Penacony's {n_entries} missions run past three hours"),
    none_above("herta", 180,
               "where before it only Jarilo-VI and the Luofu had one at all"),
    count_above("jarilo", 180, 1,
                "where before it only Jarilo-VI and the Luofu had one at all"),
    count_above("luofu", 180, 1,
                "where before it only Jarilo-VI and the Luofu had one at all"),
    is_extreme("penacony", "Mission 3", "max",
               "and *{longest_title}* alone takes {longest_len}"),
    is_extreme("penacony", "Mission 5", "min",
               "The last two missions are the wind-down"),

    largest_chapter("amphoreus", "By far the largest chapter"),
    count_above("amphoreus", 180, 8, "Every one of them runs past three hours"),
    is_extreme("amphoreus", "Mission 1", "max",
               "*{longest_title}*, the arrival on Amphoreus, is the longest"),
    rank_at_most("amphoreus", "Mission 1", 1, "the longest mission in the game",
                 scope="global"),

    is_extreme("planarcadia", "Mission 1", "max",
               "The opening mission is the longest, at {longest_len}"),
    is_extreme("planarcadia", "Mission 4", "min",
               "the four after it settle between {shortest_len} and {len_Mission_2}"),
    rank_at_most("planarcadia", "Mission 2", 2,
                 "the four after it settle between {shortest_len} and {len_Mission_2}",
                 scope="chapter"),
]

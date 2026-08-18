"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (count_above, is_extreme, largest_chapter,
                        median_between, rank_at_most, total_ratio_between)

CLAIMS = [
    median_between("prologue", "Act I", 45, 75,
                   "Every act here lands within about a quarter hour of an hour"),
    median_between("prologue", "Act II", 45, 75,
                   "Every act here lands within about a quarter hour of an hour"),
    median_between("prologue", "Act III", 45, 75,
                   "Every act here lands within about a quarter hour of an hour"),

    median_between("ch1", "Act II", 100, 140,
                   "Acts II and III roughly double the Prologue's per-act length"),
    median_between("ch1", "Act III", 100, 140,
                   "Acts II and III roughly double the Prologue's per-act length"),

    median_between("ch2", "Act I", 120, 240, "marathon acts"),
    median_between("ch2", "Act III", 120, 240, "marathon acts"),
    is_extreme("ch2", "Act II", "min", "while Act II consists of only two quest "
               "parts and takes {len_Act_II}"),

    count_above("ch3", 120, 4, "Where the questline changes scale"),
    is_extreme("ch3", "Act V", "max", "Act V as the chapter centrepiece"),

    count_above("ch4", 120, 5, "The most consistently long chapter"),
    is_extreme("ch4", "Act V", "max", "and Act V, at {len_Act_V}, as its centrepiece"),

    is_extreme("ch5", "Interlude", "min", "The Interlude is the exception"),

    largest_chapter("sotwm", "By far the largest chapter"),
    total_ratio_between("sotwm", ["ch3", "ch4"], 0.9, 1.2,
                        "a running time comparable to Sumeru and Fontaine combined"),
    rank_at_most("sotwm", "Act I", 3, "Act I alone runs {len_Act_I}", scope="global"),

    rank_at_most("ch7", "Act I", 10, "but both are long", scope="global"),
    rank_at_most("ch7", "Act II", 10, "but both are long", scope="global"),
]

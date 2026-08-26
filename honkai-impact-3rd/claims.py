"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (count_above, is_extreme, largest_chapter,
                        median_between, none_above, rank_at_most,
                        sample_at_most, total_ratio_between)

CLAIMS = [
    is_extreme("wdb", "Chapter II", "max",
               "Chapter II is where the game stops explaining and starts "
               "telling, and it is the longer of the two"),

    none_above("teod", 60,
               "chapters that sit close together and stay under the hour"),
    is_extreme("teod", "Chapter VI", "max",
               "Babylon: the tower, the prisoner underneath it, "
               "and the longest of the four"),

    median_between("utfs", "Chapter VII", 5, 40, "Chapters VII and VIII are short"),
    median_between("utfs", "Chapter VIII", 5, 60, "Chapters VII and VIII are short"),
    median_between("utfs", "Chapter IX", 101, 600,
                   "and then Chapter IX runs to ..., "
                   "longer than the two of them together"),
    is_extreme("utfs", "Chapter IX", "max",
               "and the largest entry in the arc"),
    sample_at_most("utfs", "Chapter IX", 7,
                   "and the pool for it is thinner than for its neighbours "
                   "because most of its uploaders split it up"),

    is_extreme("ftdo", "Chapter XI", "max",
               "Chapter XI is the longest of them"),
    is_extreme("ftdo", "Chapter XI - EX", "min",
               "A single act, and the shortest entry of the arc"),
    median_between("ftdo", "Chapter XI - EX", 5, 59,
                   "only the EX chapter still fits inside an hour"),
    median_between("ftdo", "Chapter X", 61, 600,
                   "only the EX chapter still fits inside an hour"),
    median_between("ftdo", "Chapter XI", 61, 600,
                   "only the EX chapter still fits inside an hour"),
    median_between("ftdo", "Chapter XII", 61, 600,
                   "only the EX chapter still fits inside an hour"),

    sample_at_most("shooting_star", "Chapter XIII", 7,
                   "Both pools are small, and both estimates are rated "
                   "accordingly"),
    sample_at_most("shooting_star", "Chapter XIV", 7,
                   "Both pools are small, and both estimates are rated "
                   "accordingly"),

    is_extreme("ety", "Chapter XVI", "max",
               "Chapter XVI is the largest entry in it"),
    is_extreme("ety", "Chapter XVII", "min",
               "Chapter XVII, the storm the arc is remembered for, "
               "is the shortest of the three"),

    median_between("hlb", "Chapter XVIII", 60, 110,
                   "Two chapters of almost identical size"),
    median_between("hlb", "Chapter XIX", 60, 110,
                   "Two chapters of almost identical size"),

    is_extreme("txd", "Chapter XX", "max",
               "The arc's centrepiece, and the longest of its three chapters"),
    is_extreme("txd", "Chapter XXII", "min",
               "and the arc's shortest entry"),
    median_between("txd", "Chapter XXI", 100, 180,
                   "Chapter XXI is not far behind it"),

    count_above("rf", 180, 3,
                "Three chapters, every one of them past three hours"),
    is_extreme("rf", "Chapter XXIV", "max",
               "The legion theater, and the arc's longest entry"),

    is_extreme("tsa", "Chapter XXVII", "max",
               "with Chapter XXVII the largest of them"),
    sample_at_most("tsa", "Chapter XXV - EX", 7,
                   "No entry here rests on eight uploads"),
    sample_at_most("tsa", "Chapter XXVI", 7, "No entry here rests on eight uploads"),
    sample_at_most("tsa", "Chapter XXVII", 7, "No entry here rests on eight uploads"),
    sample_at_most("tsa", "Chapter XXVIII", 7, "No entry here rests on eight uploads"),

    sample_at_most("ttf", "Chapter XXXI", 5,
                   "and *Fur Elysia* in particular rests on a handful of "
                   "complete uploads"),

    sample_at_most("dotf", "Chapter XXXIII", 5,
                   "The truth, named. The pool for it is small"),

    is_extreme("atfots", "Chapter XXXVIII", "max",
               "By far the largest entry in the arc"),
    rank_at_most("atfots", "Chapter XXXVIII", 5,
                 "and one of the largest in the report", scope="global"),
    sample_at_most("atfots", "Chapter XXXVIII", 2,
                   "it rests on two complete uploads"),
    sample_at_most("atfots", "Chapter XXXVI", 7,
                   "Every entry here rests on a handful of them "
                   "and is rated *low*"),
    sample_at_most("atfots", "Chapter XXXVII", 7,
                   "Every entry here rests on a handful of them "
                   "and is rated *low*"),
    sample_at_most("atfots", "Chapter XXXIX", 7,
                   "Every entry here rests on a handful of them "
                   "and is rated *low*"),

    is_extreme("bts", "Chapter XLI", "max",
               "Worldly retribution, and the largest entry in the arc"),
    sample_at_most("bts", "Chapter XLI", 2,
                   "rest on two complete uploads each"),
    sample_at_most("bts", "Chapter XLII", 2,
                   "rest on two complete uploads each"),
    sample_at_most("bts", "Chapter XL", 7,
                   "The figures are the best the evidence supports "
                   "and no more than that"),
    sample_at_most("bts", "Interlude", 1,
                   "and the interlude on one"),

    sample_at_most("ttgb", "Chapter I", 3,
                   "the three numbered chapters are thin, "
                   "and Chapter I thinnest of all"),
    sample_at_most("ttgb", "Chapter II", 7,
                   "the three numbered chapters are thin"),
    sample_at_most("ttgb", "Chapter III", 7,
                   "the three numbered chapters are thin"),

    largest_chapter("datrow", "By a distance the largest arc in the report"),
    total_ratio_between("datrow",
                        ["wdb", "teod", "utfs", "ftdo", "shooting_star", "ety"],
                        1.0, 3.0,
                        "which is more than the whole of Part 1's first six "
                        "arcs put together"),
    is_extreme("datrow", "Chapter IX", "max",
               "is the longest entry in the game", scope="global"),
    median_between("datrow", "Chapter EX-2", 5, 119,
                   "*To None May God Pray* is the only entry in the arc "
                   "under two hours"),
    count_above("datrow", 120, 6,
                "*To None May God Pray* is the only entry in the arc "
                "under two hours"),
    median_between("datrow", "Chapter EX-3", 120, 600,
                   "The arc's closing interlude, "
                   "and the longer of its two EX chapters"),

    is_extreme("aric", "Chapter XI", "max",
               "A mass for atheists, and the largest entry in the arc"),
    median_between("aric", "Chapter X", 225, 275,
                   "Four of its entries sit within half an hour of each other"),
    median_between("aric", "Chapter XI", 225, 275,
                   "Four of its entries sit within half an hour of each other"),
    median_between("aric", "Chapter XII", 225, 275,
                   "Four of its entries sit within half an hour of each other"),
    median_between("aric", "Chapter XIII", 225, 275,
                   "Four of its entries sit within half an hour of each other"),
    median_between("aric", "Chapter EX-4", 5, 179,
                   "and the only entry here under three hours"),
    count_above("aric", 180, 4,
                "and the only entry here under three hours"),
]

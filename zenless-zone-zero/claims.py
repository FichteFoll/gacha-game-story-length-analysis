"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (count_above, is_extreme, largest_chapter,
                        median_between, none_above, rank_at_most,
                        sample_at_most)

CLAIMS = [
    none_above("s1", 240,
               "by a distance the cheapest to get through"),
    rank_at_most("s1", "Epilogue (A)", 2,
                 "The two epilogue halves stand apart from the rest",
                 scope="chapter"),
    rank_at_most("s1", "Epilogue (B)", 2,
                 "The two epilogue halves stand apart from the rest",
                 scope="chapter"),
    rank_at_most("s1", "Chapter 4", 3,
                 "everything before them sits between {shortest_len} "
                 "and {len_Chapter_4}",
                 scope="chapter"),

    sample_at_most("s1", "Chapter 2", 7,
                   "*A Call From the Hollow's Heart* in particular "
                   "rests on a handful of complete runs"),

    largest_chapter("s2", "Where the story changes scale"),
    count_above("s2", 180, 6,
                "{n_above_3h} of Season 2's {n_entries} entries "
                "run past three hours"),
    rank_at_most("s2", "Chapter 6", 1,
                 "the longest single entry in the game", scope="global"),
    is_extreme("s2", "Epilogue (B)", "min",
               "every other entry lands between {len_Epilogue_B} "
               "and {len_Interlude}"),
    rank_at_most("s2", "Interlude", 2,
                 "every other entry lands between {len_Epilogue_B} "
                 "and {len_Interlude}",
                 scope="chapter"),

    median_between("s3", "Chapter 1", 180, 360,
                   "Both were written at the Season 2 scale "
                   "rather than the Season 1 one"),
    median_between("s3", "Chapter 2", 180, 360,
                   "Both were written at the Season 2 scale "
                   "rather than the Season 1 one"),
]

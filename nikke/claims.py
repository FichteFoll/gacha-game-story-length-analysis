"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (count_above, is_extreme, largest_chapter,
                        median_between, none_above, rank_at_most,
                        sample_at_most, total_ratio_between)

CLAIMS = [
    # README.md
    is_extreme("v1", "Chapter 00", "min",
               "a runtime floor below the length of the prologue, "
               "which is the shortest chapter here", scope="global"),
    median_between("v1", "Chapter 00", 1, 20,
                   "The early chapters are minutes long "
                   "and the late ones are hours long"),

    # 01-fall-to-secret.md
    none_above("v1", 60, "no entry in it reaches the hour"),
    median_between("v1", "Chapter 03", 1, 20,
                   "Chapter 03 is a single errand"),
    is_extreme("v1", "Chapter 04", "max",
               "which Chapter 04 closes as the largest entry of the ten"),

    # 02-comrade-to-eden.md
    median_between("v2", "Chapter 10", 1, 30,
                   "Two chapters that could have come out of the opening volume"),
    median_between("v2", "Chapter 11", 1, 30,
                   "Two chapters that could have come out of the opening volume"),
    median_between("v2", "Chapter 12", 1, 60,
                   "Journey is the first entry in the game to pass the hour"),
    median_between("v2", "Chapter 13", 1, 60,
                   "Journey is the first entry in the game to pass the hour"),
    median_between("v2", "Chapter 14", 61, 600,
                   "Journey is the first entry in the game to pass the hour"),
    is_extreme("v2", "Chapter 18", "max",
               "Chapter 18 is the largest of the ten"),
    none_above("v2", 120, "Nothing here reaches two hours"),

    # 03-flame-dragon-to-rescue.md
    total_ratio_between("v3", ["v2"], 1.4, 2.2,
                        "The volume where the campaign stops being a series "
                        "of missions and becomes an expedition"),
    count_above("v3", 90, 5,
                "and half of its chapters pass the hour and a half"),
    is_extreme("v3", "Chapter 24", "max",
               "Banishment is the largest of them"),

    # 04-treasure-to-gene.md
    median_between("v4", "Chapter 34", 121, 600,
                   "with Inheritance and Gene running past that"),
    median_between("v4", "Chapter 39", 121, 600,
                   "with Inheritance and Gene running past that"),
    is_extreme("v4", "Chapter 34", "max",
               "Most of the volume sits between one hour and two"),
    sample_at_most("v4", "Chapter 32", 6,
                   "and Advance rests on a handful of them either way"),

    # 05-choice-to-reborn.md
    largest_chapter("v5",
                    "the largest volume in the report "
                    "despite being the smallest by count"),
    count_above("v5", 120, 6,
                "Of its nine chapters, six run past two hours"),
    rank_at_most("v5", "Chapter 47", 2,
                 "Outbreak and Reborn are the two shortest chapters "
                 "in the volume", scope="chapter", end="min"),
    rank_at_most("v5", "Chapter 48", 2,
                 "Outbreak and Reborn are the two shortest chapters "
                 "in the volume", scope="chapter", end="min"),
    median_between("v5", "Chapter 46", 150, 600,
                   "took far less time over each of the two"),
    median_between("v5", "Chapter 47", 1, 110,
                   "took far less time over each of the two"),
    median_between("v5", "Chapter 48", 1, 110,
                   "took far less time over each of the two"),
]

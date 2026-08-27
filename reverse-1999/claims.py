"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (is_extreme, largest_chapter, median_between,
                        rank_at_most, sample_at_most, total_ratio_between)

CLAIMS = [
    # 01-the-living-and-the-rest.md, the blurb
    largest_chapter("a1", "the largest in this report"),
    median_between("a1", "Prologue", 1, 59,
                   "The prologue is a tutorial that ends inside the hour"),
    is_extreme("a1", "Chapter 7", "max",
               "Chapter 7 is the longest entry in the game", scope="global"),

    # 01-the-living-and-the-rest.md, the pacing paragraph
    largest_chapter("a1", "the largest arc in the report"),
    median_between("a1", "Prologue", 1, 59,
                   "the only one whose entries run from under an hour "
                   "to over eight"),
    median_between("a1", "Chapter 7", 481, 900,
                   "the only one whose entries run from under an hour "
                   "to over eight"),
    median_between("a1", "Chapter 1", 100, 180,
                   "then two to three hours each for Chapters 1 to 3"),
    median_between("a1", "Chapter 2", 100, 180,
                   "then two to three hours each for Chapters 1 to 3"),
    median_between("a1", "Chapter 3", 100, 180,
                   "then two to three hours each for Chapters 1 to 3"),
    median_between("a1", "Chapter 4", 181, 299,
                   "then a step up to somewhere near four hours "
                   "at Chapters 4 and 5"),
    median_between("a1", "Chapter 5", 181, 299,
                   "then a step up to somewhere near four hours "
                   "at Chapters 4 and 5"),
    median_between("a1", "Chapter 6", 300, 480,
                   "and a second one at Chapter 6"),
    median_between("a1", "Inter Chapter - I", 1, 120,
                   "The two inter chapters interrupt the ramp, "
                   "and both stay under two hours"),
    median_between("a1", "Inter Chapter - II", 1, 120,
                   "The two inter chapters interrupt the ramp, "
                   "and both stay under two hours"),

    # 01-the-living-and-the-rest.md, the Chapter 4 and Chapter 6 notes.
    # "the first entry to pass three hours" and "to pass five hours" rest on
    # the two bounds above plus everything published before them staying under.
    median_between("a1", "Chapter 4", 181, 299,
                   "the first entry in the game to pass three hours"),
    median_between("a1", "Chapter 6", 300, 480,
                   "the first entry in the game to pass five hours"),

    # 02-the-journey-back.md
    is_extreme("a2", "Chapter 10", "max",
               "is the longest of the three"),
    median_between("a2", "Chapter 8", 240, 420,
                   "with nothing in the arc under four hours"),
    median_between("a2", "Chapter 9", 240, 420,
                   "Chapters 8 and 9 sit inside a single band"),
    median_between("a2", "Chapter 10", 300, 540,
                   "Chapter 10 is clear of both"),

    # 03-the-roots-of-the-tale.md
    median_between("a3", "Chapter 11", 300, 600,
                   "three entries, none of them under five hours"),
    median_between("a3", "Chapter 12", 300, 600,
                   "three entries, none of them under five hours"),
    median_between("a3", "Chapter 13", 300, 600,
                   "three entries, none of them under five hours"),
    sample_at_most("a3", "Chapter 13", 7,
                   "and the newest resting on the fewest uploads of any of them"),
    total_ratio_between("a3", ["a2"], 1.0, 2.0,
                        "which between them outweigh the arc before this one "
                        "on the same number of entries"),
    is_extreme("a3", "Chapter 12", "max",
               "Chapter 12 is the longest of the three"),
    rank_at_most("a3", "Chapter 12", 2,
                 "and the second longest entry in the game", scope="global"),
]

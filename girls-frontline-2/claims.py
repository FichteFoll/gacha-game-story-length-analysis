"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from assertions import (count_above, is_extreme, largest_chapter,
                        median_between, none_above, rank_at_most,
                        total_ratio_between)

CLAIMS = [
    # 01-double-pendulum-to-harmonic-cycle.md, the blurb
    median_between("v1", "Chapter 6", 180, 240,
                   "Chapter 1 is 1 h 39 min and Chapter 6 is more than twice that"),
    median_between("v1", "Chapter 1", 60, 119,
                   "Chapter 1 is 1 h 39 min and Chapter 6 is more than twice that"),

    # 01-double-pendulum-to-harmonic-cycle.md, the pacing paragraph
    is_extreme("v1", "Chapter 1", "min",
               "The launch chapters are the shortest in the game", scope="global"),
    median_between("v1", "Chapter 1", 60, 119,
                   "it is the only entry here under two hours"),
    median_between("v1", "Chapter 2", 120, 179,
                   "Chapters 2 and 3 sit together around two and a half"),
    median_between("v1", "Chapter 3", 120, 179,
                   "Chapters 2 and 3 sit together around two and a half"),
    median_between("v1", "Chapter 4", 180, 239,
                   "Chapters 4, 5 and 6 all pass three hours "
                   "without any of them reaching four"),
    median_between("v1", "Chapter 5", 180, 239,
                   "Chapters 4, 5 and 6 all pass three hours "
                   "without any of them reaching four"),
    median_between("v1", "Chapter 6", 180, 239,
                   "Chapters 4, 5 and 6 all pass three hours "
                   "without any of them reaching four"),

    # 02-sojourners-to-bitter-thorns.md, the blurb and the pacing paragraph
    is_extreme("v2", "Chapter 6.7", "min",
               "it is the shortest entry in this volume"),
    # "the first entry in the game to pass four hours" rests on this bound plus
    # everything published before it staying under, which the claims above and
    # the three below cover between them.
    median_between("v2", "Chapter 8", 240, 299,
                   "Chapter 8 being the first entry in the game "
                   "to pass four hours"),
    none_above("v1", 240,
               "Chapter 8 being the first entry in the game "
               "to pass four hours"),
    median_between("v2", "Chapter 6.5", 60, 175,
                   "Three of the four decimal chapters come in under both "
                   "whole-numbered ones"),
    median_between("v2", "Chapter 6.7", 60, 175,
                   "Three of the four decimal chapters come in under both "
                   "whole-numbered ones"),
    median_between("v2", "Chapter 7", 176, 239,
                   "Three of the four decimal chapters come in under both "
                   "whole-numbered ones"),
    median_between("v2", "Chapter 8.3", 100, 175,
                   "it has no more stages than Chapter 8.3 "
                   "and is more than twice as long as it"),
    median_between("v2", "Chapter 8.7", 320, 480,
                   "it has no more stages than Chapter 8.3 "
                   "and is more than twice as long as it"),

    # 03-aphelion-to-intertwined-assault.md
    is_extreme("v3", "Chapter 9", "min",
               "only the first of them is short"),
    is_extreme("v3", "Chapter 10", "max",
               "Chapter 10 is close to twice it"),
    median_between("v3", "Chapter 9", 120, 179,
                   "Chapter 10 is close to twice it"),
    total_ratio_between("v3", ["v1"], 1.05, 2.0,
                        "are the reason this volume outweighs the launch run "
                        "on one entry fewer"),
    median_between("v3", "Chapter 12.5", 180, 247,
                   "Chapter 12.5 closes the volume out below both of the "
                   "chapters it sits between"),
    median_between("v3", "Chapter 11", 248, 330,
                   "Chapter 12.5 closes the volume out below both of the "
                   "chapters it sits between"),
    median_between("v3", "Chapter 12", 248, 360,
                   "Chapter 12.5 closes the volume out below both of the "
                   "chapters it sits between"),

    # 04-corposant-to-antiparallel.md
    largest_chapter("v4",
                    "by a wide margin the largest volume in the report"),
    total_ratio_between("v4", ["v3"], 1.2, 3.0,
                        "by a wide margin the largest volume in the report"),
    is_extreme("v4", "Chapter 15", "max",
               "it holds the largest chapters in the game", scope="global"),
    rank_at_most("v4", "Chapter 16", 2,
                 "it holds the largest chapters in the game", scope="global"),
    count_above("v4", 360, 3,
                "then Chapters 14, 15 and 16 all pass six hours, "
                "three consecutive entries longer than anything published "
                "before them"),
    none_above("v3", 360,
               "three consecutive entries longer than anything published "
               "before them"),
    median_between("v4", "Chapter 13", 210, 300,
                   "Chapter 17 then drops back to about where Chapter 13 "
                   "started, and those two are the only entries here under "
                   "six hours"),
    median_between("v4", "Chapter 17", 210, 300,
                   "Chapter 17 then drops back to about where Chapter 13 "
                   "started, and those two are the only entries here under "
                   "six hours"),

    # 05-dawnforger-to-needy-catgirl-overload.md
    count_above("v5", 240, 3,
                "every entry here is over four hours"),
    is_extreme("v5", "Chapter 19", "max",
               "Chapter 19 is the longest of the three"),
    is_extreme("v5", "Chapter 20", "min",
               "Even Chapter 20, the volume's floor, sits above almost "
               "everything in the first two volumes"),
    none_above("v1", 240,
               "Even Chapter 20, the volume's floor, sits above almost "
               "everything in the first two volumes"),
    median_between("v5", "Chapter 20", 240, 330,
                   "something close to the running time of an ordinary "
                   "chapter"),
]

"""What this report's prose still asserts about the data, in words.

The vocabulary these are written in, and the check that runs them,
live in the skill's `assertions.py`; only the claims themselves are per report.
"""
from analyze import IQR_SAMPLES
from assertions import (Claim, count_above, is_extreme, largest_chapter,
                        median_between, none_above, rank_at_most)


def sample_at_least(chapter, act_label, n, quote):
    """For prose that calls a pool large enough to be graded on its spread,
    the counterpart of sample_at_most."""
    def check(index):
        act = next(a for a in index[chapter] if a["act_label"] == act_label)
        got = act["stats"]["n"]
        return got >= n, f"{act_label} rests on {got} uploads, expected {n} or more"
    return Claim(quote, f"{chapter} {act_label}: at least {n} uploads", check)


CLAIMS = [
    none_above("prologue", 60,
               "The shortest chapter in the game by a wide margin, "
               "and the only one that is over in under an hour"),
    is_extreme("prologue", "Prologue II", "min",
               "which is why it lands at {len_Prologue_II} "
               "against the first half's {len_Prologue_I}"),

    median_between("ch1", "Act VI", 60, 120,
                   "The six launch acts and the Interlude are short work, "
                   "the largest of them Act VI at {len_Act_VI}"),
    median_between("ch1", "Act I", 20, 120,
                   "The six launch acts and the Interlude are short work"),
    median_between("ch1", "Interlude", 5, 120,
                   "The six launch acts and the Interlude are short work"),
    rank_at_most("ch1", "Act VII", 1,
                 "and Act VII is the largest single thing in it",
                 scope="chapter"),
    rank_at_most("ch1", "Act VIII", 2,
                 "Those two are the longest entries in the chapter",
                 scope="chapter"),

    largest_chapter("ch2", "By far the largest chapter here"),
    count_above("ch2", 120, 9,
                "nine of its seventeen entries run past two hours"),
    count_above("ch2", 180, 3, "and three past three"),
    median_between("ch2", "Prologue", 5, 75,
                   "the prologue, the two afterstory segues and "
                   "*Rust, Sword and the Sun* all sit under an hour "
                   "and a quarter"),
    median_between("ch2", "Segue - I", 5, 75,
                   "the prologue, the two afterstory segues and "
                   "*Rust, Sword and the Sun* all sit under an hour "
                   "and a quarter"),
    median_between("ch2", "Segue - II", 5, 75,
                   "the prologue, the two afterstory segues and "
                   "*Rust, Sword and the Sun* all sit under an hour "
                   "and a quarter"),
    median_between("ch2", "Segue - III", 5, 75,
                   "the prologue, the two afterstory segues and "
                   "*Rust, Sword and the Sun* all sit under an hour "
                   "and a quarter"),
    is_extreme("ch2", "Act XI", "max",
               "Act XI is the chapter's set piece and the longest act "
               "in Rinascita at {len_Act_XI}"),

    is_extreme("ch3", "Segue - III", "min",
               "they run from {len_Segue_III}, the shortest entry in the game",
               scope="global"),
    is_extreme("ch3", "Act III", "max",
               "with Act III as the chapter's centrepiece"),
    median_between("ch3", "Segue - VII", 90, 180,
                   "up to {len_Segue_VII}, which is longer than most "
                   "chapters' acts"),

    is_extreme("ch4", "Act III", "max",
               "Act III is the longest single entry in the game at "
               "{len_Act_III}", scope="global"),
    median_between("ch4", "Segue - I", 5, 45,
                   "the two segues together add under {len_Segue_I} plus "
                   "{len_Segue_II}"),
    median_between("ch4", "Segue - II", 5, 45,
                   "the two segues together add under {len_Segue_I} plus "
                   "{len_Segue_II}"),
    sample_at_least("ch4", "Segue - II", IQR_SAMPLES,
                    "the closing segue, thin while it was new, has since "
                    "gathered enough uploads to be rated on its spread"),
]

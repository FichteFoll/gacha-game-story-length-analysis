"""Quantities derived from analysis.json.

The authored prose in chapter_text.py states no number of its own: it carries
placeholders that are filled from here at render time, so a re-harvest that
moves a median cannot leave a stale figure behind in a sentence.
"""
import re

WORDS = ["zero", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "eleven", "twelve"]


def word(n):
    """Spelled-out count, because these numbers appear mid-sentence in prose."""
    return WORDS[n] if n < len(WORDS) else str(n)


def hm(minutes):
    if minutes is None:
        return "n/a"
    h, m = divmod(int(round(minutes)), 60)
    return f"{h} h {m:02d} min" if h else f"{m} min"


def median_of(act):
    return act["stats"]["median"] or 0


def count_above(acts, minutes):
    return sum(1 for a in acts if median_of(a) > minutes)


def count_between(acts, lo, hi):
    return sum(1 for a in acts if lo <= median_of(a) <= hi)


def chapter_total(acts):
    return sum(median_of(a) for a in acts)


def act_key(act_label):
    """`Act IV - Prelude` -> `Act_IV_Prelude`, usable as a format placeholder."""
    return re.sub(r"\W+", "_", act_label).strip("_")


EXTREME_DEPTH = 3      # how many entries at each end get a superlative sentence


def act_name(act):
    """`Chapter IV, Act V`, for naming an act from a different chapter."""
    return f"{act['chapter_title'].split(':')[0]}, {act['act_label']}"


def rank(act, acts, longest=True):
    """1-based rank by estimate, sharing a rank between ties."""
    better = (lambda o: median_of(o) > median_of(act)) if longest \
        else (lambda o: median_of(o) < median_of(act))
    return 1 + sum(1 for o in acts if better(o))


def superlatives(acts):
    """Generated superlative sentences, keyed "<chapter id>|<act label>".

    Derived rather than authored, so the phrase can only turn up on an act that
    currently holds the position, and ties are stated as ties.
    """
    out = {}
    for act in acts:
        high, low = rank(act, acts), rank(act, acts, longest=False)
        tied = [o for o in acts
                if o is not act and median_of(o) == median_of(act)]
        if high == 1:
            others = " and ".join(act_name(o) for o in tied)
            sentence = (f"Tied with {others} for the longest act in the game."
                        if tied else "The single longest act in the game.")
        elif high <= EXTREME_DEPTH:
            sentence = f"One of the {word(EXTREME_DEPTH)} longest acts in the game."
        elif low == 1 and not tied:
            sentence = "The shortest entry in the questline."
        elif low <= EXTREME_DEPTH:
            sentence = (f"One of the {word(EXTREME_DEPTH)} shortest entries "
                        f"in the questline.")
        else:
            continue
        out[f"{act['chapter_id']}|{act['act_label']}"] = sentence
    return out


def chapter_facts(acts, quest_parts=None):
    """The values the authored prose may interpolate, keyed by placeholder name."""
    quest_parts = quest_parts or {}
    ranked = sorted(acts, key=median_of)
    numbered = [a for a in acts if a["act_label"].startswith("Act ")]
    facts = {
        "n_entries": word(len(acts)),
        "n_acts": word(len(numbered)),
        "n_above_2h": word(count_above(acts, 120)),
        "n_above_3h": word(count_above(acts, 180)),
        "n_under_1h": word(sum(1 for a in acts if median_of(a) < 60)),
        "total": hm(chapter_total(acts)),
        "longest_label": ranked[-1]["act_label"],
        "longest_title": ranked[-1]["act_title"],
        "longest_len": hm(median_of(ranked[-1])),
        "shortest_label": ranked[0]["act_label"],
        "shortest_title": ranked[0]["act_title"],
        "shortest_len": hm(median_of(ranked[0])),
    }
    if numbered:
        by_length = sorted(numbered, key=median_of)
        facts["acts_low"] = hm(median_of(by_length[0]))
        facts["acts_high"] = hm(median_of(by_length[-1]))
    for act in acts:
        key = act_key(act["act_label"])
        facts[f"len_{key}"] = hm(median_of(act))
        parts = quest_parts.get(f"{act['chapter_id']}|{act['act_label']}")
        if parts:
            facts[f"parts_{key}"] = word(len(parts))
    return facts

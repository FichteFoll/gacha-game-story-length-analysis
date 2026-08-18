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

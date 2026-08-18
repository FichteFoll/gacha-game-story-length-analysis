"""The vocabulary a report's claims.py writes its assertions in.

Figures the prose interpolates cannot go stale. Adjectives can: "marathon acts",
"the chapter centrepiece", "by far the largest chapter" are claims about the data
that survive any re-harvest unchallenged. Each one is written down in the report's
own `claims.py` next to the sentence it guards, and gen_docs.py evaluates the lot
before it writes a single file.

Vocabulary:
    count_above(chapter, minutes, n)      at least n entries longer than `minutes`
    none_above(chapter, minutes)          no entry is longer than `minutes`
    median_between(chapter, act, lo, hi)  this act's estimate is within [lo, hi]
    rank_at_most(chapter, act, k, scope)  this act is among the k longest
    is_extreme(chapter, act, end, scope)  this act is the longest/shortest
    total_ratio_between(chapter, others, lo, hi)
                                          chapter total over the others' combined
    largest_chapter(chapter)              no chapter totals more
"""
from collections import namedtuple

from facts import chapter_total, count_above as _count_above, median_of

# `quote` is the sentence the claim guards, so a failure names the prose to fix.
Claim = namedtuple("Claim", "quote describe check")


def _act(index, chapter, act_label):
    for act in index[chapter]:
        if act["act_label"] == act_label:
            return act
    raise KeyError(f"{chapter} has no {act_label}")


def _scoped(index, chapter, scope):
    if scope == "chapter":
        return index[chapter]
    return [a for acts in index.values() for a in acts]


def count_above(chapter, minutes, n, quote):
    """At least n, not exactly n: the exact count is interpolated into the prose,
    so only the floor the surrounding wording relies on is worth asserting."""
    def check(index):
        got = _count_above(index[chapter], minutes)
        return got >= n, f"{got} entries above {minutes} min, expected {n} or more"
    return Claim(quote, f"{chapter}: {n}+ entries above {minutes} min", check)


def none_above(chapter, minutes, quote):
    """The companion to count_above, for prose that says a chapter stays under
    something ("nothing before Penacony passes three hours")."""
    def check(index):
        got = _count_above(index[chapter], minutes)
        return got == 0, f"{got} entries above {minutes} min, expected none"
    return Claim(quote, f"{chapter}: nothing above {minutes} min", check)


def median_between(chapter, act_label, lo, hi, quote):
    def check(index):
        got = median_of(_act(index, chapter, act_label))
        return lo <= got <= hi, f"{act_label} is {got} min, expected {lo}-{hi}"
    return Claim(quote, f"{chapter} {act_label}: {lo}-{hi} min", check)


def rank_at_most(chapter, act_label, k, quote, scope="global"):
    def check(index):
        act = _act(index, chapter, act_label)
        pool = _scoped(index, chapter, scope)
        got = 1 + sum(1 for o in pool if median_of(o) > median_of(act))
        return got <= k, f"{act_label} ranks {got} of {len(pool)}, wanted top {k}"
    return Claim(quote, f"{chapter} {act_label}: top {k} {scope}", check)


def is_extreme(chapter, act_label, end, quote, scope="chapter"):
    def check(index):
        act = _act(index, chapter, act_label)
        pool = _scoped(index, chapter, scope)
        want = max if end == "max" else min
        holder = want(pool, key=median_of)
        return median_of(holder) == median_of(act), \
            f"{end} of {scope} is {holder['act_label']} ({median_of(holder)} min)"
    return Claim(quote, f"{chapter} {act_label}: {end} of {scope}", check)


def total_ratio_between(chapter, others, lo, hi, quote):
    def check(index):
        mine = chapter_total(index[chapter])
        theirs = sum(chapter_total(index[o]) for o in others)
        ratio = mine / theirs
        return lo <= ratio <= hi, \
            f"{chapter} is {ratio:.2f} times {'+'.join(others)}, expected {lo}-{hi}"
    return Claim(quote, f"{chapter}: {lo}-{hi} times {'+'.join(others)}", check)


def largest_chapter(chapter, quote):
    def check(index):
        biggest = max(index, key=lambda c: chapter_total(index[c]))
        return biggest == chapter, f"{biggest} is the largest chapter"
    return Claim(quote, f"{chapter}: largest chapter", check)


def failures(analysis, claims):
    """Every claim that no longer holds, as human-readable lines."""
    index = {}
    for act in analysis:
        index.setdefault(act["chapter_id"], []).append(act)
    out = []
    for claim in claims:
        ok, detail = claim.check(index)
        if not ok:
            out.append(f"{claim.describe}\n    but {detail}\n    guards: "
                       f"\"{claim.quote}\"")
    return out

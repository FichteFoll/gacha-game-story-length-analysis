#!/usr/bin/env python3
"""Screen harvested video candidates per act and compute duration statistics.

Usage: analyze.py <workdir>

Reads  <workdir>/acts.tsv            act list (see harvest.sh)
       <workdir>/evidence/*.tsv      harvested candidates
       <workdir>/chapter_keys.json   optional {chapter_id: [identifying words]},
                                     used by the act-number fallback match
       <workdir>/compilations.txt    optional extra compilation regexes, one per
                                     line, e.g. "full sumeru archon quest"
Writes <workdir>/analysis.json       accepted and rejected candidates plus stats
and prints a one-line-per-act summary for eyeballing.

A candidate survives only if its title plausibly names this exact act and it is
not a cutscene reel, a stream, a multi-act compilation or a truncated upload.
"""
import json
import pathlib
import re
import statistics
import sys

# Uploads that are not hands-on playthrough footage. Streams and let's-plays are
# excluded because their idle chatter inflates runtime well past the act length.
REJECT = re.compile(
    r"cutscene|all cinematic|cinematics|movie|film|dialogue|voice ?lines|"
    r"explained|reaction|review|\bguide\b|tips|how to|unlock|puzzle|"
    r"locations?\b|recap|summar|trailer|teaser|\bost\b|soundtrack|music|"
    r"theory|lore|tier list|\bamv\b|edit\b|montage|"
    r"\blive\b|livestream|\bstream\b|let'?s play|lets play|\U0001F534",
    re.I,
)
# Genuine multi-act uploads. Note that "full archon quest" is deliberately NOT
# listed: it is the usual phrasing for a complete single act, not a compilation.
COMPILATION = re.compile(
    r"all acts|full chapter|entire chapter|complete chapter|whole chapter|"
    r"acts? \d+ ?(&|and|\+|,) ?\d+|acts? [ivx]+ ?(&|and|\+|,) ?[ivx]+|"
    r"acts? \d+ ?- ?\d+|marathon",
    re.I,
)

STOPWORDS = {"the", "a", "an", "and", "of", "to", "in", "on", "for", "that",
             "under", "amidst", "without", "over", "with", "from"}

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
         "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12}

TITLE_MATCH_RATIO = 0.6      # share of act-title words a video title must carry
SHORT_OUTLIER = 0.5          # fraction of the median below which uploads drop
LONG_OUTLIER = 1.8           # multiple of the median above which uploads drop


def compilation_re(workdir):
    """COMPILATION plus any franchise-specific phrasings supplied by the caller."""
    extra_file = workdir / "compilations.txt"
    if not extra_file.exists():
        return COMPILATION
    extra = [l.strip() for l in extra_file.read_text().splitlines() if l.strip()]
    if not extra:
        return COMPILATION
    return re.compile(COMPILATION.pattern + "|" + "|".join(extra), re.I)


def title_words(text):
    return [w for w in re.findall(r"[a-z']+", text.lower())
            if w not in STOPWORDS and len(w) > 2]


def matches_act_title(video_title, act_title):
    want = title_words(act_title)
    if not want:
        return False
    have = set(title_words(video_title))
    return sum(1 for w in want if w in have) / len(want) >= TITLE_MATCH_RATIO


def act_number(act_label):
    return ROMAN.get(act_label.replace("Act", "").split("-")[0].strip().upper())


def matches_act_number(video_title, act, chapter_keys):
    """Fallback: the title names this act's number *and* this act's chapter.

    Both halves are required. Without the chapter check, "Snezhnaya Act 1" would
    be accepted as evidence for a different chapter's Act I.
    """
    num = act_number(act["act_label"])
    keys = chapter_keys.get(act["chapter_id"], [])
    if num is None or not keys:
        return False
    low = video_title.lower()
    roman = next(k for k, v in ROMAN.items() if v == num).lower()
    if not re.search(rf"\bact:? +(?:{num}|{roman})\b", low):
        return False
    return any(k.lower() in low for k in keys)


def load_acts(workdir):
    acts = []
    for line in (workdir / "acts.tsv").read_text().splitlines():
        if not line.strip():
            continue
        chap_id, chap_title, act_label, act_title = line.split("\t")
        acts.append(dict(
            chapter_id=chap_id, chapter_title=chap_title, act_label=act_label,
            act_title=act_title,
            slug=re.sub(r"[^A-Za-z0-9_-]", "_", f"{chap_id}_{act_label}")))
    return acts


def candidates_for(act, workdir, chapter_keys, compilation):
    rows = []
    path = workdir / "evidence" / f"{act['slug']}.tsv"
    if not path.exists():
        return rows
    for line in path.read_text().splitlines():
        f = line.split("\t")
        if len(f) < 4 or not f[0].isdigit():
            continue
        title = f[1]
        reasons = []
        if REJECT.search(title):
            reasons.append("not-a-playthrough")
        if compilation.search(title):
            reasons.append("multi-act")
        if not (matches_act_title(title, act["act_title"])
                or matches_act_number(title, act, chapter_keys)):
            reasons.append("act-mismatch")
        rows.append(dict(seconds=int(f[0]), title=title, uploader=f[2], url=f[3],
                         views=f[4] if len(f) > 4 else "NA", rejected=reasons))
    return rows


def trim_outliers(kept):
    if len(kept) < 3:
        return kept
    med = statistics.median(r["seconds"] for r in kept)
    for r in kept:
        if r["seconds"] < SHORT_OUTLIER * med:
            r["rejected"] = ["short-outlier"]
        elif r["seconds"] > LONG_OUTLIER * med:
            r["rejected"] = ["long-outlier"]
    return [r for r in kept if not r["rejected"]]


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    workdir = pathlib.Path(argv[1])
    keys_file = workdir / "chapter_keys.json"
    chapter_keys = json.loads(keys_file.read_text()) if keys_file.exists() else {}
    compilation = compilation_re(workdir)

    out = []
    for act in load_acts(workdir):
        rows = candidates_for(act, workdir, chapter_keys, compilation)
        kept = trim_outliers([r for r in rows if not r["rejected"]])
        kept.sort(key=lambda r: r["seconds"])
        secs = [r["seconds"] for r in kept]
        act.update(candidates=rows, kept=kept, stats=dict(
            n=len(secs),
            median=round(statistics.median(secs) / 60) if secs else None,
            low=round(min(secs) / 60) if secs else None,
            high=round(max(secs) / 60) if secs else None))
        out.append(act)

    (workdir / "analysis.json").write_text(json.dumps(out, indent=1))
    for act in out:
        s = act["stats"]
        flag = "  <-- thin, top up or widen the queries" if s["n"] < 6 else ""
        print(f"{act['chapter_id']:>10} {act['act_label']:<16} n={s['n']:<3}"
              f"med={s['median']} range={s['low']}-{s['high']}"
              f"  {act['act_title'][:40]}{flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

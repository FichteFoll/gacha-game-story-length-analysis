#!/usr/bin/env python3
"""Screen harvested video candidates per act and compute duration statistics.

Usage: analyze.py <workdir> [--compare <baseline>]

Reads  <workdir>/acts.tsv            act list (see harvest.sh)
       <workdir>/evidence/*.tsv      harvested candidates
       <workdir>/chapter_keys.json   optional {chapter_id: [identifying words]},
                                     used by the act-number fallback match
       <workdir>/act_keys.json       optional {chapter_id|act_label: [regex]},
                                     what a title must carry to be about this act
                                     rather than the one it shares its name with
       <workdir>/versions.json       optional, act title -> release version
       <workdir>/version_index.json  optional, version -> {number, date};
                                     both extend the chapter keys with the
                                     version branding uploaders title by
       <workdir>/compilations.txt    optional extra compilation regexes, one per
                                     line, e.g. "full sumeru archon quest"
       <workdir>/partials.txt        optional regexes for uploads covering less
                                     than one act, one per line, e.g. "part 3",
                                     plus the line "<quest part>" for titles
                                     naming one of the act's own quest parts;
                                     the mirror image of compilations.txt
       <workdir>/enriched.tsv        optional second-pass metadata (enrich.sh):
                                     exact duration, upload date, exact view
                                     count and the uploader's chapter markers
       <workdir>/quest_parts.json    optional {chapter_id|act_label: [part, ...]},
                                     what the chapter markers are matched against
       <baseline>                    optional earlier analysis.json, or the
                                     {chapter_id|act_label: minutes} map derived
                                     from one; each act's median is compared
                                     against it and the drift is recorded
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
# What an upload calls the whole of a chapter. Kept short on purpose, and
# terminated by a word boundary: "arc" without one turns every "Full Archon
# Quest" (the normal phrasing for one complete act) into a compilation.
# Anything else a game's uploaders say belongs in <workdir>/compilations.txt.
CONTAINER = r"chapter|episode|arc"
# The partials.txt line that stands for "names one of this act's quest parts".
QUEST_PART = "<quest part>"

STOPWORDS = {"the", "a", "an", "and", "of", "to", "in", "on", "for", "that",
             "under", "amidst", "without", "over", "with", "from"}

ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7,
         "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12}


def numerals(number):
    """`1|i`: how a title may write this act's number, roman numeral where there
    is one. A game that opens on a Chapter 0 has no roman half."""
    roman = next((k for k, v in ROMAN.items() if v == number), None)
    return "|".join(filter(None, [str(number), roman and roman.lower()]))

TITLE_MATCH_RATIO = 0.6      # share of act-title words a video title must carry
SHORT_OUTLIER = 0.5          # fraction of the median below which uploads drop
PARTIAL_READMIT = 0.75       # ... and below which a "part 3" upload stays out
LONG_OUTLIER = 1.8           # multiple of the median above which uploads drop
SPAN_COVERAGE = 0.6          # markers must cover this much of a single-act upload
SPAN_MINIMUM = 900           # ... and this many seconds, before a span is used
PART_SAMPLES = 3             # uploads needed before a quest part's time is kept
IQR_SAMPLES = 8              # ... and before the middle half beats the extremes
UNSTABLE_DRIFT = 0.10        # median move against the baseline that means "soft"
BUNDLE_TOLERANCE = 0.15      # how far a bundle's runtime may sit from the sum


def unit_pattern(acts):
    """`acts?`: how this game's uploads name one act, from the act labels.

    Genshin numbers its acts "Act I" and Wuthering Waves "Act 1", but a game
    that says "Episode 2" would otherwise have every bundle and compilation of
    its episodes read as a single-act upload.
    """
    units = {act_unit(a["act_label"]).lower() for a in acts
             if act_number(a["act_label"])}
    return "|".join(sorted(f"{u}s?" for u in units)) or "acts?"


def container_pattern(acts):
    """The words for the whole of a chapter, minus the one this game numbers acts
    with: a game whose act *is* a chapter would otherwise read every "Full
    Chapter 3" as a compilation of the chapters it is one of.
    """
    unit = {act_unit(a["act_label"]).lower() for a in acts}
    return "|".join(w for w in CONTAINER.split("|") if w not in unit) or CONTAINER


def compilation_re(workdir, acts):
    """Genuine multi-act uploads, in this game's wording.

    Note that "full archon quest" is deliberately not matched: "full <questline>"
    is the usual phrasing for a complete single act, not for a compilation.
    """
    units = unit_pattern(acts)
    patterns = [
        rf"all {units}",
        rf"(?:full|entire|complete|whole) (?:{container_pattern(acts)})s?\b",
        rf"(?:{units}) \d+ ?(?:&|and|\+|,) ?\d+",
        rf"(?:{units}) [ivx]+ ?(?:&|and|\+|,) ?[ivx]+",
        rf"(?:{units}) \d+ ?- ?\d+",
        r"marathon",
    ]
    return re.compile("|".join(patterns + extra_patterns(workdir,
                                                         "compilations.txt")),
                      re.I)


def extra_patterns(workdir, name):
    """The per-report regexes in <workdir>/<name>, one per line."""
    path = workdir / name
    return [l.strip() for l in path.read_text().splitlines() if l.strip()] \
        if path.exists() else []


def partial_test(workdir):
    """`(title, parts) -> covers less than one act`, the compilation's mirror.

    Where a game's acts run for hours, many uploaders split one act across
    several uploads, and such an upload's runtime measures the split rather than
    the act. Left to the outlier trim they are not merely dropped: enough of them
    drag the median they are trimmed against down with them, until the complete
    uploads are the ones that look like the outliers.

    Both ways of saying "part of an act" are per report. The literal patterns are
    the lines of partials.txt; the line "<quest part>" additionally reads a title
    naming one of the act's own quest parts as a split, which is opt-in because a
    game whose uploaders title a complete act after its closing quest part would
    otherwise lose every upload it has. Returns None where the report says
    nothing, which is every game that has no partials.txt.
    """
    patterns = extra_patterns(workdir, "partials.txt")
    by_quest_part = QUEST_PART in patterns
    literal = [p for p in patterns if p != QUEST_PART]
    regex = re.compile("|".join(literal), re.I) if literal else None
    if not (regex or by_quest_part):
        return None
    return lambda title, parts: bool(regex and regex.search(title)) \
        or (by_quest_part and part_named(title, parts) is not None)


def bundle_re(acts):
    """"Acts 9 & 10", "Act V and VI": a free second opinion on two acts at once."""
    return re.compile(rf"(?:{unit_pattern(acts)}) +([ivx]+|\d+) *"
                      rf"(?:&|and|\+|,) *([ivx]+|\d+)\b", re.I)


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
    """`Act IV - Prelude` -> 4, in roman or arabic, `Interlude` -> None."""
    numbered = act_label.split("-")[0].split()
    if not numbered:
        return None
    last = numbered[-1]
    return int(last) if last.isdigit() else ROMAN.get(last.upper())


def act_unit(act_label):
    """`Act IV` -> `Act`: the word this game numbers its acts with."""
    words = act_label.split("-")[0].split()
    return words[0] if len(words) > 1 else "act"


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
    unit = act_unit(act["act_label"]).lower()
    if not re.search(rf"\b{unit}:? +(?:{numerals(num)})\b", low):
        return False
    return any(k.lower() in low for k in keys)


def act_key_test(workdir):
    """`(act, title) -> the title may be about this act`, from act_keys.json.

    Two acts sometimes carry the same name, because the game shipped one act's
    halves a version apart and the wiki tells them apart by a suffix the title
    matching cannot see ("... (A)" against "... (B)"). An act that declares
    distinguishing marks accepts only titles carrying one of them, which also
    keeps an upload that names neither half out of both pools.
    """
    keys = {k: re.compile("|".join(v), re.I)
            for k, v in load_json(workdir, "act_keys.json").items()}

    def is_this_act(act, title):
        marks = keys.get(f"{act['chapter_id']}|{act['act_label']}")
        return marks is None or bool(marks.search(title))

    return is_this_act


def version_keys(workdir, acts):
    """Per chapter, the version names and patch numbers its acts shipped in.

    Recent uploads are branded by patch rather than by chapter ("Genshin Impact
    6.6 Act 10"), so the version is the only chapter identifier in the title.
    Derived per chapter rather than hand-listed, because a brand attached to the
    wrong chapter would let one chapter's uploads count as another's evidence.
    """
    versions = load_json(workdir, "versions.json")
    index = load_json(workdir, "version_index.json")
    keys = {}
    for act in acts:
        name = versions.get(act["act_title"])
        if not name:
            continue
        brands = keys.setdefault(act["chapter_id"], set())
        brands.add(name)
        number = index.get(name, {}).get("number")
        if number:
            brands.add(number)
    return {chapter: sorted(brands) for chapter, brands in keys.items()}


def load_json(workdir, name):
    path = workdir / name
    return json.loads(path.read_text()) if path.exists() else {}


def load_enriched(workdir):
    """URL -> exact metadata from the full extraction pass, where it exists.

    The harvest runs with --flat-playlist, whose view counts are rounded and
    which reports no upload date at all. YouTube throttles full extraction, so
    this covers whatever enrich.sh has managed to fetch so far and the rest
    falls back to the harvested figures.
    """
    path = workdir / "enriched.tsv"
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text().splitlines():
        f = line.split("\t")
        if len(f) < 5:
            continue
        duration, date, views, chapters = (maybe_json(x) for x in f[1:5])
        out[f[0]] = dict(seconds=duration, upload_date=date, views=views,
                         chapters=chapters or [])
    return out


def maybe_json(field):
    """yt-dlp prints a bare NA for a field the video does not have."""
    return None if field == "NA" else json.loads(field)


def names_act_number(text, act):
    num = act_number(act["act_label"])
    if num is None:
        return False
    unit = act_unit(act["act_label"]).lower()
    return bool(re.search(rf"\b{unit}:? *(?:{numerals(num)})\b", text.lower()))


def part_named(marker_title, parts):
    """The quest part this marker is named after, if any."""
    return next((p for p in parts if matches_act_title(marker_title, p)), None)


def act_markers(act, chapters, parts):
    """The markers of one upload that belong to this act, as (marker, part).

    Walkthrough uploads very often name their chapter markers after the quest
    parts, which is what makes an act locatable inside a longer video: it is how
    an "Acts 9 & 10" compilation becomes evidence for each act separately, and
    how the uploader's pre-roll and detours stay out of the measurement.
    """
    out = []
    for marker in chapters:
        title = marker.get("title") or ""
        part = part_named(title, parts)
        if part or matches_act_title(title, act["act_title"]) \
                or names_act_number(title, act):
            out.append((marker, part))
    return out


def marker_seconds(marker):
    return max(0, (marker.get("end_time") or 0) - (marker.get("start_time") or 0))


def act_span(act, chapters, parts, duration, bundled):
    """Measured length of this act inside an upload, or None if not locatable.

    A span that covers only a fraction of a single-act upload means the markers
    were not the quest parts after all, and trusting it would under-measure the
    act; for an upload that genuinely covers several acts there is no such floor.
    """
    matched = act_markers(act, chapters, parts)
    span = sum(marker_seconds(m) for m, _ in matched)
    if not matched or span < SPAN_MINIMUM:
        return None
    if not bundled and duration and span < SPAN_COVERAGE * duration:
        return None
    return span


def load_acts(workdir):
    """The act list, with the wiki page each act is documented on.

    The page is the optional fifth column, because an act's display title is
    often not a page title: a game that ships one act in two halves is written
    up under one of them, and a chapter page is named `Chapter VII` rather than
    `Chapter VII: Everwinter Without Mercy`.
    """
    acts = []
    for line in (workdir / "acts.tsv").read_text().splitlines():
        if not line.strip():
            continue
        chap_id, chap_title, act_label, act_title, *rest = line.split("\t")
        acts.append(dict(
            chapter_id=chap_id, chapter_title=chap_title, act_label=act_label,
            act_title=act_title, wiki_page=rest[0] if rest else act_title,
            slug=re.sub(r"[^A-Za-z0-9_-]", "_", f"{chap_id}_{act_label}")))
    return acts


def candidates_for(act, workdir, chapter_keys, act_keys, compilation, partial,
                   enriched, parts):
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
        if partial and partial(title, parts):
            reasons.append("part-of-an-act")
        if not act_keys(act, title) \
                or not (matches_act_title(title, act["act_title"])
                        or matches_act_number(title, act, chapter_keys)):
            reasons.append("act-mismatch")
        row = dict(seconds=int(f[0]), title=title, uploader=f[2], url=f[3],
                   views=f[4] if len(f) > 4 else "NA", rejected=reasons)
        exact = enriched.get(f[3])
        if exact:
            row.update(seconds=exact["seconds"] or row["seconds"],
                       views=exact["views"], upload_date=exact["upload_date"])
            measure_from_markers(row, act, exact["chapters"], parts)
        rows.append(row)
    return rows


def measure_from_markers(row, act, chapters, parts):
    """Replace an upload's runtime with the part of it that is this act.

    An upload rejected only for covering several acts, or for a title that does
    not name this one, is readmitted when its markers say where this act runs:
    the measurement no longer depends on the title being right about the scope.
    """
    bundled = bool(row["rejected"])
    span = act_span(act, chapters, parts, row["seconds"], bundled)
    if span is None:
        return
    row["runtime"] = row["seconds"]
    row["seconds"] = span
    row["measured"] = "chapter-markers"
    row["parts"] = {part: marker_seconds(marker)
                    for marker, part in act_markers(act, chapters, parts) if part}
    row["rejected"] = [r for r in row["rejected"]
                       if r not in ("multi-act", "act-mismatch")]


def part_medians(kept, parts):
    """Median minutes per quest part, over the uploads that timed it."""
    timings = {}
    for row in kept:
        for part, seconds in row.get("parts", {}).items():
            timings.setdefault(part, []).append(seconds)
    return {part: round(statistics.median(timings[part]) / 60)
            for part in parts
            if len(timings.get(part, [])) >= PART_SAMPLES}


def spread(secs):
    """Full spread, plus the interquartile bounds once the sample carries them.

    One padded upload widens a min-max range that is otherwise tight, and says
    more about that uploader than about the act. From eight uploads on there is
    enough of a distribution for the middle half to describe it better.
    """
    if not secs:
        return dict(low=None, high=None, q1=None, q3=None)
    out = dict(low=round(min(secs) / 60), high=round(max(secs) / 60),
               q1=None, q3=None)
    if len(secs) >= IQR_SAMPLES:
        q1, _, q3 = statistics.quantiles(secs, n=4)
        out.update(q1=round(q1 / 60), q3=round(q3 / 60))
    return out


def trimmed_mean(secs, drop=0.1):
    """Mean without the top and bottom tenth, as a check on the median.

    Not published: it is here so that a distribution the median hides
    (a bimodal pool of "act only" and "act plus side content" uploads, say)
    shows up as a gap between the two figures in the summary.
    """
    if not secs:
        return None
    cut = int(len(secs) * drop)
    kept = sorted(secs)[cut:len(secs) - cut] or sorted(secs)
    return round(statistics.fmean(kept) / 60)


def load_baseline(path):
    """{chapter_id|act_label: median minutes}, from either shape of input."""
    data = json.loads(pathlib.Path(path).read_text())
    if isinstance(data, dict):
        return data
    return {f"{a['chapter_id']}|{a['act_label']}": a["stats"]["median"]
            for a in data if a["stats"]["median"]}


def drift_against(baseline, act):
    """How far this act's median moved, as a fraction of the earlier one.

    An act whose median moves when the query set changes was never settled,
    whatever its sample size says, and this measures that instead of leaving it
    to a reviewer's judgement.
    """
    was = baseline.get(f"{act['chapter_id']}|{act['act_label']}")
    now = act["stats"]["median"]
    if not was or not now:
        return None
    return round((now - was) / was, 3)


def readmit_partials(rows):
    """Undo a "part of an act" rejection where the runtime contradicts the title.

    Some uploaders number the acts of a series ("Part 3: In Our Time"), others
    number the halves of one act, and the wording does not tell the two apart.
    The runtime does: an upload as long as the act the unambiguous uploads
    measured is covering that act, whatever it calls itself. The median is seeded
    from those unambiguous uploads alone, and readmission asks for more of it
    than the outlier trim would, because the title has already said this upload
    is a fragment.
    """
    solid = [r["seconds"] for r in rows if not r["rejected"]]
    if not solid:
        return
    median = statistics.median(solid)
    for row in rows:
        if row["rejected"] != ["part-of-an-act"]:
            continue
        if PARTIAL_READMIT * median <= row["seconds"] <= LONG_OUTLIER * median:
            row["rejected"] = []


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


def bundle_acts(bundle, title, chapter):
    """The two acts a bundled upload's title says it covers, if both are known."""
    match = bundle.search(title)
    if not match:
        return []
    wanted = [int(g) if g.isdigit() else ROMAN.get(g.upper())
              for g in match.groups()]
    found = [chapter.get(n) for n in wanted]
    return found if all(found) else []


def cross_check(acts):
    """Bundled uploads audit the acts they bundle, at no extra request.

    A video covering acts N and N+1 should run about as long as the two medians
    put together. It usually does, and where it does not, one of the two is
    wrong: cheap evidence that costs nothing, since these uploads were harvested
    anyway and are sitting in the rejected pile.
    """
    bundle = bundle_re(acts)
    by_chapter = {}
    for act in acts:
        by_chapter.setdefault(act["chapter_id"], {})[act_number(act["act_label"])] = act

    runtimes, seen = {}, set()
    for act in acts:
        for row in act["candidates"]:
            bundled = bundle_acts(bundle, row["title"], by_chapter[act["chapter_id"]])
            if not bundled or row["url"] in seen \
                    or "not-a-playthrough" in row["rejected"]:
                continue
            seen.add(row["url"])
            key = (act["chapter_id"], tuple(a["act_label"] for a in bundled))
            runtimes.setdefault(key, (bundled, []))[1].append(
                row.get("runtime", row["seconds"]))

    lines = []
    for (chapter, labels), (bundled, seconds) in sorted(runtimes.items()):
        expected = sum(a["stats"]["median"] or 0 for a in bundled)
        measured = round(statistics.median(seconds) / 60)
        if not expected:
            continue
        off = measured / expected - 1
        flag = "  <-- check these two" if abs(off) > BUNDLE_TOLERANCE else ""
        uploads = f"{len(seconds)} bundled upload" + ("s" if len(seconds) > 1 else "")
        lines.append(f"{chapter:>10} {' + '.join(labels):<20} "
                     f"medians {expected} min vs {measured} min "
                     f"across {uploads} ({off:+.0%}){flag}")
    return lines


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    compare = argv[argv.index("--compare") + 1] if "--compare" in argv else None
    if len(args) != 1 + bool(compare):
        print(__doc__)
        return 2
    workdir = pathlib.Path(args[0])
    baseline = load_baseline(compare) if compare else {}
    acts = load_acts(workdir)
    chapter_keys = load_json(workdir, "chapter_keys.json")
    for chapter, brands in version_keys(workdir, acts).items():
        chapter_keys[chapter] = chapter_keys.get(chapter, []) + brands
    act_keys = act_key_test(workdir)
    compilation = compilation_re(workdir, acts)
    partial = partial_test(workdir)
    enriched = load_enriched(workdir)
    quest_parts = load_json(workdir, "quest_parts.json")

    out = []
    for act in acts:
        parts = quest_parts.get(f"{act['chapter_id']}|{act['act_label']}", [])
        rows = candidates_for(act, workdir, chapter_keys, act_keys, compilation,
                              partial, enriched, parts)
        readmit_partials(rows)
        kept = trim_outliers([r for r in rows if not r["rejected"]])
        kept.sort(key=lambda r: r["seconds"])
        secs = [r["seconds"] for r in kept]
        act.update(candidates=rows, kept=kept, stats=dict(
            n=len(secs),
            median=round(statistics.median(secs) / 60) if secs else None,
            **spread(secs),
            trimmed_mean=trimmed_mean(secs),
            measured=sum(1 for r in kept if r.get("measured")),
            parts=part_medians(kept, parts)))
        act["stats"]["drift"] = drift_against(baseline, act) if baseline else None
        out.append(act)

    (workdir / "analysis.json").write_text(json.dumps(out, indent=1))
    for act in out:
        s = act["stats"]
        flag = "  <-- thin, top up or widen the queries" if s["n"] < 6 else ""
        iqr = f" iqr={s['q1']}-{s['q3']}" if s["q1"] else ""
        if s["drift"] is not None and abs(s["drift"]) >= UNSTABLE_DRIFT:
            flag = f"  <-- median moved {s['drift']:+.0%} against the baseline"
        print(f"{act['chapter_id']:>10} {act['act_label']:<16} n={s['n']:<3}"
              f"med={s['median']} mean={s['trimmed_mean']} "
              f"range={s['low']}-{s['high']}{iqr}"
              f"  {act['act_title'][:40]}{flag}")

    checks = cross_check(out)
    if checks:
        print("\ncross-check against multi-act uploads:")
        print("\n".join(checks))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Fill the marked regions of a report's authored markdown from analysis.json.

Usage: gen_docs.py <reportdir> [--no-verify]

Reads  <reportdir>/report.py    the game's configuration and structure
       <reportdir>/claims.py    what the authored prose asserts about the data
       <reportdir>/data/        the vault, analysis.json above all
Fills  <reportdir>/README.md    its chapter table, extremes table and thresholds
       <reportdir>/<slug>.md    one per chapter, in story order: the heading and
                                the at-a-glance table, and for every act its
                                heading, its figures and its evidence

The markdown files are hand-written. Only the marked regions are rewritten:

    <!--f:NAME-->value<!--/f-->            a derived figure inside a sentence
    <!--gen:KIND attr="value"-->           a derived block, on lines of its own
    ...body...
    <!--/gen-->

Every other byte of a file is left as its author wrote it. An unknown NAME or
KIND, a marker that is not paired up as above, or an act label the analysis does
not know, is an error naming the file and the marker; nothing is written then, so
a renamed act cannot silently leave a stale figure behind, nor a broken marker
cost the author the prose around it.

Every claim in the report's claims.py is checked against analysis.json before
anything is written; --no-verify fills anyway, for inspecting what a failing
claim produces.

Nothing here is game-specific: what the questline, its level gate and its wiki
are called comes from report.py and data/wiki.json, so a second game is a new
report directory rather than a second copy of this file.
"""
import json
import pathlib
import re
import sys

from analyze import (IQR_SAMPLES as MIN_SAMPLES, LONG_OUTLIER, SPAN_COVERAGE,
                     UNSTABLE_DRIFT)
from assertions import failures
from facts import (chapter_facts, chapter_total, hm, median_of, report_facts,
                   superlatives, word)
from queries import RECENT_VERSIONS

# The interquartile factors the confidence rating is graded on. Their companion
# thresholds (the eight-upload floor, the 10 percent drift) come from analyze.py,
# which screens against the same numbers.
SPREAD_HIGH = 1.25
SPREAD_MEDIUM = 1.5

BLOCK = re.compile(r"<!--gen:(?P<kind>[a-z-]+)(?P<attrs>[^>]*)-->\n"
                   r"(?P<body>.*?)<!--/gen-->", re.DOTALL)
INLINE = re.compile(r"<!--f:(?P<name>\w+)-->[^\n]*?<!--/f-->")
# Deliberately laxer than the two above, so that a marker they cannot match is
# still seen by the scan and named for what is wrong with it.
MARKER = re.compile(r"<!--(?P<close>/?)(?P<form>gen|f)(?::(?P<rest>[^>]*))?-->")
ATTR = re.compile(r'(\w+)="([^"]*)"')


class MarkerError(Exception):
    """A marker the filler cannot fill. The message names file and marker."""


def write(path, text):
    cleaned = "\n".join(line.rstrip() for line in text.splitlines()) + "\n"
    path.write_text(cleaned)


def fill(path, regions, facts):
    """The file's text with every marked region rewritten, nothing else touched."""
    text = path.read_text()
    expected = scan(path, text, regions, facts)

    def block(match):
        kind, attrs = match["kind"], match["attrs"]
        try:
            body = regions[kind](dict(ATTR.findall(attrs)))
        except MarkerError as e:
            raise MarkerError(f"{path}: <!--gen:{kind}{attrs}-->: {e}") from None
        return f"<!--gen:{kind}{attrs}-->\n" + "\n".join(body) + "\n<!--/gen-->"

    def inline(match):
        return marked(match["name"], facts[match["name"]])

    text, blocks = BLOCK.subn(block, text)
    text, values = INLINE.subn(inline, text)
    if (blocks, values) != expected:
        raise MarkerError(f"{path}: filled {blocks} of {expected[0]} region(s) "
                          f"and {values} of {expected[1]} value(s); "
                          f"refusing to write a file this run did not fill whole")
    return text


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def alone_on_line(text, match):
    line_start = text.rfind("\n", 0, match.start()) + 1
    return (match.start() == line_start
            and text[match.end():match.end() + 1] in ("\n", ""))


def scan(path, text, regions, facts):
    """Validate every marker in the file as read, and count what must be filled.

    BLOCK and INLINE cannot be trusted to discover a broken marker themselves:
    their bodies are non-greedy, so an opener whose closer is missing matches
    from there to the *next* region's closer, and substituting that match would
    delete the authored text and the marker in between while leaving the
    opener and closer counts balanced. So the file is checked before anything is
    replaced, and fill() compares what it filled against the count returned
    here. Every message names the file, the line and the marker at fault.
    """
    counts = {"gen": 0, "f": 0}
    unclosed = {"gen": None, "f": None}

    def at(match):
        return f"{path}:{line_of(text, match.start())}"

    for m in MARKER.finditer(text):
        form = m["form"]
        pending = unclosed[form]
        if m["close"]:
            if pending is None:
                raise MarkerError(f"{at(m)}: {m[0]} without an opening marker")
            if form == "f" and at(pending) != at(m):
                raise MarkerError(f"{at(pending)}: {pending[0]} must be closed "
                                  f"on the line it opens on")
            if form == "gen" and not alone_on_line(text, m):
                raise MarkerError(f"{at(m)}: {m[0]} must sit on a line of its own")
            unclosed[form] = None
            counts[form] += 1
            continue
        if pending is not None:
            raise MarkerError(f"{at(pending)}: {pending[0]} is never closed")
        rest = m["rest"] or ""
        if form == "gen":
            kind = rest.split(maxsplit=1)[0] if rest else ""
            if kind not in regions:
                raise MarkerError(f"{path}: unknown region <!--gen:{kind}-->")
            if not alone_on_line(text, m):
                raise MarkerError(f"{at(m)}: {m[0]} must sit on a line of its own")
        elif rest not in facts:
            raise MarkerError(f"{path}: unknown value <!--f:{rest}-->")
        unclosed[form] = m

    for pending in unclosed.values():
        if pending is not None:
            raise MarkerError(f"{at(pending)}: {pending[0]} is never closed")
    return counts["gen"], counts["f"]


def marked(name, value):
    """`<!--f:total-->9 h 03 min<!--/f-->`: a derived figure inside a sentence."""
    return f"<!--f:{name}-->{value}<!--/f-->"


def released_in(act, versions, version_index):
    """`Luna VII (6.6)`: the wiki's version name, plus its patch number."""
    name = versions.get(act["act_title"])
    if not name:
        return "unknown"
    number = version_index.get(name, {}).get("number")
    return f"{name} ({number})" if number and number != name else name


def plural(count, noun):
    return f"{count} {noun}" + ("" if count == 1 else "s")


def unit(report):
    """What this game calls one entry, lowercased, for the generated text.

    The pipeline calls it an act throughout, and the file and script names in
    the Files section keep that word, but a report on chapters or missions
    should not describe itself in a vocabulary the game never uses.
    """
    return report.config.get("unit", "Act").lower()


def bounds(stats):
    """The middle half where the sample carries it, the full spread otherwise."""
    if stats.get("q1") and stats.get("q3"):
        return stats["q1"], stats["q3"]
    return stats["low"], stats["high"]


def confidence(stats):
    n = stats["n"]
    if not n:
        return "none"
    drift = stats.get("drift")
    # A median that moves when the query set changes was never settled, whatever
    # the sample size and spread say about it.
    if drift is not None and abs(drift) >= UNSTABLE_DRIFT:
        return "low"
    if n < MIN_SAMPLES:
        return "low"
    low, high = bounds(stats)
    ratio = high / max(low, 1)
    if ratio <= SPREAD_HIGH:
        return "high"
    return "medium" if ratio <= SPREAD_MEDIUM else "low"


class Report:
    """One report directory: its configuration, its structure and its wiki."""

    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.data = self.path / "data"
        sys.path.insert(0, str(self.path))
        import claims
        import report
        self.claims = claims.CLAIMS
        self.config = report.REPORT
        self.chapters = report.CHAPTERS
        self.gates = report.GATES
        self.gate_default = report.GATE_DEFAULT
        wiki = json.loads((self.data / "wiki.json").read_text())
        self.game = (self.data / "game.txt").read_text().strip()
        self.wiki = f"https://{wiki['host']}/wiki/"

    def json(self, name):
        return json.loads((self.data / name).read_text())

    def link(self, title, page=None):
        """A wiki link, under a display title the page is not always named after."""
        page = page or title
        return f"[{title}]({self.wiki}{page.replace(' ', '_')})"

    def gate_for(self, act):
        key = f"{act['chapter_id']}|{act['act_label']}"
        return self.gates.get(key, self.gate_default.get(act["chapter_id"], "-"))


def views(row):
    """Exact where the second pass reached the video, approximate otherwise."""
    if row["views"] in (None, "NA", "None", ""):
        return "n/a"
    count = f"{int(row['views']):,}"
    return count if row.get("upload_date") else f"~{count}"


def uploaded(row):
    date = row.get("upload_date")
    return f"{date[:4]}-{date[4:6]}-{date[6:]}" if date else "n/a"


def evidence_table(act):
    lines = ["| Length | Video title | Uploader | Views | Uploaded | URL |",
             "| --- | --- | --- | --- | --- | --- |"]
    for r in act["kept"]:
        title = r["title"].replace("|", "\\|")
        uploader = r["uploader"].replace("|", "\\|")
        lines.append(f"| {hm(r['seconds'] / 60)} | {title} | {uploader} "
                     f"| {views(r)} | {uploaded(r)} | <{r['url']}> |")
    return lines


def ranged(stats):
    """`2 h 10 min to 2 h 40 min (middle half of 12; full spread ...)`."""
    low, high = stats["low"], stats["high"]
    if not (stats.get("q1") and stats.get("q3")):
        return f"{hm(low)} to {hm(high)}"
    return (f"{hm(stats['q1'])} to {hm(stats['q3'])} for the middle half "
            f"(full spread {hm(low)} to {hm(high)})")


def part_list(parts, timings):
    """Quest parts in wiki order, timed where enough uploads marked them out."""
    return "; ".join(f"{p} ({hm(timings[p])})" if p in timings else p
                     for p in parts)


def act_heading(report, act):
    return [f"### {act['act_label']} - "
            f"{report.link(act['act_title'], act.get('wiki_page'))}"]


def act_stats(report, act, parts, versions, version_index, superlative):
    """The derived superlative sentence, where there is one, and the bullets."""
    s = act["stats"]
    screened = len(act["candidates"]) - s["n"]
    sentence = superlative.get(f"{act['chapter_id']}|{act['act_label']}", "")
    body = [sentence] if sentence else []
    body += [
        "",
        f"- **Estimated length:** {hm(s['median'])}",
        f"- **Sampled range:** {ranged(s)} "
        f"across {s['n']} playthrough uploads "
        f"({plural(screened, 'further candidate')} screened out)",
        f"- **Confidence:** {confidence(s)}",
    ]
    if report.config["gate_label"]:
        body.append(f"- **{report.config['gate_label']} gate:** "
                    f"{report.gate_for(act)}")
    body.append(f"- **Released in:** {released_in(act, versions, version_index)}")
    if s.get("drift") is not None:
        body.append(f"- **Stability:** median {s['drift']:+.0%} "
                    f"against an earlier, independent query set")
    if s.get("measured"):
        body.append(f"- **Measured from the uploader's chapter markers:** "
                    f"{s['measured']} of {s['n']} uploads")
    if parts:
        body.append(f"- **Quest parts ({len(parts)}):** "
                    f"{part_list(parts, s.get('parts', {}))}")
    return body


def evidence_block(act):
    return ["<details>", "<summary>Evidence</summary>", ""] \
        + evidence_table(act) + ["", "</details>"]


def heading(chap, acts):
    return [
        f"# {chap['title']}",
        "",
        f"**Region:** {chap['region']} | "
        f"**Game versions:** {chap['versions']} | "
        f"**Entries:** {len(acts)} | "
        f"**Estimated chapter length: {hm(chapter_total(acts))}**",
    ]


def glance_table(report, acts):
    lines = [f"| {report.config.get('unit', 'Act')} | Title | Estimate "
             f"| Middle half | Uploads | Confidence |",
             "| --- | --- | --- | --- | --- | --- |"]
    for a in acts:
        s = a["stats"]
        lines.append(
            f"| {a['act_label']} | {a['act_title']} | {hm(s['median'])} "
            f"| {hm(bounds(s)[0])} - {hm(bounds(s)[1])} | {s['n']} "
            f"| {confidence(s)} |")
    return lines


def chapters_table(report, by_chapter):
    lines = ["| Chapter | Region | Versions | Entries | Estimated length | Detail |",
             "| --- | --- | --- | --- | --- | --- |"]
    for chap in report.chapters:
        acts = by_chapter[chap["id"]]
        lines.append(
            f"| {chap['title']} | {chap['region']} | {chap['versions']} "
            f"| {len(acts)} | {hm(chapter_total(acts))} "
            f"| [{chap['slug']}.md]({chap['slug']}.md) |")
    return lines


def extremes_table(report, all_acts):
    lines = [f"| | {report.config.get('unit', 'Act')} | Estimate |",
             "| --- | --- | --- |"]
    ranked = sorted(all_acts, key=median_of)
    for kind, picked in (("longest", reversed(ranked[-5:])),
                         ("shortest", ranked[:3])):
        for a in picked:
            lines.append(f"| {kind} | {a['chapter_title'].split(':')[0]}, "
                         f"{a['act_label']}: {a['act_title']} "
                         f"| {hm(a['stats']['median'])} |")
    return lines


def thresholds(report):
    """The figures the screening and the confidence rating are graded on.

    Every one of them is interpolated from the constant that enforces it, so a
    changed threshold rewrites its own description.
    """
    return [
        f"- {unit(report).capitalize()}s released within the last "
        f"{word(RECENT_VERSIONS)} versions are searched twice as deep, \n"
        "because they have far fewer uploads to draw on.",
        f"- A marker set covering less than {round(SPAN_COVERAGE * 100)} percent \n"
        f"of a single-{unit(report)} upload is ignored, \n"
        "as marking something other than the quest parts.",
        "- Of the uploads that survive screening, \n"
        f"anything below half or above {LONG_OUTLIER} times the median \n"
        "is dropped as truncated or padded.",
        f"- From {word(MIN_SAMPLES)} uploads on, the published range is "
        "the **middle half** \n"
        "(the interquartile range), with the full spread alongside it; \n"
        "below that it is the minimum and maximum.",
        f"- Confidence is *high* when the middle half spans a factor under "
        f"{SPREAD_HIGH} \n"
        f"and *medium* under {SPREAD_MEDIUM}. \n"
        f"It is *low* on fewer than {word(MIN_SAMPLES)} uploads, \n"
        f"and *low* for any {unit(report)} whose median moved by "
        f"{round(UNSTABLE_DRIFT * 100)} percent or more \n"
        "against the earlier, independent set of queries "
        "(`analyze.py --compare`), \n"
        "whatever its sample size says.",
    ]


def readme_regions(report, by_chapter, all_acts):
    return {
        "chapters": lambda attrs: chapters_table(report, by_chapter),
        "extremes": lambda attrs: extremes_table(report, all_acts),
        "thresholds": lambda attrs: thresholds(report),
    }


def chapter_regions(report, chap, acts, quest_parts, versions, version_index,
                    superlative):
    by_label = {a["act_label"]: a for a in acts}

    def act_of(attrs):
        label = attrs.get("act")
        act = by_label.get(label)
        if not act:
            raise MarkerError(f"no {unit(report)} labelled {label!r} "
                              f"in {chap['id']}")
        return act

    def stats_region(attrs):
        act = act_of(attrs)
        parts = quest_parts.get(f"{act['chapter_id']}|{act['act_label']}", [])
        return act_stats(report, act, parts, versions, version_index, superlative)

    return {
        "heading": lambda attrs: heading(chap, acts),
        "glance": lambda attrs: glance_table(report, acts),
        "act-heading": lambda attrs: act_heading(report, act_of(attrs)),
        "stats": stats_region,
        "evidence": lambda attrs: evidence_block(act_of(attrs)),
    }


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    verify = "--no-verify" not in argv[1:]
    report = Report(args[0])
    analysis = report.json("analysis.json")
    quest_parts = report.json("quest_parts.json")
    versions = report.json("versions.json")
    version_index = report.json("version_index.json")

    broken = failures(analysis, report.claims)
    if broken:
        print("the prose no longer matches the data:\n", file=sys.stderr)
        for line in broken:
            print(f"  {line}\n", file=sys.stderr)
        if verify:
            print(f"{len(broken)} claim(s) failed, nothing written "
                  f"(--no-verify to fill anyway)", file=sys.stderr)
            return 1

    superlative = superlatives(analysis, unit(report))
    by_chapter = {}
    for act in analysis:
        by_chapter.setdefault(act["chapter_id"], []).append(act)
    facts = report_facts(analysis, report.config.get("unit", "Act"), report.game,
                         report.config["date"])

    # Every file is filled before any is written, so a marker error in the last
    # chapter does not leave the earlier ones rewritten.
    filled = {}
    try:
        for chap in report.chapters:
            acts = by_chapter[chap["id"]]
            regions = chapter_regions(report, chap, acts, quest_parts, versions,
                                      version_index, superlative)
            path = report.path / f"{chap['slug']}.md"
            filled[path] = fill(path, regions,
                                facts | chapter_facts(acts, quest_parts))
        path = report.path / "README.md"
        filled[path] = fill(path, readme_regions(report, by_chapter, analysis),
                            facts)
    except MarkerError as e:
        print(e, file=sys.stderr)
        return 1

    for path, text in filled.items():
        write(path, text)
        print("filled", path.name)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

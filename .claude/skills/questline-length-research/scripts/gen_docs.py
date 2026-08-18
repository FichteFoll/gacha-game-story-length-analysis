#!/usr/bin/env python3
"""Render the per-chapter markdown reports from analysis.json and the authored prose.

Usage: gen_docs.py <reportdir> [--no-verify]

Reads  <reportdir>/report.py    the game's configuration and the authored prose
       <reportdir>/claims.py    what that prose asserts about the data
       <reportdir>/data/        the vault, analysis.json above all
Writes <reportdir>/README.md    index, method and caveats
       <reportdir>/<slug>.md    one per chapter, in story order

Every claim in the report's claims.py is checked against analysis.json before
anything is written; --no-verify renders anyway, for inspecting what a failing
claim produces.

Nothing here is game-specific: what the questline, its level gate and its wiki
are called comes from report.py and data/wiki.json, so a second game is a new
report directory rather than a second copy of this file.
"""
import json
import pathlib
import sys

from analyze import (IQR_SAMPLES as MIN_SAMPLES, LONG_OUTLIER, SPAN_COVERAGE,
                     UNSTABLE_DRIFT)
from assertions import failures
from facts import chapter_facts, chapter_total, hm, median_of, superlatives, word
from queries import RECENT_VERSIONS

# The interquartile factors the confidence rating is graded on. Their companion
# thresholds (the eight-upload floor, the 10 percent drift) come from analyze.py,
# which screens against the same numbers.
SPREAD_HIGH = 1.25
SPREAD_MEDIUM = 1.5


def write(path, text):
    cleaned = "\n".join(line.rstrip() for line in text.splitlines()) + "\n"
    path.write_text(cleaned)


def prose(text, facts=None):
    """Keep the authored semantic line breaks, and fill in the derived figures.

    An unknown placeholder raises KeyError rather than rendering a stale number.
    """
    text = text.replace(" \n", "\n")
    return text.format_map(facts) if facts else text


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
    """What this game calls one entry, lowercased, for the renderer's own prose.

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
    """One report directory: its configuration, its prose and its wiki."""

    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.data = self.path / "data"
        sys.path.insert(0, str(self.path))
        import claims
        import report
        self.claims = claims.CLAIMS
        self.config = report.REPORT
        self.chapters = report.CHAPTERS
        self.act_notes = report.ACT_NOTES
        self.gates = report.GATES
        self.gate_default = report.GATE_DEFAULT
        wiki = json.loads((self.data / "wiki.json").read_text())
        self.wiki_name = wiki["name"]
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
    return "\n".join(lines)


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


def act_section(report, act, parts, versions, version_index, facts, superlative):
    key = f"{act['chapter_id']}|{act['act_label']}"
    s = act["stats"]
    screened = len(act["candidates"]) - s["n"]
    note = "\n".join(filter(None, [prose(report.act_notes.get(key, ""), facts),
                                   superlative.get(key)]))
    body = [
        f"### {act['act_label']} - "
        f"{report.link(act['act_title'], act.get('wiki_page'))}",
        "",
        note,
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
    body += ["", "<details>", "<summary>Evidence</summary>", "",
             evidence_table(act), "", "</details>", ""]
    return "\n".join(body)


def chapter_doc(report, chap, acts, quest_parts, versions, version_index,
                superlative):
    total = chapter_total(acts)
    facts = chapter_facts(acts, quest_parts)
    head = [
        f"# {chap['title']}",
        "",
        f"**Region:** {chap['region']} | "
        f"**Game versions:** {chap['versions']} | "
        f"**Entries:** {len(acts)} | "
        f"**Estimated chapter length: {hm(total)}**",
        "",
        prose(chap["blurb"], facts),
        "",
        "## At a glance",
        "",
        f"| {report.config.get('unit', 'Act')} | Title | Estimate "
        f"| Middle half | Uploads | Confidence |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for a in acts:
        s = a["stats"]
        head.append(
            f"| {a['act_label']} | {a['act_title']} | {hm(s['median'])} "
            f"| {hm(bounds(s)[0])} - {hm(bounds(s)[1])} | {s['n']} "
            f"| {confidence(s)} |")
    head += ["", f"**Total: {hm(total)}**", "", "## Pacing", "",
             prose(chap["pacing"], facts), "",
             f"## {report.config.get('unit', 'Act')}s", ""]
    for a in acts:
        parts = quest_parts.get(f"{a['chapter_id']}|{a['act_label']}", [])
        head.append(act_section(report, a, parts, versions, version_index, facts,
                                superlative))
    overview = report.config["overview_page"]
    gate = report.config["gate_label"]
    sourced = f"Questline structure, {unit(report)} titles, quest parts"
    if gate:
        sourced += f" and {gate} gates"
    head += [
        "## Sources",
        "",
        f"- {sourced}: "
        f"{report.link(chap['wiki_page'])} "
        f"and {report.link(overview)} on the {report.wiki_name} (Fandom).",
        f"- Durations: the YouTube uploads listed under each {unit(report)} above. \n"
        "See [README.md](README.md) for the method and its limits.",
        "",
    ]
    return "\n".join(head)


def method(report):
    """What this game's harvest and screening do that another game's does not.

    The procedure itself is described once, in the repository README; only the
    game's own wiki, queries and upload habits are written down here.
    """
    overview = report.config["overview_page"]
    gate = report.config["gate_label"]
    sourced = (f"the chapter and {unit(report)} list, the {unit(report)} titles, "
               "the quest parts")
    if gate:
        sourced += f" \nand the {gate} gates"
    lines = [
        f"- **Structure:** {sourced} come from the \n"
        f"[{overview} page]({report.wiki}{overview.replace(' ', '_')}) \n"
        f"and the individual chapter and {unit(report)} pages "
        f"of the {report.wiki_name}.",
        f"- **Searches:** {report.config['queries']}",
        f"- **Compilations:** multi-{unit(report)} uploads such as \n"
        f"{report.config['compilations']}, \n"
        f"which count only where their chapter markers \n"
        f"located this {unit(report)} inside them.",
    ]
    partials = report.config.get("partials")
    if partials:
        lines.append(f"- **Partial uploads:** {partials}.")
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


def limits(report):
    """The caveats of this game, on top of the ones every report shares."""
    return [f"- {c}" for c in report.config["caveats"]]


def readme(report, by_chapter):
    grand = sum(chapter_total(acts) for acts in by_chapter.values())
    n_videos = sum(a["stats"]["n"] for acts in by_chapter.values() for a in acts)
    n_screened = sum(len(a["candidates"]) for acts in by_chapter.values() for a in acts)
    lines = [
        f"# {report.config['title']}",
        "",
        report.config["intro"],
        "",
        f"**Total for the whole main questline: {hm(grand)}** "
        f"({sum(len(a) for a in by_chapter.values())} entries "
        f"counting {report.config.get('entries_are', 'acts, preludes and interludes')}, "
        f"measured against {n_videos} accepted uploads "
        f"out of {n_screened} candidates).\n"
        f"That figure is the sum of the per-{unit(report)} medians, "
        "so treat it as an order of magnitude "
        "rather than a number anyone actually clocked end to end.",
        "",
        "## Chapters",
        "",
        "| Chapter | Region | Versions | Entries | Estimated length | Detail |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for chap in report.chapters:
        acts = by_chapter[chap["id"]]
        total = chapter_total(acts)
        lines.append(
            f"| {chap['title']} | {chap['region']} | {chap['versions']} "
            f"| {len(acts)} | {hm(total)} | [{chap['slug']}.md]({chap['slug']}.md) |")
    lines += [
        "",
        f"## Longest and shortest {report.config.get('unit', 'Act').lower()}s",
        "",
        f"| | {report.config.get('unit', 'Act')} | Estimate |",
        "| --- | --- | --- |",
    ]
    ranked = sorted((a for acts in by_chapter.values() for a in acts),
                    key=median_of)
    for a in reversed(ranked[-5:]):
        lines.append(f"| longest | {a['chapter_title'].split(':')[0]}, "
                     f"{a['act_label']}: {a['act_title']} "
                     f"| {hm(a['stats']['median'])} |")
    for a in ranked[:3]:
        lines.append(f"| shortest | {a['chapter_title'].split(':')[0]}, "
                     f"{a['act_label']}: {a['act_title']} "
                     f"| {hm(a['stats']['median'])} |")
    lines += [
        "",
        "## Method",
        "",
        "The pipeline, the evidence vault it leaves behind \n"
        "and what these numbers do and do not mean \n"
        "are described in the [repository README](../README.md). \n"
        f"Specific to {report.game}:",
        "",
    ] + method(report)
    lines += ["", "The figures it screens and grades on:", ""] + thresholds(report)
    lines += ["", "## Limits of this report", "",
              "Beyond the limits every report in this repository shares, \n"
              "listed in the [repository README](../README.md):", ""] + limits(report)
    lines += ["", f"Data collected {report.config['date']}.", ""]
    return "\n".join(lines)


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
                  f"(--no-verify to render anyway)", file=sys.stderr)
            return 1

    superlative = superlatives(analysis, report.config.get("unit", "Act").lower())
    by_chapter = {}
    for act in analysis:
        by_chapter.setdefault(act["chapter_id"], []).append(act)

    for chap in report.chapters:
        doc = chapter_doc(report, chap, by_chapter[chap["id"]], quest_parts,
                          versions, version_index, superlative)
        write(report.path / f"{chap['slug']}.md", doc)
        print("wrote", chap["slug"] + ".md")
    write(report.path / "README.md", readme(report, by_chapter))
    print("wrote README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

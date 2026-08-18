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
    """The pipeline, described for a reader who did not run it.

    Every threshold quoted here is interpolated from the constant that enforces
    it, so a change to the screening cannot leave the method text describing the
    old one.
    """
    overview = report.config["overview_page"]
    gate = report.config["gate_label"]
    sourced = (f"The chapter and {unit(report)} list, the {unit(report)} titles, "
              f"the quest parts")
    if gate:
        sourced += f" \nand the {gate} gates"
    return [
        "1. **Structure from the wiki.** \n"
        f"{sourced} come from the \n"
        f"[{overview} page]({report.wiki}{overview.replace(' ', '_')}) \n"
        f"and the individual chapter and {unit(report)} pages of the {report.wiki_name}. \n"
        "Fandom serves a Cloudflare challenge to plain HTTP clients, \n"
        "so the pages were read through the MediaWiki API \n"
        "(`/api.php?action=query&prop=revisions&rvprop=content`) instead.",
        "",
        "2. **Durations from playthrough uploads.** \n"
        f"{report.config['queries']} \n"
        f"{unit(report).capitalize()}s released within the last "
        f"{word(RECENT_VERSIONS)} versions "
        f"are searched twice as deep, \n"
        "because they have far fewer uploads to draw on. \n"
        "Each result was collected with its runtime, title, uploader, \n"
        "view count and URL.",
        "",
        "3. **A second pass over the candidates worth measuring.** \n"
        "The search listing gives rounded view counts and no upload date, \n"
        "so every candidate that was not discarded outright \n"
        "is fetched again in full. \n"
        "That yields exact view counts and upload dates, \n"
        "and the uploader's own chapter markers. \n"
        "YouTube rate-limits these requests, \n"
        "so the pass covers as many as it manages \n"
        "and the rest keep their figures from the search listing.",
        "",
        f"4. **Locating the {unit(report)} inside the upload.** \n"
        "Where an uploader marked out their video with chapter markers, \n"
        f"the markers are matched against the {unit(report)}'s quest parts, \n"
        "its title and its number, \n"
        f"and the {unit(report)} is measured from those markers rather than from \n"
        "the video's total runtime. \n"
        "That drops the uploader's pre-roll and detours from the measurement, \n"
        f"turns an upload covering two {unit(report)}s into evidence for each of them, \n"
        "and, where enough uploads marked the same quest part, \n"
        "gives that part its own median. \n"
        f"A marker set that covers less than {round(SPAN_COVERAGE * 100)} percent \n"
        f"of a single-{unit(report)} upload is ignored: \n"
        "those markers were something other than the quest parts, \n"
        f"and trusting them would under-measure the {unit(report)}.",
        "",
        "5. **Screening.** \n"
        "A candidate is discarded when its title marks it as something other than \n"
        f"a hands-on playthrough of exactly that {unit(report)}: \n"
        "cutscene reels, cinematic edits, lore explainers, guides and reaction videos; \n"
        "livestreams and let's-plays, whose idle chatter inflates runtime; \n"
        f"multi-{unit(report)} compilations such as {report.config['compilations']}, \n"
        f"unless their chapter markers located this {unit(report)} inside them; \n"
        + partials_clause(report) +
        f"and uploads whose title does not name the {unit(report)} \n"
        f"either by name or by chapter plus {unit(report)} number. \n"
        f"Of the survivors, anything below half or above {LONG_OUTLIER} times "
        f"the median \n"
        "is dropped as a truncated or padded upload.",
        "",
        "6. **Estimate.** \n"
        "The published figure is the **median** of the accepted uploads. \n"
        f"From {word(MIN_SAMPLES)} uploads on, the published range is "
        f"the **middle half** \n"
        "(the interquartile range), with the full spread given alongside it: \n"
        "one padded upload widens a min-max range that is otherwise tight, \n"
        f"and says more about that uploader than about the {unit(report)}. \n"
        f"Below {word(MIN_SAMPLES)} uploads there is no distribution to speak of \n"
        "and the range is the minimum and maximum. \n"
        f"Nothing is rated above *low* on fewer than {word(MIN_SAMPLES)} uploads. \n"
        "From there, confidence is *high* \n"
        f"when the middle half spans a factor under {SPREAD_HIGH} \n"
        f"and *medium* under {SPREAD_MEDIUM}. \n"
        "Everything else is *low*, \n"
        f"as is any {unit(report)} whose median moved by "
        f"{round(UNSTABLE_DRIFT * 100)} "
        f"percent or more \n"
        "against the earlier, independent set of queries \n"
        "(`analyze.py --compare`): \n"
        "a figure that moves when the queries change was never settled, \n"
        "whatever its sample size says.",
    ]


def partials_clause(report):
    """What an upload covering less than one act looks like, where that happens.

    Only some games have the habit, so the clause is the report's to write and
    absent everywhere else, in step with data/partials.txt.
    """
    partials = report.config.get("partials")
    return f"{partials}; \n" if partials else ""


def limits(report):
    """What the numbers are, and the report's own caveats after the shared ones."""
    shared = [
        f"- They measure **video runtime of someone playing the {unit(report)}**, \n"
        f"which is the closest available proxy for how long the {unit(report)} takes. \n"
        "They are not official figures; \n"
        f"{report.config['publisher']} does not publish {unit(report)} lengths.",
        "- Runtime includes the traversal, dialogue and combat \n"
        "that a player cannot skip, \n"
        "but it also includes whatever detours the uploader took, \n"
        "and it excludes the time a first-time player spends \n"
        "re-reading dialogue or dying to a boss. \n"
        "Treat the median as a middle estimate and the range as the real spread.",
        "- Uploaders play at different speeds, \n"
        "skip cutscenes to different degrees, \n"
        "and record on different game versions. \n"
        f"{unit(report).capitalize()}s that were rebalanced or shortened after release \n"
        "may be measured against older, longer uploads.",
    ]
    return shared + [f"- {c}" for c in report.config["caveats"]]


def steering_inputs(report):
    """The tail of the input list, which partials.txt joins where it exists."""
    if (report.data / "partials.txt").exists():
        return ", `data/compilations.txt` \nand `data/partials.txt`"
    return " and `data/compilations.txt`"


def files_section(report):
    return [
        "- One markdown file per chapter, listed in the table above. \n"
        f"Each {unit(report)} section carries a collapsed evidence table \n"
        "with runtime, video title, uploader, view count, upload date and URL \n"
        "for every accepted upload. \n"
        "A view count prefixed with `~` came from the search listing \n"
        "and is rounded; the rest are exact.",
        "- `data/analysis.json` holds the same evidence in machine-readable form, \n"
        "including the rejected candidates and the reason each was rejected.",
        "- `data/acts.tsv` is the act list extracted from the wiki.",
        "- `data/evidence/` holds the raw harvest, one file per act, \n"
        "before any screening was applied.",
        "- `data/versions.json` maps each act to its release version, \n"
        "as categorized on the wiki, \n"
        "and `data/version_index.json` gives each version \n"
        "its patch number and release date. \n"
        "Both are fetched by `fetch_versions.py` before the harvest, \n"
        "because the harvest searches for version-branded upload titles.",
        "- `data/quest_parts.json` lists the quest parts of each act, \n"
        "in the order the wiki gives them.",
        "- `data/wiki.json`, `data/game.txt`, `data/chapter_keys.json`, \n"
        f"`data/query_templates.txt`{steering_inputs(report)} \n"
        "are the inputs the pipeline is steered with, described under Method.",
        "- The scripts themselves live in the `questline-length-research` skill \n"
        "(`.claude/skills/questline-length-research/scripts/`), \n"
        "shared by every report in this repository: \n"
        "`harvest.sh` collects the candidates, \n"
        "`topup.sh` widens a thin act's pool, \n"
        "`analyze.py` screens them and computes the statistics, \n"
        "`enrich.sh` fetches exact metadata and chapter markers for the survivors, \n"
        "and `gen_docs.py` renders these markdown files from `analysis.json`. \n"
        "Re-running \n"
        "`analyze.py data --compare data/baseline.json` \n"
        "over the harvested evidence reproduces `data/analysis.json` exactly.",
        "- `data/baseline.json` holds the per-act medians \n"
        "from the first, independent set of queries, \n"
        "which is what the stability figure is measured against.",
        "- Every figure in the prose is interpolated from `analysis.json` \n"
        "rather than written by hand, \n"
        "and the claims the prose makes in words \n"
        "are asserted in `claims.py` before any file is written. \n"
        "A claim that no longer holds fails the build.",
    ]


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
    lines += ["", "## Method", ""] + method(report)
    lines += ["", "## What these numbers do and do not mean", ""] + limits(report)
    lines += ["", "## Files", ""] + files_section(report)
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

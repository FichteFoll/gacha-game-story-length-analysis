#!/usr/bin/env python3
"""Render the per-chapter markdown reports from analysis.json and the authored prose.

Usage: gen_docs.py [--no-verify]

Every claim in claims.py is checked against analysis.json before anything is
written; --no-verify renders anyway, for inspecting what a failing claim produces.
"""
import json
import pathlib
import sys

from chapter_text import AR, AR_DEFAULT, ACT_NOTES, CHAPTERS
from claims import failures
from facts import chapter_facts, chapter_total, hm, median_of, superlatives

OUT = pathlib.Path(__file__).parent.parent
DATA = OUT / "data"

WIKI = "https://genshin-impact.fandom.com/wiki/"

# The middle half of a sample is tighter than its extremes by construction, so it
# is held to a tighter factor: the two ladders are meant to rate alike.
SPREAD_HIGH = {True: 1.25, False: 1.6}
SPREAD_MEDIUM = {True: 1.5, False: 2.2}


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


def bounds(stats):
    """The middle half where the sample carries it, the full spread otherwise."""
    if stats.get("q1") and stats.get("q3"):
        return stats["q1"], stats["q3"]
    return stats["low"], stats["high"]


def confidence(stats):
    n = stats["n"]
    if not n:
        return "none"
    low, high = bounds(stats)
    ratio = high / max(low, 1)
    interquartile = bool(stats.get("q1"))
    if n >= 8 and ratio <= SPREAD_HIGH[interquartile]:
        return "high"
    if n >= 6 and ratio <= SPREAD_MEDIUM[interquartile]:
        return "medium"
    return "low"


def ar_for(act):
    key = f"{act['chapter_id']}|{act['act_label']}"
    return AR.get(key, AR_DEFAULT.get(act["chapter_id"], "-"))


def wiki_link(title):
    return f"[{title}]({WIKI}{title.replace(' ', '_')})"


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


def act_section(act, parts, versions, version_index, facts, superlative):
    key = f"{act['chapter_id']}|{act['act_label']}"
    s = act["stats"]
    screened = len(act["candidates"]) - s["n"]
    note = "\n".join(filter(None, [prose(ACT_NOTES.get(key, ""), facts),
                                   superlative.get(key)]))
    body = [
        f"### {act['act_label']} - {wiki_link(act['act_title'])}",
        "",
        note,
        "",
        f"- **Estimated length:** {hm(s['median'])}",
        f"- **Sampled range:** {ranged(s)} "
        f"across {s['n']} playthrough uploads "
        f"({screened} further candidates screened out)",
        f"- **Confidence:** {confidence(s)}",
        f"- **Adventure Rank gate:** {ar_for(act)}",
        f"- **Released in:** {released_in(act, versions, version_index)}",
    ]
    if s.get("measured"):
        body.append(f"- **Measured from the uploader's chapter markers:** "
                    f"{s['measured']} of {s['n']} uploads")
    if parts:
        body.append(f"- **Quest parts ({len(parts)}):** "
                    f"{part_list(parts, s.get('parts', {}))}")
    body += ["", "<details>", "<summary>Evidence</summary>", "",
             evidence_table(act), "", "</details>", ""]
    return "\n".join(body)


def chapter_doc(chap, acts, quest_parts, versions, version_index, superlative):
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
        "| Act | Title | Estimate | Middle half | Uploads | Confidence |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for a in acts:
        s = a["stats"]
        head.append(
            f"| {a['act_label']} | {a['act_title']} | {hm(s['median'])} "
            f"| {hm(bounds(s)[0])} - {hm(bounds(s)[1])} | {s['n']} "
            f"| {confidence(s)} |")
    head += ["", f"**Total: {hm(total)}**", "", "## Pacing", "",
             prose(chap["pacing"], facts), "", "## Acts", ""]
    for a in acts:
        parts = quest_parts.get(f"{a['chapter_id']}|{a['act_label']}", [])
        head.append(act_section(a, parts, versions, version_index, facts,
                                superlative))
    head += [
        "## Sources",
        "",
        f"- Questline structure, act titles, quest parts and Adventure Rank gates: "
        f"{wiki_link(chap['wiki_page'])} "
        f"and [Archon Quest]({WIKI}Archon_Quest) on the Genshin Impact Wiki (Fandom).",
        "- Durations: the YouTube uploads listed under each act above. \n"
        "See [README.md](README.md) for the method and its limits.",
        "",
    ]
    return "\n".join(head)


def readme(chapters, by_chapter):
    grand = sum(chapter_total(acts) for acts in by_chapter.values())
    n_videos = sum(a["stats"]["n"] for acts in by_chapter.values() for a in acts)
    n_screened = sum(len(a["candidates"]) for acts in by_chapter.values() for a in acts)
    lines = [
        "# Genshin Impact Archon Questline: How Long Each Act Takes",
        "",
        "Duration estimates for every main act of the Archon Quest storyline, \n"
        "from the Mondstadt Prologue to Chapter VII, \n"
        "each one backed by the YouTube playthroughs it was measured from.",
        "",
        f"**Total for the whole main questline: {hm(grand)}** "
        f"({sum(len(a) for a in by_chapter.values())} entries "
        f"counting acts, preludes and interludes, "
        f"measured against {n_videos} accepted uploads "
        f"out of {n_screened} candidates).\n"
        "That figure is the sum of the per-act medians, "
        "so treat it as an order of magnitude "
        "rather than a number anyone actually clocked end to end.",
        "",
        "## Chapters",
        "",
        "| Chapter | Region | Versions | Entries | Estimated length | Detail |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for chap in chapters:
        acts = by_chapter[chap["id"]]
        total = chapter_total(acts)
        lines.append(
            f"| {chap['title']} | {chap['region']} | {chap['versions']} "
            f"| {len(acts)} | {hm(total)} | [{chap['slug']}.md]({chap['slug']}.md) |")
    lines += [
        "",
        "## Longest and shortest acts",
        "",
        "| | Act | Estimate |",
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
        "1. **Structure from the wiki.** \n"
        "The chapter and act list, the act titles, the quest parts \n"
        "and the Adventure Rank gates come from the \n"
        "[Archon Quest page](https://genshin-impact.fandom.com/wiki/Archon_Quest) \n"
        "and the individual chapter and act pages of the Genshin Impact Wiki. \n"
        "Fandom serves a Cloudflare challenge to plain HTTP clients, \n"
        "so the pages were read through the MediaWiki API \n"
        "(`/api.php?action=query&prop=revisions&rvprop=content`) instead.",
        "",
        "2. **Durations from playthrough uploads.** \n"
        "For every act, YouTube was searched four ways: \n"
        "by chapter plus act label plus act title, by act title alone, \n"
        "and twice by the patch branding recent uploads use instead of act titles \n"
        "(\"Genshin Impact 6.6 Act 10 ...\"). \n"
        "Acts released within the last four versions are searched twice as deep, \n"
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
        "4. **Locating the act inside the upload.** \n"
        "Where an uploader marked out their video with chapter markers, \n"
        "the markers are matched against the act's quest parts, \n"
        "its title and its number, \n"
        "and the act is measured from those markers rather than from \n"
        "the video's total runtime. \n"
        "That drops the uploader's pre-roll and detours from the measurement, \n"
        "turns an upload covering two acts into evidence for each of them, \n"
        "and, where enough uploads marked the same quest part, \n"
        "gives that part its own median. \n"
        "A marker set that covers less than 60 percent \n"
        "of a single-act upload is ignored: \n"
        "those markers were something other than the quest parts, \n"
        "and trusting them would under-measure the act.",
        "",
        "5. **Screening.** \n"
        "A candidate is discarded when its title marks it as something other than \n"
        "a hands-on playthrough of exactly that act: \n"
        "cutscene reels, cinematic edits, lore explainers, guides and reaction videos; \n"
        "livestreams and let's-plays, whose idle chatter inflates runtime; \n"
        "multi-act compilations such as \"Acts 9 & 10\" or \"Full Sumeru Archon Quest\", \n"
        "unless their chapter markers located this act inside them; \n"
        "and uploads whose title does not name the act \n"
        "either by name or by chapter plus act number. \n"
        "Of the survivors, anything below half or above 1.8 times the median \n"
        "is dropped as a truncated or padded upload.",
        "",
        "6. **Estimate.** \n"
        "The published figure is the **median** of the accepted uploads. \n"
        "From eight uploads on, the published range is the **middle half** \n"
        "(the interquartile range), with the full spread given alongside it: \n"
        "one padded upload widens a min-max range that is otherwise tight, \n"
        "and says more about that uploader than about the act. \n"
        "Below eight uploads there is no distribution to speak of \n"
        "and the range is the minimum and maximum. \n"
        "Confidence is *high* at eight or more uploads \n"
        "whose middle half spans a factor under 1.25, \n"
        "and *medium* at six or more under 1.5. \n"
        "Where the sample is too small for an interquartile range, \n"
        "the same ladder runs on the full spread at 1.6 and 2.2, \n"
        "which is the looser test the extremes deserve. \n"
        "Everything else is *low*.",
        "",
        "## What these numbers do and do not mean",
        "",
        "- They measure **video runtime of someone playing the act**, \n"
        "which is the closest available proxy for how long the act takes. \n"
        "They are not official figures; \n"
        "HoYoverse does not publish act lengths.",
        "- Runtime includes the traversal, dialogue and combat \n"
        "that a player cannot skip, \n"
        "but it also includes whatever detours the uploader took, \n"
        "and it excludes the time a first-time player spends \n"
        "re-reading dialogue or dying to a boss. \n"
        "Treat the median as a middle estimate and the range as the real spread.",
        "- Uploaders play at different speeds, \n"
        "skip cutscenes to different degrees, \n"
        "and record on different game versions. \n"
        "Acts that were rebalanced or shortened after release \n"
        "may be measured against older, longer uploads.",
        "- The newest acts (Nod-Krai's later acts, Chapter VII) \n"
        "have the fewest uploads to draw on, \n"
        "so their figures are the softest. \n"
        "They are marked *low* or *medium* confidence accordingly.",
        "- Interlude Chapter acts \n"
        "(*The Crane Returns on the Wind*, *Perilous Trail*, \n"
        "*Inversion of Genesis*, *Paralogism*) \n"
        "are Archon Quests but not part of the main chapter progression, \n"
        "so they are outside this report's scope.",
        "",
        "## Files",
        "",
        "- One markdown file per chapter, listed in the table above. \n"
        "Each act section carries a collapsed evidence table \n"
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
        "Both are fetched by `pipeline/fetch_versions.py` before the harvest, \n"
        "because the harvest searches for version-branded upload titles.",
        "- `data/quest_parts.json` lists the quest parts of each act, \n"
        "in the order the wiki gives them.",
        "- `data/chapter_keys.json` and `data/compilations.txt` \n"
        "are the screening inputs described under Method.",
        "- `pipeline/` holds the scripts that produced all of this: \n"
        "`harvest.sh` collects the candidates, \n"
        "`topup.sh` widens a thin act's pool, \n"
        "`analyze.py` screens them and computes the statistics, \n"
        "and `gen_docs.py` renders these markdown files from `analysis.json`. \n"
        "Re-running `analyze.py` over the harvested evidence \n"
        "reproduces `data/analysis.json` exactly.",
        "- Every figure in the prose is interpolated from `analysis.json` \n"
        "by `pipeline/facts.py` rather than written by hand, \n"
        "and the claims the prose makes in words \n"
        "are asserted in `pipeline/claims.py` before any file is written. \n"
        "A claim that no longer holds fails the build.",
        "",
        f"Data collected {DATE}.",
        "",
    ]
    return "\n".join(lines)


DATE = "2026-08-18"


def main(argv):
    verify = "--no-verify" not in argv[1:]
    analysis = json.loads((DATA / "analysis.json").read_text())
    quest_parts = json.loads((DATA / "quest_parts.json").read_text())
    versions = json.loads((DATA / "versions.json").read_text())
    version_index = json.loads((DATA / "version_index.json").read_text())
    broken = failures(analysis)
    if broken:
        print("the prose no longer matches the data:\n", file=sys.stderr)
        for line in broken:
            print(f"  {line}\n", file=sys.stderr)
        if verify:
            print(f"{len(broken)} claim(s) failed, nothing written "
                  f"(--no-verify to render anyway)", file=sys.stderr)
            return 1

    superlative = superlatives(analysis)
    by_chapter = {}
    for act in analysis:
        by_chapter.setdefault(act["chapter_id"], []).append(act)

    for chap in CHAPTERS:
        doc = chapter_doc(chap, by_chapter[chap["id"]], quest_parts, versions,
                          version_index, superlative)
        write(OUT / f"{chap['slug']}.md", doc)
        print("wrote", chap["slug"] + ".md")
    write(OUT / "README.md", readme(CHAPTERS, by_chapter))
    print("wrote README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

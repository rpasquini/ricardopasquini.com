# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "beautifulsoup4",
# ]
# ///
"""Best-effort structured extraction of the /publications page into
src/content/publications/data.json. This is a DRAFT — entries are flagged
with needsReview when the parser wasn't confident (missing year, no
abstract found, authors/venue not cleanly separable, etc). A human pass is
still required before treating this as final.

Usage: uv run scripts/extract_publications.py
"""

import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_HTML = REPO_ROOT / "src" / "content" / "pages-raw" / "publications-raw.html"
OUT_JSON = REPO_ROOT / "src" / "content" / "publications" / "data.json"

SECTION_MAP = {
    "WORKING PAPERS": "working-paper",
    "REFEREED PUBLICATIONS": "refereed",
    "PREVIOUS WORK BY TOPIC": "previous-work",
}

YEAR_RE = re.compile(r"^\s*(\d{4})\b")
QUOTE_RE = re.compile(r"[“”\"](.+?)[“”\"]")
WITH_RE = re.compile(r"\bwith\s+(.+?)(?:[.\n]|$)", re.IGNORECASE)
KEYWORDS_RE = re.compile(r"Keywords?:\s*(.+?)(?:\s*JEL Classification:\s*(.+))?$", re.IGNORECASE)
SPACE_BEFORE_LABEL_RE = re.compile(r"(?<=[a-zà-ÿ.,;)\"'])(Keywords?:|JEL Classification:)")


def classify_link(url: str) -> str:
    u = url.lower()
    if "ssrn.com" in u:
        return "ssrn"
    if "arxiv.org" in u:
        return "arxiv"
    if u.startswith("https://doi.org") or "doi.org" in u:
        return "doi"
    if u.endswith(".pdf"):
        return "pdf"
    if "github.com" in u:
        return "repo"
    if any(d in u for d in ("sciencedirect", "tandfonline", "degruyter", "worldscientific", "lincolninst", "cefargentina", "caf.com", "worldbank.org", "palgrave.com")):
        return "venue"
    return "other"


def slugify(text: str, maxlen: int = 60) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text[:maxlen].strip("-") or "entry"


def parse_entry(li, section: str, topic: str | None, order: int | None) -> dict:
    li_copy = BeautifulSoup(str(li), "html.parser")
    details = li_copy.find("details")
    abstract = ""
    if details:
        p = details.find("p")
        abstract = p.get_text(" ", strip=True) if p else ""
        details.decompose()

    keywords: list[str] = []
    if abstract:
        abstract = SPACE_BEFORE_LABEL_RE.sub(r" \1", abstract)
        kw_match = KEYWORDS_RE.search(abstract)
        if kw_match:
            abstract = abstract[: kw_match.start()].strip(" .*\\")
            for group in kw_match.groups():
                if group:
                    for k in re.split(r"[,;]", group):
                        k = k.strip(" .*\\")
                        if k:
                            keywords.append(k)

    links = []
    for a in li_copy.find_all("a"):
        href = a.get("href")
        if not href:
            continue
        label = a.get_text(" ", strip=True) or href
        links.append({"label": label, "url": href, "kind": classify_link(href)})

    headline = li_copy.get_text(" ", strip=True)

    year_match = YEAR_RE.match(headline)
    year = int(year_match.group(1)) if year_match else None

    quote_match = QUOTE_RE.search(headline)
    if quote_match:
        title = quote_match.group(1).strip()
    else:
        # fall back to first link text, else first ~100 chars
        title = links[0]["label"] if links else headline[:100]

    with_match = WITH_RE.search(headline)
    authors: list[str] = []
    if with_match:
        raw = with_match.group(1)
        raw = re.sub(r"\band\b", ",", raw, flags=re.IGNORECASE)
        authors = [a.strip(" .") for a in raw.split(",") if a.strip(" .")]

    needs_review = (
        not links
        or (section != "working-paper" and not year_match)
        or (not quote_match and not links)
    )

    entry_id = f"{section}-{slugify(title)}"
    if year:
        entry_id = f"{year}-{slugify(title)}"

    return {
        "id": entry_id,
        "title": title,
        "authors": authors,
        "year": year,
        "order": order,
        "section": section,
        "topic": topic,
        "venue": None,
        "links": links,
        "abstract": abstract or None,
        "keywords": keywords,
        "needsReview": needs_review,
        "_raw": headline,
    }


def main() -> None:
    html = SRC_HTML.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    write = soup.find("div", id="write")
    children = [c for c in write.children if getattr(c, "name", None)]

    entries = []
    section = None
    topic = None
    seen_first_h1 = False
    working_paper_order = 0

    for el in children:
        if el.name == "h1":
            seen_first_h1 = True
            section = SECTION_MAP.get(el.get_text(strip=True).upper())
            topic = None
            continue
        if not seen_first_h1:
            continue  # skip the TOC list before the first h1
        if el.name == "p":
            text = el.get_text(" ", strip=True)
            if section == "previous-work" and text and len(text) < 60 and not el.find("a"):
                topic = text
            continue
        if el.name == "ul" and section:
            for li in el.find_all("li", recursive=False):
                # The page states working papers are listed "In order of
                # most recent revision" -- capture that document order as
                # an explicit field rather than relying on array position.
                order = working_paper_order if section == "working-paper" else None
                entries.append(parse_entry(li, section, topic, order))
                if section == "working-paper":
                    working_paper_order += 1

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")

    review_count = sum(1 for e in entries if e["needsReview"])
    print(f"Wrote {len(entries)} publication entries to {OUT_JSON}")
    print(f"{review_count} entries flagged needsReview=true")
    by_section = {}
    for e in entries:
        by_section[e["section"]] = by_section.get(e["section"], 0) + 1
    print("By section:", by_section)


if __name__ == "__main__":
    main()

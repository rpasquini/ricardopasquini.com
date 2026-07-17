# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "beautifulsoup4",
#   "markdownify",
# ]
# ///
"""Convert the WordPress WXR export into Astro content collection files.

Usage: uv run scripts/convert_wxr.py
"""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md

REPO_ROOT = Path(__file__).resolve().parent.parent
BLOG_ROOT = REPO_ROOT.parent
XML_PATH = BLOG_ROOT / "ricardoapasquini.WordPress.2026-07-12.xml"
POSTS_OUT = REPO_ROOT / "src" / "content" / "posts"
PAGES_OUT = REPO_ROOT / "src" / "content" / "pages-raw"  # raw extracted HTML for hand-conversion

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
}

PATH_KEY_RE = re.compile(r"(\d{4}/\d{2}/[^/?#]+\.[A-Za-z0-9]+)$")


def media_key_from_url(url: str) -> str | None:
    m = PATH_KEY_RE.search(urlparse(url).path)
    return m.group(1) if m else None


def rewrite_media_urls(soup: BeautifulSoup) -> None:
    for tag, attr in (("img", "src"), ("a", "href")):
        for el in soup.find_all(tag):
            url = el.get(attr)
            if not url or not url.startswith("http"):
                continue
            key = media_key_from_url(url)
            if key:
                el[attr] = f"/media/{key}"


def yaml_escape(value: str) -> str:
    return value.replace('"', '\\"')


def frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, list):
            if v:
                items = ", ".join(f'"{yaml_escape(x)}"' for x in v)
                lines.append(f"{k}: [{items}]")
            else:
                lines.append(f"{k}: []")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        else:
            lines.append(f'{k}: "{yaml_escape(str(v))}"')
    lines.append("---")
    return "\n".join(lines)


def slugify_fallback(link: str) -> str:
    path = urlparse(link).path.strip("/")
    return path.split("/")[-1] or "post"


def clean_slug(raw_slug: str) -> str:
    """Decode percent-encoding, then strip anything that isn't URL-safe
    (older posts sometimes have emoji baked into wp:post_name)."""
    decoded = unquote(raw_slug)
    ascii_only = re.sub(r"[^a-zA-Z0-9]+", "-", decoded).strip("-").lower()
    return ascii_only or raw_slug


def convert_posts(items: list[ET.Element]) -> list[tuple[str, str]]:
    """Returns a list of (old_slug, new_slug) pairs where the slug changed,
    for the redirect map."""
    POSTS_OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    redirects = []
    for it in items:
        pt = it.find("wp:post_type", NS)
        st = it.find("wp:status", NS)
        if pt is None or pt.text != "post" or st is None or st.text != "publish":
            continue

        title = (it.findtext("title") or "").strip()
        link = it.findtext("link") or ""
        post_name = it.findtext("wp:post_name", default="", namespaces=NS)
        raw_slug = post_name or slugify_fallback(link)
        slug = clean_slug(raw_slug)
        if slug != raw_slug:
            redirects.append((raw_slug, slug))
        date_raw = it.findtext("wp:post_date", default="", namespaces=NS)
        date = date_raw.split(" ")[0] if date_raw else ""
        categories = [c.text for c in it.findall("category") if c.get("domain") == "category"]
        tags = [c.text for c in it.findall("category") if c.get("domain") == "post_tag"]
        excerpt = (it.findtext("excerpt:encoded", default="", namespaces=NS) or "").strip()

        content_el = it.find("content:encoded", NS)
        content_html = content_el.text if content_el is not None and content_el.text else ""

        soup = BeautifulSoup(content_html, "html.parser")
        rewrite_media_urls(soup)
        body_md = html_to_md(str(soup), heading_style="ATX").strip()

        meta = {
            "title": title,
            "date": date,
            "slug": slug,
            "lang": "es",
            "categories": categories,
            "tags": tags,
            "excerpt": excerpt[:300],
            "draft": False,
        }

        out_path = POSTS_OUT / f"{slug}.md"
        out_path.write_text(frontmatter(meta) + "\n\n" + body_md + "\n", encoding="utf-8")
        count += 1
    print(f"Wrote {count} posts to {POSTS_OUT}")
    return redirects


def extract_raw_pages(items: list[ET.Element], page_ids: dict[str, str]) -> None:
    """Dump raw content:encoded for the pages that need hand-conversion (About/Teaching/Home)."""
    PAGES_OUT.mkdir(parents=True, exist_ok=True)
    id_to_item = {}
    for it in items:
        pid = it.findtext("wp:post_id", default="", namespaces=NS)
        if pid in page_ids:
            id_to_item[pid] = it

    for pid, label in page_ids.items():
        it = id_to_item.get(pid)
        if it is None:
            print(f"WARNING: page id {pid} ({label}) not found")
            continue
        content_el = it.find("content:encoded", NS)
        html = content_el.text if content_el is not None and content_el.text else ""
        soup = BeautifulSoup(html, "html.parser")
        rewrite_media_urls(soup)
        (PAGES_OUT / f"{label}.html").write_text(str(soup), encoding="utf-8")
        (PAGES_OUT / f"{label}.md").write_text(html_to_md(str(soup), heading_style="ATX"), encoding="utf-8")
    print(f"Wrote raw + markdown page dumps to {PAGES_OUT}")


def main() -> None:
    tree = ET.parse(XML_PATH)
    items = tree.getroot().find("channel").findall("item")

    redirects = convert_posts(items)
    extract_raw_pages(items, {"804": "about", "259": "teaching", "2215": "home", "114": "publications-raw"})

    # Redirects needed because the source slug wasn't URL-safe, plus the
    # deliberate About URL cleanup (frontpage-mytest -> about) and the
    # dropped standalone pages redirecting home.
    all_redirects = [(old, new) for old, new in redirects] + [
        ("frontpage-mytest", "about"),
    ]
    # Note: "an-indebtedness-atlas-for-argentina" is deliberately excluded here
    # even though its WXR *page* (id 2201) is dropped: a separate published
    # *post* (id 2212) uses the exact same slug and IS kept, so that URL must
    # keep serving the post, not redirect to home.
    dropped_pages = [
        "entrepreneurialnetworks",
        "presentaciones",
        "grupo-de-evaluacion-de-impacto",
        "526-2",
    ]
    redirects_path = REPO_ROOT / "redirects.json"
    redirects_path.write_text(
        json.dumps(
            {
                "slug_fixes": [{"from": o, "to": n} for o, n in all_redirects],
                "dropped_pages_to_home": dropped_pages,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote redirect map ({len(all_redirects)} slug fixes) to {redirects_path}")


if __name__ == "__main__":
    main()

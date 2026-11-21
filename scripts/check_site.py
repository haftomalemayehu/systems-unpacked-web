#!/usr/bin/env python3
"""Dependency-free static website source checks (not a browser/security audit)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PAGES = sorted(ROOT.rglob("index.html"))
SKIP = {".git", ".github"}
BASE = "https://systems-unpacked.com/"
errors = []

class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = False
        self.h1 = 0
        self.description = False
        self.canonical = []
        self.links = []
        self.ids = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"): self.ids.append(a["id"])
        if tag == "title": self.title = True
        if tag == "h1": self.h1 += 1
        if tag == "meta" and a.get("name") == "description" and a.get("content"): self.description = True
        if tag == "link" and a.get("rel") == "canonical": self.canonical.append(a.get("href", ""))
        for attr in ("href", "src"):
            if attr in a and tag in ("a", "link", "img", "script", "iframe", "source"):
                self.links.append(a[attr])

for page in PAGES:
    if any(part in SKIP for part in page.parts): continue
    html = page.read_text(encoding="utf-8")
    parser = Inspector()
    parser.feed(html)
    for element_id in sorted(set(parser.ids)):
        if parser.ids.count(element_id) > 1:
            errors.append(f"{page}: duplicate HTML id: {element_id}")
    expected = BASE + ("" if page.parent == ROOT else page.parent.relative_to(ROOT).as_posix() + "/")
    if not parser.title: errors.append(f"{page}: missing title")
    if not parser.description: errors.append(f"{page}: missing meta description")
    if parser.h1 != 1: errors.append(f"{page}: expected one h1, found {parser.h1}")
    if parser.canonical != [expected]: errors.append(f"{page}: canonical should be {expected}")
    for link in parser.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc or link.startswith(("#", "mailto:", "tel:", "data:")): continue
        target = unquote(parsed.path)
        dest = ROOT / target.lstrip("/") if target.startswith("/") else page.parent / target
        dest = dest.resolve()
        if not dest.is_relative_to(ROOT.resolve()):
            errors.append(f"{page}: path escapes site root: {link}")
        elif not dest.is_file() and not (dest.is_dir() and (dest / "index.html").is_file()):
            errors.append(f"{page}: missing local target: {link}")
        if parsed.fragment and not parsed.path and not re.search(r'id=["\']' + re.escape(parsed.fragment) + r'["\']', html):
            errors.append(f"{page}: missing fragment target: {link}")

for required in ("robots.txt", "sitemap.xml"):
    if not (ROOT / required).is_file(): errors.append(f"missing {required}")
try:
    tree = ET.parse(ROOT / "sitemap.xml")
    urls = [e.text for e in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    expected_urls = {BASE + ("" if p.parent == ROOT else p.parent.relative_to(ROOT).as_posix() + "/") for p in PAGES}
    if set(urls) != expected_urls: errors.append("sitemap URLs differ from site pages")
except (ET.ParseError, OSError) as exc:
    errors.append(f"sitemap XML error: {exc}")

if errors:
    print("\n".join("FAIL: " + e for e in errors))
    sys.exit(1)
print(f"PASS: {len(PAGES)} HTML pages, internal links/assets, metadata, and sitemap")

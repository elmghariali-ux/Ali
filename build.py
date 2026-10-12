#!/usr/bin/env python3
"""Build the ZAYA site: one real HTML page per room, from src/site.html.

Each page shows its own room as plain HTML (what Google reads). The other rooms
travel along inside <template> tags, so moving between rooms never reloads the
page and the music never stops. Run:  python3 build.py
"""
import re, html, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://zayaritual.com"
src = (ROOT / "src/site.html").read_text()
OUT = {"ritual": "index.html", "nights": "nights.html", "signal": "signal.html",
       "request": "request.html", "about": "about.html"}

a = src.index("<main>\n") + len("<main>\n")
b = src.index("</main>")
chunks = [c for c in re.split(r'(?=<div class="room" )', src[a:b]) if c.strip()]
rooms = []
for c in chunks:
    c = c.rstrip()
    head_end = c.index(">") + 1
    tag, inner = c[:head_end], c[head_end:]
    assert inner.endswith("</div>"), tag
    inner = inner[: -len("</div>")]
    attrs = dict(re.findall(r'data-([a-z]+)="([^"]*)"', tag))
    rooms.append((attrs, tag.replace(" hidden>", ">"), inner))

def esc(v):  # attribute values are already HTML-escaped in the source
    return v

for attrs, tag, _ in rooms:
    name = attrs["room"]
    title, desc, path = attrs["title"], attrs["desc"], attrs["path"]
    url = SITE + path
    page = src
    page = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", page, count=1)
    page = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', page, count=1)
    page = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', page, count=1)
    page = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(title)}">', page, count=1)
    page = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(desc)}">', page, count=1)
    page = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', page, count=1)
    body = []
    for a2, t2, inner2 in rooms:
        if a2["room"] == name:
            body.append(f"{t2}{inner2}</div>")
        else:
            body.append(f"{t2[:-1]} hidden><template>{inner2}</template></div>")
    page = page[: page.index("<main>\n") + len("<main>\n")] + "\n\n".join(body) + "\n" + page[page.index("</main>"):]
    (ROOT / OUT[name]).write_text(page)
    print(f"{OUT[name]:14} {path:10} {len(page)//1024} KB  {html.unescape(title)}")

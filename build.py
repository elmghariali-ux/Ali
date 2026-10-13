#!/usr/bin/env python3
"""Build the ZAYA site from src/site.html.

The home page is the whole ritual in one scroll. /nights, /signal and /request
are the same night, opened at that moment (handy for Instagram links); they
point Google to the home page. /about (The House) is its own page. Rooms that
aren't shown travel along inside <template>, so moving between them never
reloads and the music never stops. Run:  python3 build.py
"""
import re, html, pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://zayaritual.com"
src = (ROOT / "src/site.html").read_text()

PAGES = [  # file, room shown, title, description, canonical path
    ("index.html", "ritual", "ZAYA — Afro House Ritual in Barcelona",
     "ZAYA is an Afro House ritual in Barcelona. Edition III: Saturday 21 November 2026. Tickets are released to invited guests only — request an invitation.", "/"),
    ("nights.html", "ritual", "The Nights — ZAYA at Hotel El Palace, Barcelona",
     "Editions I and II of ZAYA at Hotel El Palace, Barcelona: two Afro House nights, both sold out, with no advertising.", "/"),
    ("signal.html", "ritual", "Edition III · Saturday 21 November 2026 — ZAYA Barcelona",
     "ZAYA Edition III: Saturday 21 November 2026 in Barcelona. Afro House and Afrotech. Tickets for invited guests only; the venue is revealed soon.", "/"),
    ("request.html", "ritual", "Request an invitation — ZAYA Barcelona",
     "Request an invitation to ZAYA Edition III, an Afro House night in Barcelona on Saturday 21 November 2026. Every request is read by hand.", "/"),
    ("about.html", "about", "About ZAYA — Afro House & Afrotech in Barcelona",
     "Barcelona had no true home for Afro House, so we built one. ZAYA is an Afro House and Afrotech ritual curated by Argana. 18+, by invitation.", "/about"),
]

a = src.index("<main>\n") + len("<main>\n")
b = src.index("</main>")
rooms = []
for c in [c for c in re.split(r'(?=<div class="room" )', src[a:b]) if c.strip()]:
    c = c.rstrip()
    head_end = c.index(">") + 1
    tag, inner = c[:head_end].replace(" hidden>", ">"), c[head_end:]
    assert inner.endswith("</div>"), tag
    rooms.append((re.search(r'data-room="([^"]+)"', tag).group(1), tag, inner[: -len("</div>")]))

for fname, show, title, desc, canon in PAGES:
    t, d, url = html.escape(title, quote=True), html.escape(desc, quote=True), SITE + canon
    page = src
    page = re.sub(r"<title>.*?</title>", f"<title>{t}</title>", page, count=1)
    page = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{d}">', page, count=1)
    page = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', page, count=1)
    page = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{t}">', page, count=1)
    page = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{d}">', page, count=1)
    page = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', page, count=1)
    body = [f"{tag}{inner}</div>" if name == show else f"{tag[:-1]} hidden><template>{inner}</template></div>"
            for name, tag, inner in rooms]
    page = page[: page.index("<main>\n") + len("<main>\n")] + "\n\n".join(body) + "\n" + page[page.index("</main>"):]
    (ROOT / fname).write_text(page)
    print(f"{fname:13} {len(page)//1024} KB  {title}")

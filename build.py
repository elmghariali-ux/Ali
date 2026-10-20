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
import importlib.util as _iu
_sp = _iu.spec_from_file_location('legal0', ROOT / 'src/legal.py'); _lg = _iu.module_from_spec(_sp); _sp.loader.exec_module(_lg)
src = src.replace('{{OWNER_NAME}}', html.escape(_lg.OWNER['name']) if _lg.OWNER['name'].strip() else 'ZAYA')

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


# ---------- legal pages: /legal, /privacy, /cookies (English + Spanish) ----------
import importlib.util
spec = importlib.util.spec_from_file_location("legal", ROOT / "src/legal.py")
legal = importlib.util.module_from_spec(spec); spec.loader.exec_module(legal)

pending = [k for k, v in legal.OWNER.items() if not v.strip()]
fill = {k: (html.escape(v) if v.strip() else '<span class="pending">[pending]</span>') for k, v in legal.OWNER.items()}

LEGAL_TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://zayaritual.com/{slug}">
{robots}<meta name="theme-color" content="#070404">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23070404'/%3E%3Ccircle cx='16' cy='16' r='5' fill='%23B3261E'/%3E%3C/svg%3E">
<link rel="preload" href="/fonts/jost-latin-300-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/fonts/fonts.css">
<style>
:root{{--bg:#070404;--ink:#f3ebe4;--soft:#d6cac1;--mute:#a3958d;--hot:#ff6b4d;--accent:#B3261E}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:'Jost',system-ui,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased}}
a{{color:inherit;text-decoration:none;transition:color .3s}}a:hover{{color:var(--hot)}}
::selection{{background:var(--accent);color:#fff}}
:focus-visible{{outline:1px solid var(--hot);outline-offset:4px}}
.cap{{font-size:11px;letter-spacing:.42em;text-transform:uppercase}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:12px 5vw;color:var(--soft)}}
.top a{{min-height:44px;display:inline-flex;align-items:center}}
.mark{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:17px;letter-spacing:.55em;padding-left:.55em;color:var(--ink)}}
.lang{{display:flex;gap:22px}}
main{{max-width:700px;margin:0 auto;padding:12vh 5vw 10vh}}
section+section{{margin-top:14vh;padding-top:12vh;border-top:1px solid rgba(233,225,218,.1)}}
.kicker{{margin:0 0 22px;color:var(--hot);text-align:center}}
h1{{margin:0;text-align:center;font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(40px,6vw,68px);line-height:1.08}}
.upd{{margin:22px 0 9vh;text-align:center;color:#8f817a}}
.lede{{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:clamp(21px,2.2vw,25px);line-height:1.55;color:var(--soft);margin:0 0 6vh}}
h2{{margin:52px 0 16px;font-size:11px;font-weight:400;letter-spacing:.36em;text-transform:uppercase;color:var(--hot)}}
p,li{{font-size:15.5px;line-height:1.85;color:#cfc2b9}}
p{{margin:0 0 1em}}
ul{{margin:0 0 1em;padding-left:1.1em}}li{{margin:0 0 .6em}}li::marker{{color:var(--accent)}}
b{{font-weight:400;color:var(--ink)}}
main a{{border-bottom:1px solid rgba(255,107,77,.45)}}
dl.id{{margin:20px 0 22px;border-top:1px solid rgba(233,225,218,.12)}}
dl.id div{{display:flex;gap:20px;padding:13px 0;border-bottom:1px solid rgba(233,225,218,.12)}}
dl.id dt{{flex:none;width:110px;padding-top:.3em;font-size:10px;letter-spacing:.32em;text-transform:uppercase;color:#8f817a}}
dl.id dd{{margin:0;font-size:15.5px;line-height:1.6;color:var(--ink);word-break:break-word}}
dl.id dd a{{border:0}}
.pending{{color:var(--hot)}}
footer{{padding:28px 5vw 36px;border-top:1px solid rgba(233,225,218,.08);display:flex;flex-wrap:wrap;justify-content:space-between;gap:14px 24px;color:#8f817a}}
footer nav{{display:flex;flex-wrap:wrap;gap:8px 26px}}
footer a{{min-height:44px;display:inline-flex;align-items:center}}
footer a[aria-current]{{color:var(--ink)}}
@media (max-width:560px){{.cap{{letter-spacing:.3em}}dl.id div{{flex-direction:column;gap:4px}}dl.id dt{{width:auto;padding:0}}}}
</style>
</head>
<body>
<header class="top cap">
  <a class="mark" href="/" aria-label="ZAYA, home">ZAYA</a>
  <nav class="lang" aria-label="Language"><a href="#en" hreflang="en">English</a><a href="#es" hreflang="es">Español</a></nav>
</header>
<main>
<section id="en" lang="en">
  <p class="cap kicker">ZAYA · {kick_en}</p>
  <h1>{h_en}</h1>
  <p class="cap upd">Last updated · {upd_en}</p>
  {en}
</section>
<section id="es" lang="es">
  <p class="cap kicker">ZAYA · {kick_es}</p>
  <h1>{h_es}</h1>
  <p class="cap upd">Última actualización · {upd_es}</p>
  {es}
</section>
</main>
<footer class="cap">
  <a href="/">ZAYA · The Ritual</a>
  <nav aria-label="Legal">{links}</nav>
</footer>
<script defer src="/_vercel/insights/script.js"></script>
</body>
</html>
"""
LINKS = [("legal", "Legal notice"), ("privacy", "Privacy"), ("cookies", "Cookies")]
for slug, pg in legal.PAGES.items():
    links = "".join(f'<a href="/{s}"{" aria-current=\"page\"" if s == slug else ""}>{n}</a>' for s, n in LINKS)
    out = LEGAL_TPL.format(
        title=pg["title"], desc=html.escape(pg["desc"], quote=True), slug=slug,
        robots='<meta name="robots" content="noindex">\n' if pending else "",
        kick_en="Legal", kick_es="Legal", h_en=pg["h_en"], h_es=pg["h_es"],
        upd_en=legal.UPDATED_EN, upd_es=legal.UPDATED_ES,
        en=pg["en"].format(**fill), es=pg["es"].format(**fill), links=links)
    (ROOT / f"{slug}.html").write_text(out)
    print(f"{slug + '.html':13} legal page")
if pending:
    print("WARNING: owner details pending in src/legal.py ->", ", ".join(pending), "— do NOT publish to main.")

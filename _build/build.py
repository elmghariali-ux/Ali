"""Builds the static multilingual Alma site: / (es), /en/, /fr/, FAQ pages, sitemap, robots."""
import copy, json, os, re, sys
from bs4 import BeautifulSoup

SRC = sys.argv[1]          # template with data-es / data-en / data-fr
OUT = sys.argv[2]          # repo root
SITE = "https://almasocial.club"
LANGS = ["es", "en", "fr"]
PATH = {"es": "/", "en": "/en/", "fr": "/fr/"}
FAQ_PATH = {"es": "/faq/", "en": "/en/faq/", "fr": "/fr/faq/"}

META = {
    "es": ("Alma Social Club — Asociación privada en Barcelona",
           "Alma Social Club es una asociación privada de personas adultas en L'Hospitalet de Llobregat, Barcelona. Un espacio para socios con murales, neón y buena compañía. Abierto todos los días de 10:00 a 22:00. Solo +18."),
    "en": ("Alma Social Club — Private members' club in Barcelona",
           "Alma Social Club is a private association of adults in L'Hospitalet de Llobregat, Barcelona. A members-only space with murals, neon light and good company. Open daily 10:00–22:00. Adults 18+ only."),
    "fr": ("Alma Social Club — Club privé à Barcelone",
           "Alma Social Club est une association privée de personnes majeures à L'Hospitalet de Llobregat, Barcelone. Un espace réservé aux membres, avec fresques, néons et bonne compagnie. Ouvert tous les jours de 10h à 22h. +18 uniquement."),
}
FAQ_META = {
    "es": ("Preguntas frecuentes — Alma Social Club Barcelona", "Horario, dirección, cómo funciona la membresía y otras preguntas frecuentes sobre Alma Social Club, asociación privada en Barcelona."),
    "en": ("FAQ — Alma Social Club Barcelona", "Opening hours, address, how membership works and other frequently asked questions about Alma Social Club, a private association in Barcelona."),
    "fr": ("FAQ — Alma Social Club Barcelone", "Horaires, adresse, fonctionnement de l'adhésion et autres questions fréquentes sur Alma Social Club, association privée à Barcelone."),
}
OGLOCALE = {"es": "es_ES", "en": "en_GB", "fr": "fr_FR"}
STATUS = {
    "es": ("ABIERTO AHORA", "CERRADO · ABRE A LAS 10:00"),
    "en": ("OPEN NOW", "CLOSED · OPENS 10:00"),
    "fr": ("OUVERT", "FERMÉ · OUVRE À 10H"),
}
FAQ_LABEL = {"es": "FAQ", "en": "FAQ", "fr": "FAQ"}

FAQ = {
 "es": [
  ("¿Qué es Alma Social Club?", "Alma Social Club es una asociación privada de personas adultas en L'Hospitalet de Llobregat (Barcelona). Es un espacio para socios pensado para encontrarse, desconectar y hacer comunidad."),
  ("¿Dónde está?", "En Carrer Dos de Maig, 7, 08904 L'Hospitalet de Llobregat, Barcelona. Puedes abrir la ruta en Google Maps desde la página de inicio."),
  ("¿Cuál es el horario?", "Abrimos todos los días, de lunes a domingo, de 10:00 a 22:00."),
  ("¿Quién puede hacerse socio?", "Personas mayores de 18 años con un documento de identidad original y en vigor (DNI, NIE o pasaporte) que lean y acepten los estatutos y el reglamento interno. La membresía es personal e intransferible."),
  ("¿Puedo entrar sin ser socio?", "El acceso al local está reservado a los socios. Las condiciones para hacerse socio se explican en persona en el club."),
  ("¿En qué idiomas atendéis?", "El equipo atiende en español y en inglés. Esta web también está disponible en francés."),
  ("¿Esta web vende algo?", "No. Esta web es exclusivamente informativa y no constituye publicidad ni oferta de ningún producto."),
  ("¿Cómo puedo contactar?", "Por Instagram, en @alma.csc.barcelona, o pasando por el club en horario de apertura."),
 ],
 "en": [
  ("What is Alma Social Club?", "Alma Social Club is a private association of adults in L'Hospitalet de Llobregat (Barcelona). It's a members-only space to meet, unwind and build community."),
  ("Where is it?", "Carrer Dos de Maig, 7, 08904 L'Hospitalet de Llobregat, Barcelona. You can open directions in Google Maps from the home page."),
  ("What are the opening hours?", "We're open every day, Monday to Sunday, from 10:00 to 22:00."),
  ("Who can become a member?", "Adults aged 18 or over with an original, valid ID (national ID, NIE or passport) who read and accept the association's bylaws and house rules. Membership is personal and non-transferable."),
  ("Can I visit without being a member?", "Access to the premises is reserved for members. The conditions for joining are explained in person at the club."),
  ("Which languages do you speak?", "The team speaks Spanish and English. This website is also available in French."),
  ("Does this website sell anything?", "No. This website is for information only and does not constitute advertising or an offer of any product."),
  ("How can I get in touch?", "On Instagram at @alma.csc.barcelona, or by stopping by the club during opening hours."),
 ],
 "fr": [
  ("Qu'est-ce qu'Alma Social Club ?", "Alma Social Club est une association privée de personnes majeures à L'Hospitalet de Llobregat (Barcelone). C'est un espace réservé aux membres pour se retrouver, décompresser et créer du lien."),
  ("Où se trouve le club ?", "Carrer Dos de Maig, 7, 08904 L'Hospitalet de Llobregat, Barcelone. Vous pouvez ouvrir l'itinéraire Google Maps depuis la page d'accueil."),
  ("Quels sont les horaires ?", "Nous sommes ouverts tous les jours, du lundi au dimanche, de 10h à 22h."),
  ("Qui peut devenir membre ?", "Les personnes de 18 ans et plus, munies d'une pièce d'identité originale et en cours de validité (carte d'identité, NIE ou passeport), qui lisent et acceptent les statuts et le règlement intérieur. L'adhésion est personnelle et non transférable."),
  ("Puis-je venir sans être membre ?", "L'accès au local est réservé aux membres. Les conditions d'adhésion sont expliquées sur place, au club."),
  ("Quelles langues parlez-vous ?", "L'équipe parle espagnol et anglais. Ce site est aussi disponible en français."),
  ("Ce site vend-il quelque chose ?", "Non. Ce site a un caractère purement informatif et ne constitue ni une publicité ni une offre de produit."),
  ("Comment vous contacter ?", "Sur Instagram, @alma.csc.barcelona, ou en passant au club pendant les horaires d'ouverture."),
 ],
}
FAQ_HEAD = {"es": ("Preguntas", "frecuentes"), "en": ("Frequently asked", "questions"), "fr": ("Questions", "fréquentes")}
BACK = {"es": "← Volver al inicio", "en": "← Back to home", "fr": "← Retour à l'accueil"}

LANG_CSS = """
.langs{display:inline-flex;gap:2px;padding:3px;border:1px solid var(--line);border-radius:99px}
.langs a{font:600 12px var(--m);letter-spacing:.1em;padding:6px 10px;border-radius:99px;color:var(--mute);transition:.2s}
.langs a:hover{color:var(--ink)}.langs a.on{background:rgba(53,182,255,.18);color:var(--ink)}
.gb .langs{margin-top:24px}
.faq{max-width:860px;margin:56px auto 0;display:grid;gap:12px}
.faq details{border:1px solid var(--line);border-radius:20px;background:var(--glass);backdrop-filter:blur(14px);padding:22px 26px}
.faq summary{cursor:pointer;font:700 clamp(17px,2vw,21px)/1.35 var(--b);list-style:none;display:flex;justify-content:space-between;gap:16px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font:400 26px/1 var(--m);color:var(--sky);transition:transform .3s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{color:var(--mute);margin-top:12px}
.faqhero{padding-top:150px}
"""


def langs_html(lang, paths):
    return '<span class="langs">' + "".join(
        f'<a href="{paths[l]}" hreflang="{l}" lang="{l}"{" class=\"on\" aria-current=\"page\"" if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS) + "</span>"


def head_tags(lang, paths, meta, jsonld):
    title, desc = meta[lang]
    url = SITE + paths[lang]
    alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE + paths[l]}">' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{SITE + paths["es"]}">'
    og_alt = "".join(f'<meta property="og:locale:alternate" content="{OGLOCALE[l]}">' for l in LANGS if l != lang)
    return (f'<title>{title}</title>'
            f'<meta name="description" content="{desc}">'
            f'<link rel="canonical" href="{url}">{alts}'
            f'<meta name="robots" content="index,follow,max-image-preview:large">'
            f'<meta property="og:type" content="website"><meta property="og:site_name" content="Alma Social Club">'
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">'
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/og.jpg">'
            f'<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            f'<meta property="og:locale" content="{OGLOCALE[lang]}">{og_alt}'
            f'<meta name="twitter:card" content="summary_large_image">'
            f'<meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}">'
            f'<meta name="twitter:image" content="{SITE}/assets/og.jpg">'
            f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>')


def business(lang):
    return {
        "@context": "https://schema.org", "@type": "LocalBusiness", "@id": SITE + "/#club",
        "name": "Alma Social Club", "url": SITE + PATH[lang], "description": META[lang][1],
        "image": SITE + "/assets/og.jpg", "logo": SITE + "/assets/mascot.webp",
        "address": {"@type": "PostalAddress", "streetAddress": "Carrer Dos de Maig, 7",
                    "addressLocality": "L'Hospitalet de Llobregat", "postalCode": "08904",
                    "addressRegion": "Barcelona", "addressCountry": "ES"},
        "geo": {"@type": "GeoCoordinates", "latitude": 41.3743185, "longitude": 2.114596},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "10:00", "closes": "22:00"}],
        "sameAs": ["https://www.instagram.com/alma.csc.barcelona/"],
        "inLanguage": lang,
    }


def localize(soup, lang):
    for other in LANGS:
        if other == lang:
            continue
        for el in soup.select(f"[data-{other}]"):
            el.decompose()
    for el in soup.select(f"[data-{lang}]"):
        del el[f"data-{lang}"]
    soup.html["lang"] = lang


def fix_common(html, lang, paths):
    # absolute asset paths so subfolder pages work
    html = html.replace('"assets/', '"/assets/').replace("(assets/", "(/assets/").replace("'assets/", "'/assets/")
    # language toggles -> real links
    html = re.sub(r'<button[^>]*data-lang[^>]*>ES / EN</button>', langs_html(lang, paths), html)
    return html


def fix_js(html, lang):
    # drop runtime language switching
    html = re.sub(r"/\* language \*/.*?\n\n", "", html, flags=re.S)
    html = html.replace("var L=g('alma-lang'); if(L)R.lang=L; else if(!/^(es|ca)/i.test(navigator.language||'es'))R.lang='en';", "")
    o, c = STATUS[lang]
    html = re.sub(r"\$\('#stt'\)\.textContent=R\.lang==='es'\?.*?\}\n",
                  f"$('#stt').textContent=o?'{o}':'{c}'}}\n", html, flags=re.S)
    html = html.replace("['#manES','#manEN'].forEach(function(id){var p=$(id),",
                        "document.querySelectorAll('.man .big').forEach(function(p){var ")
    html = html.replace(r"hl=/^(frecuencia\.|frequency\.|tuyo\.|yours\.)$/i;",
                        r"hl=/^(frecuencia\.|frequency\.|fréquence\.|tuyo\.|yours\.|ressemble\.)$/i;")
    html = re.sub(r"document\.querySelectorAll\('\.man \[data-'.*?\.w'\)",
                  "document.querySelectorAll('.man .big .w')", html)
    return html


def add_nav_faq(soup, lang, faq_href, label):
    nl = soup.select_one(".nl")
    langs = nl.select_one(".langs") if nl else None
    a = soup.new_tag("a", href=faq_href)
    a.string = label
    if langs:
        langs.insert_before(a)


def build_home(tpl, lang):
    soup = BeautifulSoup(tpl, "html.parser")
    localize(soup, lang)
    head = soup.head
    for t in head.find_all(["title"]):
        t.decompose()
    for m in head.find_all("meta"):
        if m.get("name") in ("description",) or (m.get("property") or "").startswith("og:"):
            m.decompose()
    head.find("meta", attrs={"name": "viewport"}).insert_after(
        BeautifulSoup(head_tags(lang, PATH, META, business(lang)), "html.parser"))
    soup.style.append(LANG_CSS)
    html = fix_common(str(soup), lang, PATH)
    soup = BeautifulSoup(html, "html.parser")
    add_nav_faq(soup, lang, FAQ_PATH[lang], FAQ_LABEL[lang])
    # footer link to FAQ
    fb = soup.select_one(".fb .mono")
    if fb:
        fa = soup.new_tag("a", href=FAQ_PATH[lang]); fa.string = " · FAQ"; fb.append(fa)
    return fix_js(str(soup), lang)


def build_faq(home_html, lang):
    soup = BeautifulSoup(home_html, "html.parser")
    # head: swap meta
    head = soup.head
    for t in head.find_all("title"): t.decompose()
    for m in head.find_all(["meta", "link", "script"]):
        if m.name == "meta" and (m.get("name") in ("description", "twitter:title", "twitter:description") or (m.get("property") or "") in ("og:title", "og:description", "og:url")):
            m.decompose()
        elif m.name == "link" and m.get("rel") and (m["rel"][0] in ("canonical", "alternate")):
            m.decompose()
        elif m.name == "script" and m.get("type") == "application/ld+json":
            m.decompose()
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
              "mainEntity": [{"@type": "Question", "name": q,
                              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ[lang]]}
    tags = head_tags(lang, FAQ_PATH, FAQ_META, faq_ld)
    tags = re.sub(r'<meta name="robots"[^>]*>|<meta property="og:(type|site_name|image[^"]*|locale[^"]*)"[^>]*>|<meta name="twitter:(card|image)"[^>]*>', "", tags)
    head.find("meta", attrs={"name": "viewport"}).insert_after(BeautifulSoup(tags, "html.parser"))
    # language links point at FAQ variants
    for box in soup.select(".langs"):
        box.replace_with(BeautifulSoup(langs_html(lang, FAQ_PATH), "html.parser"))
    # nav links back to home anchors
    for a in soup.select(".nl a[href^='#']"):
        a["href"] = PATH[lang] + a["href"]
    soup.select_one(".logo")["href"] = PATH[lang]
    # body: keep gate, cursor, nav, footer; replace main content
    body = soup.body
    keep = {"gate", "cur", "nav"}
    for el in list(body.find_all(recursive=False)):
        if el.name in ("header", "section") or (el.name == "div" and "mqw" in (el.get("class") or [])):
            el.decompose()
    h1a, h1b = FAQ_HEAD[lang]
    items = "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>"
                    for i, (q, a) in enumerate(FAQ[lang]))
    sec = BeautifulSoup(
        f'<section class="faqhero"><div class="wrap">'
        f'<p class="ey mono"><a href="{PATH[lang]}">{BACK[lang]}</a></p>'
        f'<h1 style="font:800 clamp(38px,6.4vw,92px)/.98 var(--d);letter-spacing:-.035em">{h1a} <span class="chrome">{h1b}</span></h1>'
        f'<div class="faq">{items}</div></div></section>', "html.parser")
    soup.find("footer").insert_before(sec)
    html = str(soup)
    # strip home-only JS that would error on missing elements
    html = html.replace("<script>\n(function(){", "<script>\n(function(){var __faq=1;", 1)
    js_start = html.index("<script>\n(function(){var __faq=1;")
    js = f"""<script>
(function(){{
var B=document.body,$=function(s){{return document.querySelector(s)}};
function g(k){{try{{return localStorage.getItem(k)}}catch(e){{return null}}}}
function s(k,v){{try{{localStorage.setItem(k,v)}}catch(e){{}}}}
var gate=$('#gate');
function enter(){{gate.classList.add('off');B.classList.remove('locked');setTimeout(function(){{gate.hidden=true}},700)}}
if(g('alma-age')==='ok'){{gate.hidden=true;B.classList.remove('locked')}}
$('#gy').onclick=function(){{s('alma-age','ok');enter()}};
$('#gn').onclick=function(){{location.href='https://www.google.com'}};
var nav=$('#nav');nav.classList.add('s');
$('#yr').textContent=new Date().getFullYear();
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}})}},{{threshold:.15}});
document.querySelectorAll('.rv').forEach(function(el){{io.observe(el)}});
}})();
</script>"""
    end = html.index("</script>", js_start) + len("</script>")
    return html[:js_start] + js + html[end:]


def write(path, html):
    full = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write("<!doctype html>\n" + html.replace("<!DOCTYPE html>", "").replace("<!doctype html>", "").lstrip())
    print("wrote", full)


tpl = open(SRC).read()
for lang in LANGS:
    home = build_home(tpl, lang)
    write(PATH[lang], home)
    write(FAQ_PATH[lang], build_faq(home, lang))

urls = []
for paths in (PATH, FAQ_PATH):
    for l in LANGS:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{SITE + paths[x]}"/>' for x in LANGS)
        urls.append(f"<url><loc>{SITE + paths[l]}</loc>{alts}<changefreq>monthly</changefreq><priority>{'1.0' if paths is PATH and l == 'es' else '0.8'}</priority></url>")
open(os.path.join(OUT, "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
    + "".join(urls) + "</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("sitemap + robots done")

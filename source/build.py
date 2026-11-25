# -*- coding: utf-8 -*-
"""Genera la web estática multidioma de gecanor.com.

  python3 source/build.py            (necesita Python + playwright + Chrome)

Lee las páginas de source/pages/*.html (diseño del motor dc-runtime) y escribe en
gecanor-lab-web/:
  - una copia por idioma con su propia URL: /  (EN), /es/..., /ca/...
  - el contenido ya renderizado dentro del HTML (#ssr) para que buscadores e IA
    lo lean sin ejecutar JavaScript; al cargar, el motor lo sustituye por la
    versión interactiva
  - <head> con title/description por idioma, canonical, hreflang, Open Graph y
    datos estructurados (JSON-LD)
  - páginas legales (/legal, /cookies), sitemap.xml, robots.txt y llms.txt
"""
import html, json, os, re, sys, shutil, threading, http.server, functools, datetime
import markdown as md
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import (SITE, LANGS, PREFIX, LANG_CODE, OG_LOCALE, COMPANY, APP_PAGES, META,
                     ORG_DESC, SERVICES, FOOTER_LINKS, STATIC_PAGES, UPDATED, BACK,
                     OFFICE, HOME_H1, SERVICES_INTRO, FAQ, FAQ_TITLE, FAQ_LABEL)

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / 'source' / 'pages'
OUT = REPO / 'gecanor-lab-web'
VENDOR = Path(os.environ.get('GECANOR_VENDOR', '/home/claude/vendor'))
OG_IMAGE = SITE + '/assets/og-gecanor.jpg'
ALL_PAGES = {**APP_PAGES, **{k: v[0] for k, v in STATIC_PAGES.items()}}

sys.path.insert(0, str(Path(__file__).parent / 'articles'))
from articles import ARTICLES, AUTHOR
from covers import cover_name

ART_DIR = Path(__file__).parent / 'articles'
TODAY = os.environ.get('BUILD_DATE') or datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).date().isoformat()


def published(lang):
    """Artículos publicados en un idioma, del más reciente al más antiguo."""
    out = [a for a in ARTICLES if a['date'] <= TODAY and lang in a and (ART_DIR / f"{a['slug']}.{lang}.md").exists()]
    return sorted(out, key=lambda a: a['date'], reverse=True)


def art_path(a):
    return '/resources/' + a['slug']


def url(lang, path):
    p = PREFIX[lang] + path
    return SITE + (p or '/')


def local(lang, path):
    p = PREFIX[lang] + path
    return p or '/'


def out_file(lang, path):
    p = (PREFIX[lang] + path).strip('/')
    return OUT / p / 'index.html' if p else OUT / 'index.html'


# ------------------------------------------------------------------ head
def head(page, lang, extra_ld=None, meta=None, path=None, langs=None, og_type='website', image=None):
    title, desc = meta or META[page][lang]
    og_img = image or OG_IMAGE
    path = ALL_PAGES[page] if path is None else path
    langs = langs or LANGS
    canon = url(lang, path)
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{url(l, path)}">\n' for l in langs)
    if len(langs) > 1:
        alts += f'<link rel="alternate" hreflang="x-default" href="{url("en" if "en" in langs else langs[0], path)}">\n'
    org = {
        '@type': 'Organization', '@id': SITE + '/#org', 'name': COMPANY['brand'], 'legalName': COMPANY['legal'],
        'taxID': COMPANY['nif'], 'url': SITE + '/', 'logo': SITE + '/assets/logo-gecanor.png', 'image': OG_IMAGE,
        'email': COMPANY['email'], 'description': ORG_DESC[lang],
        'address': {'@type': 'PostalAddress', 'streetAddress': OFFICE['street'], 'addressLocality': OFFICE['city'],
                    'postalCode': OFFICE['zip'], 'addressCountry': 'ES'},
        'location': [
            {'@type': 'Place', 'name': 'Gecanor Barcelona', 'address': {'@type': 'PostalAddress', 'streetAddress': OFFICE['street'],
             'addressLocality': 'Barcelona', 'postalCode': OFFICE['zip'], 'addressCountry': 'ES'}},
            {'@type': 'Place', 'name': 'Gecanor Chengdu', 'address': {'@type': 'PostalAddress', 'streetAddress': 'Wanke Jiazhouwan V-Pai, 501',
             'addressLocality': 'Chengdu', 'postalCode': '610036', 'addressCountry': 'CN'}}],
        'sameAs': [COMPANY['instagram'], COMPANY['linkedin']],
        'areaServed': ['ES', 'EU', 'CN'],
        'knowsAbout': ['Cosmetic formulation', 'Nutricosmetics', 'Food supplements', 'Private label cosmetics',
                       'Contract manufacturing', 'Regulation (EC) No 1223/2009', 'Cosmetic packaging', 'Brand strategy'],
    }
    graph = [org,
             {'@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': COMPANY['brand'],
              'publisher': {'@id': SITE + '/#org'}, 'inLanguage': ['en', 'es', 'ca']},
             {'@type': 'WebPage', '@id': canon + '#webpage', 'url': canon, 'name': title, 'description': desc,
              'inLanguage': lang, 'isPartOf': {'@id': SITE + '/#website'}, 'about': {'@id': SITE + '/#org'}}]
    if extra_ld:
        graph += extra_ld
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('</', '<\\/')
    e = html.escape
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
{alts}<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{COMPANY['brand']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/gr.svg">
<script type="application/ld+json">{ld}</script>
<script src="/consent.js"></script>
'''


def service_ld(lang):
    return [{'@type': 'Service', 'name': s, 'serviceType': s, 'provider': {'@id': SITE + '/#org'},
             'areaServed': ['ES', 'EU'], 'url': url(lang, '/services') + (f'#s0{i}' if i else '')}
            for i, s in enumerate(SERVICES[lang])]


def faq_ld(lang):
    return [{'@type': 'FAQPage', '@id': url(lang, '') + '#faq', 'inLanguage': lang,
             'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
                            for q, a in FAQ[lang]]}]


MONO = "font-family:'IBM Plex Mono',ui-monospace,monospace"


def faq_html(lang):
    e = html.escape
    items = ''.join(
        f'<div style="display:grid;grid-template-columns:48px minmax(0,1fr);gap:6px 16px;padding:22px 0;border-top:1px solid #DAD9D4">'
        f'<span style="{MONO};font-size:12px;color:#6F6E69">{i + 1:02d}</span>'
        f'<div><h3 style="margin:0 0 8px;font-size:clamp(18px,1.6vw,22px);line-height:1.25;font-weight:600">{e(q)}</h3>'
        f'<p style="margin:0;max-width:72ch;font-size:16px;line-height:1.55;color:#3A3A38">{e(a)}</p></div></div>'
        for i, (q, a) in enumerate(FAQ[lang]))
    return (f'<section id="faq" style="padding:72px 24px 56px;border-top:1px solid #0B0B0B">'
            f'<div style="display:flex;justify-content:space-between;gap:16px;margin-bottom:20px;{MONO};font-size:12px;color:#6F6E69;text-transform:uppercase">'
            f'<span>{FAQ_LABEL[lang]}</span><span>{len(FAQ[lang]):02d}</span></div>'
            f'<h2 style="margin:0 0 28px;font-size:clamp(40px,7vw,96px);line-height:0.9;letter-spacing:-0.03em;text-transform:uppercase;font-weight:800">{FAQ_TITLE[lang]}</h2>'
            f'{items}</section>\n\n  ')


# ------------------------------------------------------------------ app pages
ASSET_RE = re.compile(r'(["\'(])\.\.?/(assets/|support\.js|i18n\.js|lab-i18n\.js)')


def transform(src, lang, page=''):
    P = PREFIX[lang]
    s = ASSET_RE.sub(r'\1/\2', src)
    # enlaces internos -> versión del idioma
    s = re.sub(r'href="/(services|resources|get-started)(?=["#])', lambda m: f'href="{P}/{m.group(1)}', s)
    s = re.sub(r"'/(services|resources|get-started)'", lambda m: f"'{P}/{m.group(1)}'", s)
    if P:
        s = s.replace('href="/"', f'href="{P}"').replace('href="/#', f'href="{P}#')
    # idioma fijado por la URL; los botones EN/ES/CAT llevan a la URL del otro idioma
    s = re.sub(r"getLang\(\) \{[^\n]*\}", f"getLang() {{ return '{LANG_CODE[lang]}'; }}", s)
    s = re.sub(
        r"pickLang\(code\) \{\n\s*this\.lang = code;\n\s*try \{ localStorage\.setItem\('gecanor-lang', code\); \} catch \(e\) \{\}\n\s*this\.forceUpdate\(\(\) => this\.runI18n\(\)\);\n\s*\}",
        "pickLang(code) {\n    try { localStorage.setItem('gecanor-lang', code); } catch (e) {}\n"
        "    const pre = { EN: '', ES: '/es', CAT: '/ca' }[code];\n"
        "    const path = location.pathname.replace(/^\\/(es|ca)(?=\\/|$)/, '').replace(/\\/$/, '');\n"
        "    location.href = (pre + path || '/') + location.hash;\n  }", s)
    assert "return '" + LANG_CODE[lang] in s and "const pre = " in s, 'language patch failed'
    # enlaces legales en el pie
    legal, cookies = FOOTER_LINKS[lang]
    s = s.replace('<span>© 2026 Gecanor Beauty Tech</span>',
                  f'<span>© 2026 Gecanor Beauty Tech · <a href="{P}/legal">{legal}</a> · <a href="{P}/cookies">{cookies}</a></span>')
    if page == 'home':
        # el titular de diseño pasa a ser decorativo; el H1 real describe lo que hacemos
        a = s.count('<h1 data-hero-h1="1"')
        s = s.replace('<h1 data-hero-h1="1"', '<div data-hero-h1="1" role="presentation"')
        s = re.sub(r'(<div data-hero-h1="1" role="presentation"[\s\S]*?)</h1>', r'\1</div>', s, count=1)
        s = s.replace("el.closest('h1')", "el.closest('[data-hero-h1]')")
        old = '<p data-hero-p="1" style="margin:0;max-width:36ch;font-size:clamp(17px,1.5vw,21px);line-height:1.3;font-weight:500">We are fully dedicated to create within <br />the cosmetic and supplements space.</p>'
        assert a == 1 and old in s, 'home hero patch failed'
        s = s.replace(old, old.replace('<p data-hero-p="1"', '<h1 data-hero-p="1"').replace(
            'We are fully dedicated to create within <br />the cosmetic and supplements space.</p>', HOME_H1[lang] + '</h1>'))
        anchor = '<section style="position:relative;padding:40px 24px 110px;'
        assert s.count(anchor) == 1, 'faq anchor'
        s = s.replace(anchor, faq_html(lang) + anchor)
    if page == 'resources':
        # artículos en este idioma; si aún no está traducido, se enlaza la versión en español
        note = {'en': 'In Spanish · ', 'ca': 'En castellà · ', 'es': ''}[lang]
        items = []
        for a in sorted({x['slug']: x for l in LANGS for x in published(l)}.values(), key=lambda x: x['date'], reverse=True):
            al = lang if a in published(lang) else 'es'
            items.append({'cat': a['cat'], 'time': a['time'], 'title': a[al]['title'],
                          'excerpt': ('' if al == lang else note) + a[al]['excerpt'],
                          'href': PREFIX[al] + art_path(a), 'image': '/assets/articles/' + cover_name(a['slug'], al, 'card')})
        assert 'const ARTICLES = [];' in s, 'resources anchor'
        s = s.replace('const ARTICLES = [];', 'const ARTICLES = ' + json.dumps(items, ensure_ascii=False).replace('</', '<\\/') + ';')
    if page == 'services':
        old = 'Six disciplines under one roof. Pick the ones you need or hand us the whole path from brief to shelf.</p>'
        assert old in s, 'services intro'
        s = s.replace(old, SERVICES_INTRO[lang] + '</p>')
    return s


def split_source(src):
    m = re.search(r'<x-dc(?:\s[^>]*)?>', src)
    end = src.rfind('</x-dc>') + len('</x-dc>')
    xdc = src[m.start():end]
    rest = src[end:]
    rest = rest[:rest.rfind('</body>')]
    return xdc, rest


LOADER = '''<script>
(function () {
  var t = document.getElementById('dc-src');
  var x = document.createElement('x-dc');
  x.innerHTML = t.innerHTML.replace(/^\\s*<x-dc[^>]*>/, '').replace(/<\\/x-dc>\\s*$/, '');
  t.parentNode.insertBefore(x, t);
  var ssr = document.getElementById('ssr');
  var mo = new MutationObserver(function () {
    var r = document.getElementById('dc-root');
    if (r && r.childElementCount && ssr) { ssr.remove(); ssr = null; mo.disconnect(); }
  });
  mo.observe(document.body, { childList: true, subtree: true });
})();
</script>'''


def app_page(page, lang, ssr='', helmet=''):
    src = transform((SRC / f'{page}.html').read_text(encoding='utf-8'), lang, page)
    xdc, rest = split_source(src)
    extra = service_ld(lang) if page == 'services' else (faq_ld(lang) if page == 'home' else None)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head(page, lang, extra)}<script>window.__resources = {{"https://unpkg.com/react@18.3.1/umd/react.production.min.js": "/vendor/react.production.min.js", "https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js": "/vendor/react-dom.production.min.js"}};</script>
<script src="/support.js"></script>
{helmet}</head>
<body>
<div id="ssr">{ssr}</div>
<template id="dc-src">{xdc}</template>
{LOADER}
{rest.strip()}
</body>
</html>
'''


# ------------------------------------------------------------------ static pages
STATIC_CSS = '''
body{margin:0;background:#FBFBF9;color:#0B0B0B;font-family:Archivo,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}
header{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:24px;border-bottom:1px solid #0B0B0B}
header .logo{display:block;width:64px;height:54px;background:#0B0B0B;-webkit-mask:url(/assets/gr.svg) center/contain no-repeat;mask:url(/assets/gr.svg) center/contain no-repeat}
nav{display:flex;gap:14px;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:12px;letter-spacing:.06em;text-transform:uppercase}
nav a{text-decoration:none;opacity:.45}nav a[aria-current]{opacity:1;text-decoration:underline}
main{max-width:760px;margin:0 auto;padding:48px 24px 96px;line-height:1.6;font-size:16px}
h1{font-size:clamp(34px,6vw,56px);line-height:1;letter-spacing:-.03em;text-transform:uppercase;margin:0 0 24px}
h2{font-size:20px;margin:40px 0 8px}h3{font-size:16px;margin:24px 0 4px}
.upd,.back{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:12px;color:#6F6E69;text-transform:uppercase;letter-spacing:.06em}
.tbl{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{border-top:1px solid #D8D7D2;padding:8px 10px 8px 0;text-align:left;vertical-align:top}
th{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:#6F6E69}
.btns{display:flex;gap:10px;flex-wrap:wrap}.btns button{cursor:pointer;border:1px solid #0B0B0B;background:transparent;padding:12px 18px;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.btns .primary{background:#0B0B0B;color:#fff}
footer{border-top:1px solid #0B0B0B;padding:18px 24px;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:11px;color:#8F8E89;text-transform:uppercase}
'''


def static_page(page, lang):
    path, body_fn = STATIC_PAGES[page]
    cur = ' aria-current="page"'
    langs = ''.join(
        f'<a href="{local(l, path)}" hreflang="{l}"{cur if l == lang else ""}>{LANG_CODE[l]}</a>' for l in LANGS)
    legal, cookies = FOOTER_LINKS[lang]
    P = PREFIX[lang]
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head(page, lang)}<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{STATIC_CSS}</style>
</head>
<body>
<header><a class="logo" href="{local(lang, '')}" aria-label="Gecanor Beauty Tech"></a><nav>{langs}</nav></header>
<main>
<p class="back"><a href="{local(lang, '')}">{BACK[lang]}</a></p>
{body_fn(lang)}
<p class="upd">{UPDATED[lang]}</p>
</main>
<footer>© 2026 Gecanor Beauty Tech · <a href="{P}/legal">{legal}</a> · <a href="{P}/cookies">{cookies}</a></footer>
</body>
</html>
'''



# ------------------------------------------------------------------ articles
MONTHS = {'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
          'ca': ['gener', 'febrer', 'març', 'abril', 'maig', 'juny', 'juliol', 'agost', 'setembre', 'octubre', 'novembre', 'desembre'],
          'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']}
CAT_LABEL = {'es': {'Formulation': 'Formulación', 'Regulatory': 'Regulación', 'Manufacturing': 'Fabricación', 'Packaging': 'Packaging', 'Brand & market': 'Marca y mercado'},
             'ca': {'Formulation': 'Formulació', 'Regulatory': 'Regulació', 'Manufacturing': 'Fabricació', 'Packaging': 'Packaging', 'Brand & market': 'Marca i mercat'},
             'en': {}}
ART_TXT = {
    'es': dict(home='Inicio', services='Servicios', resources='Recursos', start='Empezar', faq='Preguntas frecuentes', sources='Fuentes',
               by='Por', related='Más artículos', cta='Cuéntanos tu proyecto', read='min de lectura', updated='Publicado el',
               disclaimer='Artículo informativo; no sustituye el asesoramiento regulatorio de cada producto.'),
    'ca': dict(home='Inici', services='Serveis', resources='Recursos', start='Comencem', faq='Preguntes freqüents', sources='Fonts',
               by='Per', related='Més articles', cta='Explica\'ns el teu projecte', read='min de lectura', updated='Publicat el',
               disclaimer='Article informatiu; no substitueix l\'assessorament regulatori de cada producte.'),
    'en': dict(home='Home', services='Services', resources='Resources', start='Get started', faq='Frequently asked questions', sources='Sources',
               by='By', related='More articles', cta='Tell us about your project', read='min read', updated='Published on',
               disclaimer='For information only; it does not replace product-specific regulatory advice.'),
}

ART_CSS = STATIC_CSS + """
nav.site{gap:18px}nav.site a{opacity:1}
.crumbs{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#6F6E69;margin:0 0 28px}
.crumbs a{text-decoration:none}.crumbs a:hover{text-decoration:underline}
.meta{display:flex;flex-wrap:wrap;gap:6px 16px;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:#6F6E69;margin:0 0 18px}
.meta b{color:#0B0B0B;font-weight:500}
article h1{text-transform:none;font-size:clamp(34px,5vw,58px);letter-spacing:-.03em;line-height:1.02;font-weight:600}
article .cover{display:block;width:100%;height:auto;border:1px solid #DAD9D4;margin:0 0 32px}
.byline{font-size:14px;color:#3A3A38;border-top:1px solid #DAD9D4;border-bottom:1px solid #DAD9D4;padding:12px 0;margin:0 0 32px}
article .body>p:first-child{font-size:19px;line-height:1.5}
article h2{font-size:26px;letter-spacing:-.02em;margin:48px 0 10px;line-height:1.15}
article h3{font-size:18px;margin:26px 0 6px}
article table{margin:18px 0}article td,article th{padding:10px 12px 10px 0}
article li{margin:4px 0}
.faq{margin-top:56px;border-top:1px solid #0B0B0B;padding-top:8px}
.cta{margin:56px 0 0;padding:28px;background:#0B0B0B;color:#fff;display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between}
.cta p{margin:0;max-width:52ch}.cta a{background:#fff;color:#0B0B0B;padding:14px 22px;text-decoration:none;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:12px;letter-spacing:.1em;text-transform:uppercase}
.src{font-size:14px}.src li{margin:2px 0}
.disc{font-size:13px;color:#6F6E69;font-style:italic}
.related a{display:block;padding:14px 0;border-top:1px solid #DAD9D4;text-decoration:none;font-weight:500}.related a:hover{text-decoration:underline}
.sh{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 24px;border-bottom:0}.sh{position:sticky;top:0;z-index:500;background:#FBFBF9}
.sh .logo{width:84px;height:70px}@media (max-width:760px){.sh{position:static}}
.sh nav{display:flex;flex-wrap:wrap;align-items:center;justify-content:flex-end;gap:22px;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:12px;letter-spacing:.06em;text-transform:uppercase}
.sh nav a{opacity:1;text-decoration:none}.sh nav a:hover{color:#6F6E69}
.sh nav a.on{text-decoration:underline;text-underline-offset:4px}
.sh nav a.gs{padding:10px 16px;background:#0B0B0B;color:#fff}.sh nav a.gs:hover{background:#3A3A38;color:#fff}
.sh .lg{display:flex;align-items:center;gap:2px}.sh .lg a{padding:4px 5px;font-size:11px;opacity:.45}.sh .lg a[aria-current]{opacity:1;text-decoration:underline;text-underline-offset:4px}
.sf{background:#0B0B0B;color:#fff;padding:48px 24px 24px;border-top:0;font-family:Archivo,Helvetica,Arial,sans-serif;font-size:15px;color:#fff;text-transform:none}
.sf a{text-decoration:none}.sf a:hover{color:#8F8E89}
.sf .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:32px;line-height:1.5}
.sf .k{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:11px;color:#8F8E89;text-transform:uppercase;margin-bottom:10px}
.sf .st{display:flex;flex-direction:column;gap:4px}
.sf img{display:block;margin:20px 0 14px;width:min(100%,720px);height:auto}
.sf .bt{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-top:18px;font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:11px;color:#8F8E89;text-transform:uppercase}
@media (max-width:760px){.sh{gap:8px}.sh nav{gap:10px 9px;font-size:11px;letter-spacing:.02em}html[lang="en"] .sh nav{gap:10px 12px;font-size:12px;letter-spacing:.06em}html[lang="ca"] .sh nav{gap:10px 12px;letter-spacing:.04em}.sh .lg{flex-basis:100%;justify-content:flex-end}.sh nav a.gs{margin-top:5px}.sh .logo{flex:0 0 74px;width:74px;height:64px;margin-left:-12px}}
"""

SITE_TXT = {
 "en": {
  "work": "Work",
  "services": "Services",
  "studio": "Studio",
  "resources": "Resources",
  "gs": "Get Started",
  "collab": "Let's collaborate!",
  "spain": "Spain",
  "china": "China",
  "index": "Index",
  "home": "Home",
  "start": "Get Started",
  "legal": "Legal &amp; privacy",
  "cookies": "Cookies"
 },
 "es": {
  "work": "Proyectos",
  "services": "Servicios",
  "studio": "Estudio",
  "resources": "Recursos",
  "gs": "Empezar",
  "collab": "¡Colaboremos!",
  "spain": "España",
  "china": "China",
  "index": "Índice",
  "home": "Inicio",
  "start": "Empezar",
  "legal": "Aviso legal y privacidad",
  "cookies": "Cookies"
 },
 "ca": {
  "work": "Projectes",
  "services": "Serveis",
  "studio": "Estudi",
  "resources": "Recursos",
  "gs": "Comencem",
  "collab": "Col·laborem!",
  "spain": "Espanya",
  "china": "Xina",
  "index": "Índex",
  "home": "Inici",
  "start": "Comencem",
  "legal": "Avís legal i privacitat",
  "cookies": "Galetes"
 }
}
SITE_CODE = {'en': 'EN', 'es': 'ES', 'ca': 'CAT'}


def site_header(lang, path, langs):
    t, P = SITE_TXT[lang], PREFIX[lang]
    home = local(lang, '')
    lg = ''.join(f'<a href="{local(l, path)}" hreflang="{l}"' + (' aria-current="page"' if l == lang else '') + f'>{SITE_CODE[l]}</a>' for l in langs)
    return (f'<header class="sh"><a class="logo" href="{home}" aria-label="Gecanor Beauty Tech"></a>\n'
            f'<nav class="site"><a href="{P}/#work">{t["work"]}</a><a href="{P}/services">{t["services"]}</a><a href="{P}/#studio">{t["studio"]}</a>'
            f'<a class="on" href="{P}/resources">{t["resources"]}</a><a class="gs" href="{P}/get-started">{t["gs"]}</a><span class="lg">{lg}</span></nav></header>')


def site_footer(lang):
    t, P = SITE_TXT[lang], PREFIX[lang]
    home = local(lang, '')
    return (f'<footer class="sf"><div class="cols">\n'
            f'<div><div class="k">{t["collab"]}</div><div class="st"><a href="mailto:social@gecanor.com">social@gecanor.com</a><a href="https://www.instagram.com/gecanor.beautytech/" target="_blank" rel="noopener noreferrer">Instagram ↗</a><a href="https://www.linkedin.com/company/gecanor/posts/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div>\n'
            f'<div><div class="k">{t["spain"]}</div>C/ Balmes 127, Principal 2ºA<br>08008 Barcelona</div>\n'
            f'<div><div class="k">{t["china"]}</div>Wanke Jiazhouwan V-Pai, 501<br>610036 Chengdu</div>\n'
            f'<div class="st"><div class="k" style="margin-bottom:6px">{t["index"]}</div><a href="{home}">{t["home"]}</a><a href="{P}/services">{t["services"]}</a><a href="{P}/resources">{t["resources"]}</a><a href="{P}/get-started">{t["start"]}</a></div>\n'
            f'</div><img src="/assets/gecanor-logo-bt-white.png" alt="gecanor. beauty tech" width="720" height="160" loading="lazy">\n'
            f'<div class="bt"><span>© 2026 Gecanor Beauty Tech · <a href="{P}/legal">{t["legal"]}</a> · <a href="{P}/cookies">{t["cookies"]}</a></span><span>Ref. GCN — Barcelona / Chengdu</span></div></footer>')



def fdate(d, lang):
    y, m, dd = (int(x) for x in d.split('-'))
    if lang == 'en':
        return f'{dd} {MONTHS[lang][m - 1]} {y}'
    return f'{dd} de {MONTHS[lang][m - 1]} de {y}'


def article_page(a, lang):
    t, T, e, P = a[lang], ART_TXT[lang], html.escape, PREFIX[lang]
    path = art_path(a)
    canon = url(lang, path)
    langs = [l for l in LANGS if l in a and (ART_DIR / f"{a['slug']}.{l}.md").exists() and a['date'] <= TODAY]
    body = md.markdown((ART_DIR / f"{a['slug']}.{lang}.md").read_text(encoding='utf-8'), extensions=['tables'])
    body = body.replace('<a href="http', '<a rel="noopener" target="_blank" href="http')
    cat = CAT_LABEL[lang].get(a['cat'], a['cat'])
    wide, card = '/assets/articles/' + cover_name(a['slug'], lang, 'wide'), '/assets/articles/' + cover_name(a['slug'], lang, 'card')
    ld = [
        {'@type': 'BlogPosting', '@id': canon + '#article', 'headline': t['title'], 'description': t['description'],
         'datePublished': a['date'], 'dateModified': a.get('modified', a['date']), 'inLanguage': lang,
         'mainEntityOfPage': canon, 'image': [SITE + wide, SITE + card], 'articleSection': cat, 'keywords': ', '.join(t['keywords']),
         'author': {'@type': 'Person', 'name': AUTHOR['name'], 'jobTitle': AUTHOR['role'][lang], 'worksFor': {'@id': SITE + '/#org'}},
         'publisher': {'@id': SITE + '/#org'}, 'isPartOf': {'@id': SITE + '/#website'},
         'citation': [u for _, u in a['sources']]},
        {'@type': 'FAQPage', '@id': canon + '#faq', 'inLanguage': lang,
         'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': r}} for q, r in t['faq']]},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': T['home'], 'item': url(lang, '')},
            {'@type': 'ListItem', 'position': 2, 'name': T['resources'], 'item': url(lang, '/resources')},
            {'@type': 'ListItem', 'position': 3, 'name': t['title'], 'item': canon}]},
    ]
    h = head('resources', lang, ld, meta=(t['seo_title'], t['description']), path=path, langs=langs, og_type='article', image=SITE + wide)
    h += f'<meta property="article:published_time" content="{a["date"]}">\n'
    faq = ''.join(f'<h3>{e(q)}</h3><p>{e(r)}</p>' for q, r in t['faq'])
    src = ''.join(f'<li><a rel="noopener" target="_blank" href="{e(u)}">{e(n)}</a></li>' for n, u in a['sources'])
    others = [o for o in published(lang) if o['slug'] != a['slug']][:3]
    related = ''.join(f'<a href="{P}{art_path(o)}">{e(o[lang]["title"])}</a>' for o in others)
    related = f'<section class="related"><h2>{T["related"]}</h2>{related}</section>' if related else ''
    legal, cookies = FOOTER_LINKS[lang]
    home = local(lang, '')
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
{h}<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;800&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>{ART_CSS}</style>
</head>
<body>
{site_header(lang, path, langs)}
<main>
<article>
<p class="crumbs"><a href="{home}">{T['home']}</a> / <a href="{P}/resources">{T['resources']}</a> / {e(cat)}</p>
<div class="meta"><b>{e(cat)}</b><span>{a['time'].replace('min', '').strip()} {T['read']}</span><time datetime="{a['date']}">{fdate(a['date'], lang)}</time></div>
<h1>{e(t['title'])}</h1>
<p class="byline">{T['by']} <strong>{AUTHOR['name']}</strong>, {AUTHOR['role'][lang]} · {T['updated']} {fdate(a['date'], lang)}</p>
<img class="cover" src="{wide}" alt="{e(t['title'])}" width="1200" height="630">
<div class="body">{body}</div>
<section class="faq"><h2>{T['faq']}</h2>{faq}</section>
<div class="cta"><p>{e(t['cta'])}</p><a href="{P}/get-started">{T['cta']} ↗</a></div>
<section><h2>{T['sources']}</h2><ul class="src">{src}</ul><p class="disc">{T['disclaimer']}</p></section>
{related}
</article>
</main>
{site_footer(lang)}
</body>
</html>
"""


def write_articles():
    keep = set()
    for lang in LANGS:
        for a in published(lang):
            f = out_file(lang, art_path(a)); f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(article_page(a, lang), encoding='utf-8')
            keep.add(f.parent)
    # borra páginas de artículos que ya no deben estar publicadas
    for lang in LANGS:
        base = out_file(lang, '/resources').parent
        for d in base.iterdir() if base.exists() else []:
            if d.is_dir() and d not in keep:
                shutil.rmtree(d)
    return sum(len(published(l)) for l in LANGS)


# ------------------------------------------------------------------ prerender
CDN = {
    'react@18.3.1/umd/react.production.min.js': OUT / 'vendor/react.production.min.js',
    'react-dom@18.3.1/umd/react-dom.production.min.js': OUT / 'vendor/react-dom.production.min.js',
    '@babel/standalone@7.29.0/babel.min.js': VENDOR / 'babel/babel.min.js',
}


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def translate_path(self, path):  # cleanUrls como en Vercel
        p = super().translate_path(path)
        if not os.path.exists(p) and os.path.isdir(p.rstrip('/')):
            return p
        return p


def prerender(jobs):
    """jobs: list of (page, lang). Devuelve {(page, lang): (ssr_html, helmet_html)}."""
    from playwright.sync_api import sync_playwright
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 8766), functools.partial(Handler, directory=str(OUT)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    def route(r):
        u = r.request.url
        if u.startswith('http://127.0.0.1'):
            return r.continue_()
        for k, f in CDN.items():
            if k in u:
                return r.fulfill(path=str(f), content_type='application/javascript')
        return r.fulfill(status=204, body='')

    res = {}
    with sync_playwright() as p:
        exe = os.environ.get('CHROME', '/usr/bin/google-chrome')
        b = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None, args=['--no-sandbox'])
        for page, lang in jobs:
            pg = b.new_page(viewport={'width': 1440, 'height': 900})
            pg.route('**/*', route)
            pg.add_init_script("try{localStorage.setItem('gecanor-consent','denied')}catch(e){}")
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto('http://127.0.0.1:8766' + local(lang, APP_PAGES[page]) + ('/' if APP_PAGES[page] or PREFIX[lang] else ''))
            pg.wait_for_function("document.getElementById('dc-root') && document.getElementById('dc-root').childElementCount > 0", timeout=20000)
            pg.wait_for_timeout(5000)
            if errs:
                raise RuntimeError(f'{page}/{lang}: {errs}')
            ssr, helmet = pg.evaluate('''() => {
              const root = document.getElementById('dc-root').cloneNode(true);
              root.querySelectorAll('script,.sc-logic-error').forEach(n => n.remove());
              root.querySelectorAll('h1,h2,h3,h4').forEach(h => { if (!h.textContent.trim()) h.replaceWith(...h.childNodes); });
              root.querySelectorAll('video').forEach(v => { v.removeAttribute('autoplay'); v.removeAttribute('controls'); v.setAttribute('preload', 'none'); });
              const keep = [...document.head.children].filter(n =>
                (n.tagName === 'STYLE') || (n.tagName === 'LINK' && /stylesheet|preconnect/.test(n.rel)));
              return [root.innerHTML, keep.map(n => n.outerHTML).join('\\n')];
            }''')
            assert '{{' not in ssr, f'{page}/{lang}: plantillas sin resolver en el pre-render'
            res[(page, lang)] = (ssr, helmet + '\n')
            pg.close()
        b.close()
    srv.shutdown()
    return res


# ------------------------------------------------------------------ sitemap etc.
def sitemap():
    rows = []
    for page, path in ALL_PAGES.items():
        for lang in LANGS:
            alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{url(l, path)}"/>' for l in LANGS)
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url("en", path)}"/>'
            prio = '1.0' if page == 'home' else ('0.3' if page in STATIC_PAGES else '0.8')
            rows.append(f'  <url>\n    <loc>{url(lang, path)}</loc>{alts}\n    <priority>{prio}</priority>\n  </url>')
    for lang in LANGS:
        for a in published(lang):
            ls = [l for l in LANGS if a in published(l)]
            alts = ''.join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{url(l, art_path(a))}"/>' for l in ls) if len(ls) > 1 else ''
            rows.append(f'  <url>\n    <loc>{url(lang, art_path(a))}</loc>{alts}\n    <lastmod>{a.get("modified", a["date"])}</lastmod>\n    <priority>0.7</priority>\n  </url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + '\n'.join(rows) + '\n</urlset>\n')


ROBOTS = f'''# gecanor.com
User-agent: *
Allow: /

# Buscadores e IA: acceso permitido para que puedan citar a Gecanor
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
'''


def llms_txt():
    s = SERVICES['en']
    return f'''# Gecanor Beauty Tech

> {ORG_DESC['en']}

Gecanor Beauty Tech (legal name {COMPANY['legal']}) works as a full-service, white-label development partner for brands that want to launch cosmetics, nutricosmetics or food supplements. Minimum order quantity starts at 500 units. Contact: {COMPANY['email']}.

## Services
''' + '\n'.join(f'- [{x}]({url("en", "/services")}{"#s0" + str(i) if i else ""})' for i, x in enumerate(s)) + f'''

## Pages
- [Home (EN)]({url("en", "")}) · [ES]({url("es", "")}) · [CA]({url("ca", "")})
- [Services]({url("en", "/services")}) · [Servicios]({url("es", "/services")}) · [Serveis]({url("ca", "/services")})
- [Resources / articles]({url("en", "/resources")}) · [Recursos]({url("es", "/resources")})
- [Get started / contact]({url("en", "/get-started")}) · [Empezar]({url("es", "/get-started")})
''' + ('\n## Articles\n' + '\n'.join(f'- [{a[l]["title"]}]({url(l, art_path(a))}) ({l}): {a[l]["description"]}'
                                         for l in LANGS for a in published(l)) + '\n' if any(published(l) for l in LANGS) else '')


# ------------------------------------------------------------------ main
def main():
    import covers
    covers.main()  # crea las portadas que falten
    jobs = [(p, l) for p in APP_PAGES for l in LANGS]
    # 1) páginas sin pre-render (para poder renderizarlas)
    for page, lang in jobs:
        f = out_file(lang, APP_PAGES[page]); f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(app_page(page, lang), encoding='utf-8')
    # 2) pre-render y versión final
    rendered = prerender(jobs)
    for (page, lang), (ssr, helmet) in rendered.items():
        out_file(lang, APP_PAGES[page]).write_text(app_page(page, lang, ssr, helmet), encoding='utf-8')
    # 3) páginas legales
    for page in STATIC_PAGES:
        for lang in LANGS:
            f = out_file(lang, STATIC_PAGES[page][0]); f.parent.mkdir(parents=True, exist_ok=True)
            f.write_text(static_page(page, lang), encoding='utf-8')
    n_art = write_articles()
    (OUT / 'sitemap.xml').write_text(sitemap(), encoding='utf-8')
    (OUT / 'robots.txt').write_text(ROBOTS, encoding='utf-8')
    (OUT / 'llms.txt').write_text(llms_txt(), encoding='utf-8')
    print('OK', len(rendered), 'páginas pre-renderizadas +', len(STATIC_PAGES) * len(LANGS), 'legales +', n_art, 'artículos · fecha', TODAY)


if __name__ == '__main__':
    main()

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
import html, json, os, re, sys, threading, http.server, functools
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import (SITE, LANGS, PREFIX, LANG_CODE, OG_LOCALE, COMPANY, APP_PAGES, META,
                     ORG_DESC, SERVICES, FOOTER_LINKS, STATIC_PAGES, UPDATED, BACK)

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / 'source' / 'pages'
OUT = REPO / 'gecanor-lab-web'
VENDOR = Path(os.environ.get('GECANOR_VENDOR', '/home/claude/vendor'))
OG_IMAGE = SITE + '/assets/og-gecanor.jpg'
ALL_PAGES = {**APP_PAGES, **{k: v[0] for k, v in STATIC_PAGES.items()}}


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
def head(page, lang, extra_ld=None):
    title, desc = META[page][lang]
    path = ALL_PAGES[page]
    canon = url(lang, path)
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{url(l, path)}">\n' for l in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{url("en", path)}">\n'
    org = {
        '@type': 'Organization', '@id': SITE + '/#org', 'name': COMPANY['brand'], 'legalName': COMPANY['legal'],
        'taxID': COMPANY['nif'], 'url': SITE + '/', 'logo': SITE + '/assets/logo-gecanor.png', 'image': OG_IMAGE,
        'email': COMPANY['email'], 'description': ORG_DESC[lang],
        'address': {'@type': 'PostalAddress', 'streetAddress': COMPANY['street'], 'addressLocality': COMPANY['city'],
                    'postalCode': COMPANY['zip'], 'addressCountry': COMPANY['country']},
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
{alts}<meta property="og:type" content="website">
<meta property="og:site_name" content="{COMPANY['brand']}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{OG_IMAGE}">
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


# ------------------------------------------------------------------ app pages
ASSET_RE = re.compile(r'(["\'(])\.\.?/(assets/|support\.js|i18n\.js|lab-i18n\.js)')


def transform(src, lang):
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
    src = transform((SRC / f'{page}.html').read_text(encoding='utf-8'), lang)
    xdc, rest = split_source(src)
    extra = service_ld(lang) if page == 'services' else None
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head(page, lang, extra)}<script src="/support.js"></script>
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


# ------------------------------------------------------------------ prerender
CDN = {
    'react@18.3.1/umd/react.production.min.js': VENDOR / 'react-18.3.1/umd/react.production.min.js',
    'react-dom@18.3.1/umd/react-dom.production.min.js': VENDOR / 'react-dom-18.3.1/umd/react-dom.production.min.js',
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
'''


# ------------------------------------------------------------------ main
def main():
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
    (OUT / 'sitemap.xml').write_text(sitemap(), encoding='utf-8')
    (OUT / 'robots.txt').write_text(ROBOTS, encoding='utf-8')
    (OUT / 'llms.txt').write_text(llms_txt(), encoding='utf-8')
    print('OK', len(rendered), 'páginas pre-renderizadas +', len(STATIC_PAGES) * len(LANGS), 'legales')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""Genera las portadas tipográficas de los artículos (estilo gecanor.com).

  python3 source/covers.py            (necesita playwright + Chrome)

Crea en gecanor-lab-web/assets/articles/:
  <slug>-wide.jpg  1200x630  cabecera del artículo y vista previa en redes
  <slug>-card.jpg  1200x900  tarjeta del listado de Recursos
Solo crea las que faltan; con --force las rehace todas.
"""
import base64, html, os, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'articles'))
from articles import ARTICLES

OUT = HERE.parent / 'gecanor-lab-web' / 'assets' / 'articles'
LOGO = (HERE.parent / 'gecanor-lab-web' / 'assets' / 'gr.svg').read_text(encoding='utf-8')
CAT = {'es': {'Formulation': 'Formulación', 'Regulatory': 'Regulación', 'Manufacturing': 'Fabricación', 'Packaging': 'Packaging', 'Brand & market': 'Marca y mercado'},
       'ca': {'Formulation': 'Formulació', 'Regulatory': 'Regulació', 'Manufacturing': 'Fabricació', 'Packaging': 'Packaging', 'Brand & market': 'Marca i mercat'},
       'en': {}}
TXT = {'es': ('Recursos', 'de lectura', 'gecanor.com/es/resources', 'Lab<br>notas'),
       'ca': ('Recursos', 'de lectura', 'gecanor.com/ca/resources', 'Lab<br>notes'),
       'en': ('Resources', 'read', 'gecanor.com/resources', 'Lab<br>notes')}


def cover_name(slug, lang, kind):
    """Nombre del archivo de portada (la versión en español no lleva sufijo de idioma)."""
    return f"{slug}-{kind}.jpg" if lang == 'es' else f"{slug}-{lang}-{kind}.jpg"


def font(name):
    return 'data:font/woff2;base64,' + base64.b64encode((HERE / 'fonts' / name).read_bytes()).decode()


CSS = f"""
@font-face{{font-family:'A';src:url({font('archivo-latin-wdth-normal.woff2')}) format('woff2');font-weight:100 900;font-stretch:62% 125%}}
@font-face{{font-family:'M';src:url({font('ibm-plex-mono-latin-400-normal.woff2')}) format('woff2');font-weight:400}}
@font-face{{font-family:'M';src:url({font('ibm-plex-mono-latin-500-normal.woff2')}) format('woff2');font-weight:500}}
*{{box-sizing:border-box;margin:0}}
body{{width:var(--w);height:var(--h);background:#FBFBF9;color:#0B0B0B;overflow:hidden;position:relative;font-family:'A'}}
.frame{{position:absolute;inset:36px;display:flex;flex-direction:column}}
.row{{display:grid;grid-template-columns:repeat(4,1fr);font-family:'M';font-size:15px;letter-spacing:.06em;text-transform:uppercase;color:#6F6E69;padding:12px 0;border-top:2px solid #0B0B0B;border-bottom:1px solid #DAD9D4}}
.row span:first-child{{color:#0B0B0B}}
h1{{flex:1;display:flex;align-items:center;font-weight:800;font-stretch:62%;text-transform:uppercase;line-height:.96;letter-spacing:-.01em;max-width:var(--tw);padding:24px 0}}
.foot{{display:flex;justify-content:space-between;align-items:flex-end;font-family:'M';font-size:15px;letter-spacing:.06em;text-transform:uppercase;color:#6F6E69;border-top:1px solid #DAD9D4;padding-top:14px}}
.foot svg{{height:46px;width:auto}}.foot svg *{{fill:#0B0B0B}}
.badge{{position:absolute;width:150px;height:150px;border-radius:50%;background:#0B0B0B;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-12deg);text-align:center}}
.badge b{{font-weight:850;font-stretch:62%;font-size:34px;line-height:.86;text-transform:uppercase}}
.badge i{{font-style:normal;font-family:'M';font-size:11px;letter-spacing:.08em;margin-top:8px}}
.tag{{position:absolute;background:#fff;border:1.5px solid #0B0B0B;padding:10px 14px;font-family:'M';font-size:13px;letter-spacing:.06em;text-transform:uppercase;transform:rotate(5deg)}}
.tag hr{{border:0;border-top:1px solid #0B0B0B;margin:6px 0}}
"""


def page(a, n, w, h, lang='es'):
    t = a[lang]
    cat = CAT[lang].get(a['cat'], a['cat'])
    R, READ, URL, BADGE = TXT[lang]
    badge_pos = 'right:70px;top:110px' if h < 700 else 'right:70px;top:120px'
    tag_pos = 'right:56px;bottom:110px' if h < 700 else 'right:60px;bottom:130px'
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>:root{{--w:{w}px;--h:{h}px;--tw:{'76%' if h < 700 else '84%'}}}{CSS}</style></head><body>
<div class="frame">
  <div class="row"><span>Gecanor Beauty Tech</span><span>{R} · Nº {n:02d}</span><span>{cat}</span><span>{a['time']} {READ}</span></div>
  <h1 id="t">{html.escape(t['title'])}</h1>
  <div class="foot"><span>{URL}</span>{LOGO}</div>
</div>
<div class="badge" style="{badge_pos}"><b>{BADGE}</b><i>VOL. 01</i></div>
<div class="tag" style="{tag_pos}">Ref. GCN-R-{n:02d}<hr>Barcelona — Chengdu</div>
<script>
const t=document.getElementById('t');let s={190 if h > 700 else 132};t.style.fontSize=s+'px';
const box=()=>t.scrollHeight<=t.clientHeight+2&&t.scrollWidth<=t.clientWidth+2;
const lines=()=>{{const r=document.createRange();r.selectNodeContents(t);return Math.round(r.getBoundingClientRect().height/(s*0.96));}};
while(s>40&&(!box()||lines()>{6 if h > 700 else 4}))t.style.fontSize=(s-=4)+'px';
</script></body></html>"""


def main():
    from playwright.sync_api import sync_playwright
    force = '--force' in sys.argv
    OUT.mkdir(parents=True, exist_ok=True)
    order = sorted(ARTICLES, key=lambda a: a['date'])
    jobs = []
    for n, a in enumerate(order, 1):
        for lang in ('es', 'ca', 'en'):
            if lang not in a:
                continue
            for kind, (w, h) in {'wide': (1200, 630), 'card': (1200, 900)}.items():
                f = OUT / cover_name(a['slug'], lang, kind)
                if force or not f.exists():
                    jobs.append((a, n, w, h, f, lang))
    if not jobs:
        print('Portadas al día'); return
    with sync_playwright() as p:
        exe = os.environ.get('CHROME', '/usr/bin/google-chrome')
        b = p.chromium.launch(executable_path=exe if os.path.exists(exe) else None, args=['--no-sandbox'])
        for a, n, w, h, f, lang in jobs:
            pg = b.new_page(viewport={'width': w, 'height': h})
            pg.set_content(page(a, n, w, h, lang)); pg.wait_for_timeout(300)
            pg.screenshot(path=str(f), type='jpeg', quality=88)
            pg.close(); print('·', f.name)
        b.close()


if __name__ == '__main__':
    main()

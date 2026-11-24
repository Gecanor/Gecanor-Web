/* Google tag (GA4 · GTM-NX6LWQ6T) con Consent Mode v2 + aviso de cookies.
   Analytics no guarda cookies hasta que el visitante pulsa "Aceptar".
   La elección se guarda en localStorage ("gecanor-consent": "granted" | "denied"). */
(function () {
  var TAG_ID = 'GTM-NX6LWQ6T';
  var KEY = 'gecanor-consent';

  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;

  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}

  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: saved === 'granted' ? 'granted' : 'denied',
    wait_for_update: 500
  });
  gtag('js', new Date());

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtm.js?id=' + TAG_ID;
  document.head.appendChild(s);

  if (saved === 'granted' || saved === 'denied') return;

  var TEXT = {
    EN: ['We use analytics cookies to understand how visitors use this site. They are only set if you accept.', 'Accept', 'Reject'],
    ES: ['Usamos cookies de analítica para entender cómo se usa esta web. Solo se activan si las aceptas.', 'Aceptar', 'Rechazar'],
    CAT: ['Fem servir galetes d’analítica per entendre com s’utilitza aquest web. Només s’activen si les acceptes.', 'Acceptar', 'Rebutjar']
  };

  function lang() {
    var l = 'EN';
    try { l = localStorage.getItem('gecanor-lang') || 'EN'; } catch (e) {}
    return TEXT[l] ? l : 'EN';
  }

  function choose(value, bar) {
    try { localStorage.setItem(KEY, value); } catch (e) {}
    if (value === 'granted') gtag('consent', 'update', { analytics_storage: 'granted' });
    if (bar && bar.parentNode) bar.parentNode.removeChild(bar);
  }

  function show() {
    var t = TEXT[lang()];
    var bar = document.createElement('div');
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-label', 'Cookies');
    bar.style.cssText = 'position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:560px;margin:0 auto;' +
      'background:#111;color:#fff;padding:16px 18px;border-radius:10px;font:13px/1.45 "IBM Plex Mono",ui-monospace,monospace;' +
      'display:flex;flex-wrap:wrap;gap:12px;align-items:center;box-shadow:0 8px 30px rgba(0,0,0,.25)';
    var p = document.createElement('p');
    p.style.cssText = 'margin:0;flex:1 1 280px';
    p.textContent = t[0];
    var btns = document.createElement('div');
    btns.style.cssText = 'display:flex;gap:8px';
    [[t[2], 'denied', 'transparent', '#fff'], [t[1], 'granted', '#fff', '#111']].forEach(function (b) {
      var el = document.createElement('button');
      el.type = 'button';
      el.textContent = b[0];
      el.style.cssText = 'cursor:pointer;border:1px solid #fff;border-radius:999px;padding:7px 14px;font:inherit;background:' + b[2] + ';color:' + b[3];
      el.onclick = function () { choose(b[1], bar); };
      btns.appendChild(el);
    });
    bar.appendChild(p);
    bar.appendChild(btns);
    document.body.appendChild(bar);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', show);
  else show();
})();

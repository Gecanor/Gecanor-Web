# -*- coding: utf-8 -*-
"""Textos SEO (títulos, descripciones, datos estructurados) y páginas legales.
Edita aquí y vuelve a ejecutar `python3 source/build.py`."""

SITE = 'https://www.gecanor.com'
LANGS = ['en', 'es', 'ca']
PREFIX = {'en': '', 'es': '/es', 'ca': '/ca'}
LANG_CODE = {'en': 'EN', 'es': 'ES', 'ca': 'CAT'}   # códigos que usa el motor de la web
OG_LOCALE = {'en': 'en_GB', 'es': 'es_ES', 'ca': 'ca_ES'}

COMPANY = {
    'brand': 'Gecanor Beauty Tech',
    'legal': 'Gecanor Studio, S.L.',
    'nif': 'B72670771',
    'street': 'Calle Bailén, 62',
    'city': 'Barcelona',
    'zip': '08009',
    'country': 'ES',
    'email': 'social@gecanor.com',
    'instagram': 'https://www.instagram.com/gecanor.beautytech/',
    'linkedin': 'https://www.linkedin.com/company/gecanor/',
}

# Páginas generadas desde source/pages/*.html (motor dc-runtime)
APP_PAGES = {
    'home': '',
    'services': '/services',
    'resources': '/resources',
    'get-started': '/get-started',
}

META = {
    'home': {
        'en': ('Gecanor Beauty Tech | Cosmetic & Food Supplement Brand Development in Barcelona',
               'Full-service partner to create your cosmetic or food supplement brand: custom formulation, manufacturing in Spanish labs, EU regulatory compliance, packaging and launch. From 500 units.'),
        'es': ('Gecanor | Desarrollo de marcas de cosmética y complementos alimenticios en Barcelona',
               'Creamos tu marca de cosmética o complementos alimenticios de principio a fin: formulación a medida, fabricación en laboratorios españoles, normativa UE, packaging y lanzamiento. Desde 500 unidades.'),
        'ca': ('Gecanor | Desenvolupament de marques de cosmètica i complements alimentaris a Barcelona',
               'Creem la teva marca de cosmètica o complements alimentaris de principi a fi: formulació a mida, fabricació en laboratoris espanyols, normativa UE, packaging i llançament. Des de 500 unitats.'),
    },
    'services': {
        'en': ('Services: Cosmetic Formulation, Manufacturing & EU Regulatory | Gecanor',
               'Six disciplines under one roof: custom cosmetic and nutricosmetic formulation, manufacturing with Spanish laboratories, EU Regulation 1223/2009 compliance, packaging sourcing, logistics and brand strategy.'),
        'es': ('Servicios: formulación, fabricación y registro de cosméticos | Gecanor',
               'Seis disciplinas bajo un mismo techo: formulación cosmética y nutricosmética a medida, fabricación con laboratorios españoles, cumplimiento del Reglamento (CE) 1223/2009, packaging, logística y estrategia de marca.'),
        'ca': ('Serveis: formulació, fabricació i registre de cosmètics | Gecanor',
               'Sis disciplines sota un mateix sostre: formulació cosmètica i nutricosmètica a mida, fabricació amb laboratoris espanyols, compliment del Reglament (CE) 1223/2009, packaging, logística i estratègia de marca.'),
    },
    'resources': {
        'en': ('Resources: Guides on Cosmetic Formulation, Regulation & Manufacturing | Gecanor',
               'Articles and practical guides on developing cosmetic and food supplement brands: formulation, EU regulation, packaging, private label manufacturing and launch.'),
        'es': ('Recursos: guías sobre formulación, normativa y fabricación cosmética | Gecanor',
               'Artículos y guías prácticas para crear una marca de cosmética o complementos alimenticios: formulación, normativa europea, packaging, fabricación a terceros y lanzamiento.'),
        'ca': ('Recursos: guies sobre formulació, normativa i fabricació cosmètica | Gecanor',
               'Articles i guies pràctiques per crear una marca de cosmètica o complements alimentaris: formulació, normativa europea, packaging, fabricació a tercers i llançament.'),
    },
    'get-started': {
        'en': ('Start Your Cosmetic or Supplement Brand | Gecanor Beauty Tech',
               'Tell us about your project and get a proposal to develop your cosmetic or food supplement brand, from formula to launch. Barcelona and Chengdu. From 500 units.'),
        'es': ('Empieza tu marca de cosmética o suplementos | Gecanor Beauty Tech',
               'Cuéntanos tu proyecto y recibe una propuesta para desarrollar tu marca de cosmética o complementos alimenticios, de la fórmula al lanzamiento. Barcelona y Chengdu. Desde 500 unidades.'),
        'ca': ('Comença la teva marca de cosmètica o suplements | Gecanor Beauty Tech',
               'Explica\'ns el teu projecte i rep una proposta per desenvolupar la teva marca de cosmètica o complements alimentaris, de la fórmula al llançament. Barcelona i Chengdu. Des de 500 unitats.'),
    },
    'legal': {
        'en': ('Legal notice & privacy policy | Gecanor Beauty Tech', 'Legal notice and privacy policy of Gecanor Studio, S.L. (Gecanor Beauty Tech).'),
        'es': ('Aviso legal y política de privacidad | Gecanor Beauty Tech', 'Aviso legal y política de privacidad de Gecanor Studio, S.L. (Gecanor Beauty Tech).'),
        'ca': ('Avís legal i política de privacitat | Gecanor Beauty Tech', 'Avís legal i política de privacitat de Gecanor Studio, S.L. (Gecanor Beauty Tech).'),
    },
    'cookies': {
        'en': ('Cookie policy | Gecanor Beauty Tech', 'Which cookies gecanor.com uses, what for, and how to accept or reject them.'),
        'es': ('Política de cookies | Gecanor Beauty Tech', 'Qué cookies usa gecanor.com, para qué y cómo aceptarlas o rechazarlas.'),
        'ca': ('Política de galetes | Gecanor Beauty Tech', 'Quines galetes fa servir gecanor.com, per a què i com acceptar-les o rebutjar-les.'),
    },
}

ORG_DESC = {
    'en': 'Barcelona-based full-service partner that develops cosmetic and food supplement brands: formulation, manufacturing with Spanish laboratories, EU regulatory compliance, packaging, logistics and brand strategy. Offices in Barcelona and Chengdu.',
    'es': 'Empresa de Barcelona que desarrolla marcas de cosmética y complementos alimenticios de principio a fin: formulación, fabricación con laboratorios españoles, cumplimiento normativo UE, packaging, logística y estrategia de marca. Oficinas en Barcelona y Chengdu.',
    'ca': 'Empresa de Barcelona que desenvolupa marques de cosmètica i complements alimentaris de principi a fi: formulació, fabricació amb laboratoris espanyols, compliment normatiu UE, packaging, logística i estratègia de marca. Oficines a Barcelona i Chengdu.',
}

SERVICES = {
    'en': ['Formula development & innovation', 'Manufacturing & production', 'Regulatory & compliance (EU Regulation 1223/2009)',
           'Packaging research & sourcing', 'Logistics management', 'Brand strategy & market positioning'],
    'es': ['Desarrollo de fórmulas e innovación', 'Fabricación y producción', 'Regulación y cumplimiento normativo (Reglamento CE 1223/2009)',
           'Investigación y aprovisionamiento de packaging', 'Gestión logística', 'Estrategia de marca y posicionamiento'],
    'ca': ['Desenvolupament de fórmules i innovació', 'Fabricació i producció', 'Regulació i compliment normatiu (Reglament CE 1223/2009)',
           'Recerca i aprovisionament de packaging', 'Gestió logística', 'Estratègia de marca i posicionament'],
}

FOOTER_LINKS = {
    'en': ('Legal & privacy', 'Cookies'),
    'es': ('Aviso legal y privacidad', 'Cookies'),
    'ca': ('Avís legal i privacitat', 'Galetes'),
}

# ---------------------------------------------------------------- legal pages
UPDATED = {'en': 'Last updated: 24 November 2026', 'es': 'Última actualización: 24 de noviembre de 2026', 'ca': 'Darrera actualització: 24 de novembre de 2026'}
BACK = {'en': '← Back to home', 'es': '← Volver al inicio', 'ca': '← Tornar a l\'inici'}

def legal_body(lang):
    c = COMPANY
    if lang == 'es':
        return f'''
<h1>Aviso legal y política de privacidad</h1>
<h2>1. Titular del sitio web</h2>
<p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de que este sitio web, <strong>gecanor.com</strong>, es titularidad de:</p>
<ul>
<li>Razón social: <strong>{c['legal']}</strong> (marca comercial «{c['brand']}»)</li>
<li>NIF: {c['nif']}</li>
<li>Domicilio: {c['street']}, {c['zip']} {c['city']} (España)</li>
<li>Correo electrónico: <a href="mailto:{c['email']}">{c['email']}</a></li>
</ul>
<h2>2. Condiciones de uso</h2>
<p>El acceso a este sitio web es gratuito y atribuye la condición de usuario, que se compromete a hacer un uso adecuado de los contenidos. Los textos, imágenes, vídeos, logotipos y diseño son propiedad de {c['legal']} o de terceros que han autorizado su uso, y no pueden reproducirse sin permiso. Las marcas de clientes que aparecen en el sitio pertenecen a sus respectivos titulares.</p>
<p>{c['legal']} no se responsabiliza del contenido de los sitios web de terceros a los que se pueda acceder mediante enlaces.</p>
<h2>3. Protección de datos personales</h2>
<h3>Responsable del tratamiento</h3>
<p>{c['legal']}, NIF {c['nif']}, {c['street']}, {c['zip']} {c['city']}. Contacto: <a href="mailto:{c['email']}">{c['email']}</a>.</p>
<h3>Qué datos tratamos y para qué</h3>
<ul>
<li><strong>Formulario de contacto y correos que nos envías:</strong> nombre, correo electrónico, empresa y la información de tu proyecto. Los usamos para responder a tu consulta y, si procede, preparar una propuesta. Base jurídica: tu consentimiento al enviarnos la consulta y la aplicación de medidas precontractuales a tu petición (art. 6.1.a y 6.1.b RGPD).</li>
<li><strong>Analítica web:</strong> solo si aceptas las cookies de analítica, datos de navegación seudonimizados a través de Google Analytics para conocer el uso del sitio. Base jurídica: tu consentimiento (art. 6.1.a RGPD). Más información en la <a href="/es/cookies">política de cookies</a>.</li>
</ul>
<h3>Cuánto tiempo los conservamos</h3>
<p>Los datos de contacto se conservan mientras dure la relación o la gestión de tu consulta y, después, durante los plazos legales de prescripción de responsabilidades. Los datos de analítica se conservan un máximo de 14 meses.</p>
<h3>Con quién los compartimos</h3>
<p>No vendemos ni cedemos tus datos. Para prestar el servicio usamos proveedores que actúan como encargados del tratamiento: Vercel Inc. (alojamiento web), FormSubmit (envío del formulario de contacto por correo) y Google Ireland Ltd. (Google Analytics y Google Fonts). Algunos de ellos pueden tratar datos fuera del Espacio Económico Europeo, con las garantías previstas en el RGPD (decisión de adecuación UE-EE. UU. o cláusulas contractuales tipo).</p>
<h3>Tus derechos</h3>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación del tratamiento y portabilidad, y retirar tu consentimiento en cualquier momento, escribiendo a <a href="mailto:{c['email']}">{c['email']}</a>. Si consideras que no hemos atendido correctamente tu solicitud, puedes reclamar ante la Agencia Española de Protección de Datos (<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>).</p>
<h2>4. Legislación aplicable</h2>
<p>Este aviso legal se rige por la legislación española. Para cualquier controversia, las partes se someten a los juzgados y tribunales de Barcelona, salvo que la normativa aplicable disponga otra cosa.</p>
'''
    if lang == 'ca':
        return f'''
<h1>Avís legal i política de privacitat</h1>
<h2>1. Titular del lloc web</h2>
<p>En compliment de la Llei 34/2002, de serveis de la societat de la informació i de comerç electrònic (LSSI-CE), s'informa que aquest lloc web, <strong>gecanor.com</strong>, és titularitat de:</p>
<ul>
<li>Raó social: <strong>{c['legal']}</strong> (marca comercial «{c['brand']}»)</li>
<li>NIF: {c['nif']}</li>
<li>Domicili: {c['street']}, {c['zip']} {c['city']} (Espanya)</li>
<li>Correu electrònic: <a href="mailto:{c['email']}">{c['email']}</a></li>
</ul>
<h2>2. Condicions d'ús</h2>
<p>L'accés a aquest lloc web és gratuït i atribueix la condició d'usuari, que es compromet a fer-ne un ús adequat. Els textos, imatges, vídeos, logotips i disseny són propietat de {c['legal']} o de tercers que n'han autoritzat l'ús, i no es poden reproduir sense permís. Les marques de clients que hi apareixen pertanyen als seus titulars.</p>
<p>{c['legal']} no es responsabilitza del contingut dels llocs web de tercers als quals es pugui accedir mitjançant enllaços.</p>
<h2>3. Protecció de dades personals</h2>
<h3>Responsable del tractament</h3>
<p>{c['legal']}, NIF {c['nif']}, {c['street']}, {c['zip']} {c['city']}. Contacte: <a href="mailto:{c['email']}">{c['email']}</a>.</p>
<h3>Quines dades tractem i per a què</h3>
<ul>
<li><strong>Formulari de contacte i correus que ens envies:</strong> nom, correu electrònic, empresa i la informació del teu projecte. Les fem servir per respondre la teva consulta i, si escau, preparar una proposta. Base jurídica: el teu consentiment en enviar-nos la consulta i l'aplicació de mesures precontractuals a petició teva (art. 6.1.a i 6.1.b RGPD).</li>
<li><strong>Analítica web:</strong> només si acceptes les galetes d'analítica, dades de navegació pseudonimitzades mitjançant Google Analytics per conèixer l'ús del lloc. Base jurídica: el teu consentiment (art. 6.1.a RGPD). Més informació a la <a href="/ca/cookies">política de galetes</a>.</li>
</ul>
<h3>Quant de temps les conservem</h3>
<p>Les dades de contacte es conserven mentre duri la relació o la gestió de la teva consulta i, després, durant els terminis legals de prescripció de responsabilitats. Les dades d'analítica es conserven un màxim de 14 mesos.</p>
<h3>Amb qui les compartim</h3>
<p>No venem ni cedim les teves dades. Per prestar el servei fem servir proveïdors que actuen com a encarregats del tractament: Vercel Inc. (allotjament web), FormSubmit (enviament del formulari de contacte per correu) i Google Ireland Ltd. (Google Analytics i Google Fonts). Alguns poden tractar dades fora de l'Espai Econòmic Europeu, amb les garanties previstes al RGPD (decisió d'adequació UE-EUA o clàusules contractuals tipus).</p>
<h3>Els teus drets</h3>
<p>Pots exercir els drets d'accés, rectificació, supressió, oposició, limitació del tractament i portabilitat, i retirar el consentiment en qualsevol moment, escrivint a <a href="mailto:{c['email']}">{c['email']}</a>. Si consideres que no hem atès correctament la teva sol·licitud, pots reclamar davant l'Agència Espanyola de Protecció de Dades (<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>).</p>
<h2>4. Legislació aplicable</h2>
<p>Aquest avís legal es regeix per la legislació espanyola. Per a qualsevol controvèrsia, les parts se sotmeten als jutjats i tribunals de Barcelona, llevat que la normativa aplicable disposi una altra cosa.</p>
'''
    return f'''
<h1>Legal notice &amp; privacy policy</h1>
<h2>1. Website owner</h2>
<p>In accordance with Spanish Law 34/2002 on information society services and e-commerce (LSSI-CE), this website, <strong>gecanor.com</strong>, is owned by:</p>
<ul>
<li>Company: <strong>{c['legal']}</strong> (trading as “{c['brand']}”)</li>
<li>Tax ID (NIF): {c['nif']}</li>
<li>Registered address: {c['street']}, {c['zip']} {c['city']} (Spain)</li>
<li>Email: <a href="mailto:{c['email']}">{c['email']}</a></li>
</ul>
<h2>2. Terms of use</h2>
<p>Access to this website is free of charge. Users agree to make appropriate use of its content. Texts, images, videos, logos and design belong to {c['legal']} or to third parties who have authorised their use, and may not be reproduced without permission. Client brands shown on the site belong to their respective owners.</p>
<p>{c['legal']} is not responsible for the content of third-party websites reached through links.</p>
<h2>3. Personal data protection</h2>
<h3>Data controller</h3>
<p>{c['legal']}, NIF {c['nif']}, {c['street']}, {c['zip']} {c['city']}, Spain. Contact: <a href="mailto:{c['email']}">{c['email']}</a>.</p>
<h3>What data we process and why</h3>
<ul>
<li><strong>Contact form and emails you send us:</strong> name, email address, company and details of your project, used to answer your enquiry and, where relevant, prepare a proposal. Legal basis: your consent when you contact us and pre-contractual steps taken at your request (Art. 6(1)(a) and 6(1)(b) GDPR).</li>
<li><strong>Web analytics:</strong> only if you accept analytics cookies, pseudonymised browsing data through Google Analytics to understand how the site is used. Legal basis: your consent (Art. 6(1)(a) GDPR). See the <a href="/cookies">cookie policy</a>.</li>
</ul>
<h3>How long we keep it</h3>
<p>Contact data is kept while your enquiry or our relationship is active and afterwards for the statutory limitation periods. Analytics data is kept for a maximum of 14 months.</p>
<h3>Who we share it with</h3>
<p>We do not sell or share your data. We use service providers acting as processors: Vercel Inc. (web hosting), FormSubmit (delivery of the contact form by email) and Google Ireland Ltd. (Google Analytics and Google Fonts). Some may process data outside the European Economic Area under the safeguards provided by the GDPR (EU-US adequacy decision or standard contractual clauses).</p>
<h3>Your rights</h3>
<p>You can exercise your rights of access, rectification, erasure, objection, restriction and portability, and withdraw your consent at any time, by writing to <a href="mailto:{c['email']}">{c['email']}</a>. You may also lodge a complaint with the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">www.aepd.es</a>).</p>
<h2>4. Governing law</h2>
<p>This legal notice is governed by Spanish law. Any dispute shall be submitted to the courts of Barcelona unless applicable law provides otherwise.</p>
'''


def cookies_body(lang):
    rows = {
        'en': [('gecanor-consent', 'gecanor.com (local storage)', 'Stores whether you accepted or rejected analytics cookies.', 'Technical', 'Until you change it'),
               ('gecanor-lang', 'gecanor.com (local storage)', 'Remembers the language you chose.', 'Preferences', 'Until you change it'),
               ('_ga', 'Google Analytics', 'Distinguishes unique visitors (pseudonymous ID).', 'Analytics — only with consent', '2 years'),
               ('_ga_*', 'Google Analytics', 'Keeps the state of the current session.', 'Analytics — only with consent', '2 years')],
        'es': [('gecanor-consent', 'gecanor.com (almacenamiento local)', 'Guarda si has aceptado o rechazado las cookies de analítica.', 'Técnica', 'Hasta que la cambies'),
               ('gecanor-lang', 'gecanor.com (almacenamiento local)', 'Recuerda el idioma que has elegido.', 'Preferencias', 'Hasta que la cambies'),
               ('_ga', 'Google Analytics', 'Distingue visitantes únicos (identificador seudónimo).', 'Analítica — solo con consentimiento', '2 años'),
               ('_ga_*', 'Google Analytics', 'Mantiene el estado de la sesión actual.', 'Analítica — solo con consentimiento', '2 años')],
        'ca': [('gecanor-consent', 'gecanor.com (emmagatzematge local)', 'Desa si has acceptat o rebutjat les galetes d\'analítica.', 'Tècnica', 'Fins que la canviïs'),
               ('gecanor-lang', 'gecanor.com (emmagatzematge local)', 'Recorda l\'idioma que has triat.', 'Preferències', 'Fins que la canviïs'),
               ('_ga', 'Google Analytics', 'Distingeix visitants únics (identificador pseudònim).', 'Analítica — només amb consentiment', '2 anys'),
               ('_ga_*', 'Google Analytics', 'Manté l\'estat de la sessió actual.', 'Analítica — només amb consentiment', '2 anys')],
    }[lang]
    head = {'en': ('Name', 'Provider', 'Purpose', 'Type', 'Duration'),
            'es': ('Nombre', 'Proveedor', 'Finalidad', 'Tipo', 'Duración'),
            'ca': ('Nom', 'Proveïdor', 'Finalitat', 'Tipus', 'Durada')}[lang]
    table = '<table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>' + ''.join(
        '<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in rows) + '</tbody></table>'
    t = {
        'en': dict(h1='Cookie policy',
                   intro='Cookies are small files that a website stores on your device. gecanor.com uses as few as possible: two technical/preference entries that do not identify you, and Google Analytics cookies, which are only set if you accept them.',
                   h_list='Cookies and similar technologies we use',
                   h_manage='Change your choice', manage='You can accept or reject analytics cookies at any time with these buttons. If you reject them, we delete the Google Analytics cookies already stored.',
                   accept='Accept analytics', reject='Reject analytics', status=('Current choice:', 'accepted', 'rejected', 'not set yet'),
                   h_browser='Browser settings', browser='You can also block or delete cookies from your browser settings (Chrome, Safari, Firefox, Edge). Blocking technical storage may affect how the site works.',
                   h_third='Third-party transfers', third='Google may process analytics data outside the EEA under the EU-US Data Privacy Framework. More information: <a href="https://policies.google.com/technologies/cookies" rel="noopener">Google’s cookie policy</a>. For everything else, see our <a href="/legal">legal notice &amp; privacy policy</a>.'),
        'es': dict(h1='Política de cookies',
                   intro='Las cookies son pequeños archivos que una web guarda en tu dispositivo. gecanor.com usa las mínimas: dos elementos técnicos o de preferencias que no te identifican y las cookies de Google Analytics, que solo se activan si las aceptas.',
                   h_list='Cookies y tecnologías similares que usamos',
                   h_manage='Cambia tu elección', manage='Puedes aceptar o rechazar las cookies de analítica en cualquier momento con estos botones. Si las rechazas, borramos las cookies de Google Analytics que ya estuvieran guardadas.',
                   accept='Aceptar analítica', reject='Rechazar analítica', status=('Elección actual:', 'aceptadas', 'rechazadas', 'sin elegir'),
                   h_browser='Configuración del navegador', browser='También puedes bloquear o borrar las cookies desde la configuración de tu navegador (Chrome, Safari, Firefox, Edge). Bloquear el almacenamiento técnico puede afectar al funcionamiento del sitio.',
                   h_third='Transferencias a terceros', third='Google puede tratar los datos de analítica fuera del EEE al amparo del Marco de Privacidad de Datos UE-EE. UU. Más información: <a href="https://policies.google.com/technologies/cookies?hl=es" rel="noopener">política de cookies de Google</a>. Para todo lo demás, consulta el <a href="/es/legal">aviso legal y política de privacidad</a>.'),
        'ca': dict(h1='Política de galetes',
                   intro='Les galetes són petits fitxers que un web desa al teu dispositiu. gecanor.com en fa servir les mínimes: dos elements tècnics o de preferències que no t\'identifiquen i les galetes de Google Analytics, que només s\'activen si les acceptes.',
                   h_list='Galetes i tecnologies similars que fem servir',
                   h_manage='Canvia la teva elecció', manage='Pots acceptar o rebutjar les galetes d\'analítica en qualsevol moment amb aquests botons. Si les rebutges, esborrem les galetes de Google Analytics que ja estiguessin desades.',
                   accept='Acceptar analítica', reject='Rebutjar analítica', status=('Elecció actual:', 'acceptades', 'rebutjades', 'sense triar'),
                   h_browser='Configuració del navegador', browser='També pots bloquejar o esborrar les galetes des de la configuració del navegador (Chrome, Safari, Firefox, Edge). Bloquejar l\'emmagatzematge tècnic pot afectar el funcionament del lloc.',
                   h_third='Transferències a tercers', third='Google pot tractar les dades d\'analítica fora de l\'EEE a l\'empara del Marc de Privacitat de Dades UE-EUA. Més informació: <a href="https://policies.google.com/technologies/cookies?hl=ca" rel="noopener">política de galetes de Google</a>. Per a la resta, consulta l\'<a href="/ca/legal">avís legal i política de privacitat</a>.'),
    }[lang]
    s = t['status']
    return f'''
<h1>{t['h1']}</h1>
<p>{t['intro']}</p>
<h2>{t['h_list']}</h2>
<div class="tbl">{table}</div>
<h2>{t['h_manage']}</h2>
<p>{t['manage']}</p>
<p class="status">{s[0]} <strong id="consent-state">—</strong></p>
<div class="btns"><button type="button" class="primary" data-consent="granted">{t['accept']}</button><button type="button" data-consent="denied">{t['reject']}</button></div>
<script>
(function(){{var L={{granted:{s[1]!r},denied:{s[2]!r},none:{s[3]!r}}};
function paint(){{var v=null;try{{v=localStorage.getItem('gecanor-consent')}}catch(e){{}}document.getElementById('consent-state').textContent=L[v]||L.none;}}
document.querySelectorAll('[data-consent]').forEach(function(b){{b.onclick=function(){{if(window.gecanorConsent)window.gecanorConsent(b.getAttribute('data-consent'));paint();}};}});paint();}})();
</script>
<h2>{t['h_browser']}</h2>
<p>{t['browser']}</p>
<h2>{t['h_third']}</h2>
<p>{t['third']}</p>
'''

STATIC_PAGES = {
    'legal': ('/legal', legal_body),
    'cookies': ('/cookies', cookies_body),
}

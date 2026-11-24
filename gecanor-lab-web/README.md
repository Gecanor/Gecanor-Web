# Gecanor Beauty Tech — web (diseño Lab)

Web estática lista para Vercel. No necesita instalar nada ni compilar.

## Estructura

```
source/                     (fuera de la web publicada)
  pages/*.html              diseño original de cada página (EDITAR AQUÍ)
  content.py                títulos, descripciones SEO, datos de empresa, textos legales
  build.py                  genera la web multidioma

gecanor-lab-web/            (lo que publica Vercel — GENERADO, no editar a mano)
  index.html, services/, resources/, get-started/   → inglés
  es/…, ca/…                                         → español y catalán
  legal/, cookies/ (+ es/, ca/)                      → páginas legales
  sitemap.xml, robots.txt, llms.txt
  consent.js                Google Analytics + aviso de cookies
  support.js                motor de las páginas (no tocar)
  i18n.js, lab-i18n.js      traducciones EN / ES / CAT
  assets/                   vídeos, logos, fotos, imagen para redes (og-gecanor.jpg)
```

## Cómo editar

Cada idioma tiene su propia URL (/, /es, /ca) y el contenido va ya escrito en el HTML
para que Google y las IA lo lean. Por eso las páginas de `gecanor-lab-web/` se generan:

1. Edita `source/pages/<página>.html` (diseño) o `source/content.py` (SEO, textos legales).
   Las traducciones siguen en `gecanor-lab-web/i18n.js` y `lab-i18n.js`.
2. Ejecuta `python3 source/build.py` (necesita Python con `playwright` y Chrome).
3. Sube los cambios a GitHub; Vercel publica solo.

Si cambias algo directamente en `gecanor-lab-web/index.html` u otra página generada,
se perderá la próxima vez que se ejecute el build.

## Probar en local

Hace falta un servidor (abrir el .html con doble clic no carga bien las rutas):

```
cd gecanor-lab-web
npx serve .
```

Abre http://localhost:3000

## Sustituir la web actual en GitHub

1. En GitHub, entra en el repositorio **Gecanor-Web**.
2. Abre la carpeta `gecanor-web` → botón **⋯** (arriba a la derecha) → **Delete directory** → **Commit changes**.
3. Vuelve a la raíz → **Add file → Upload files**.
4. Descomprime el zip y arrastra **la carpeta `gecanor-lab-web` entera** (no el .zip) → **Commit changes**.

## Configurar Vercel (una vez)

En vercel.com → proyecto → **Settings → Build and Deployment**:

- **Root Directory:** `gecanor-lab-web`
- **Framework Preset:** `Other`
- **Build Command:** vacío (desactiva el override y déjalo en blanco)
- **Output Directory:** vacío / `.`
- **Install Command:** vacío

Guarda y en **Deployments** pulsa **⋯ → Redeploy**. A partir de aquí, cada subida a GitHub se publica sola.

## Dominio de GoDaddy

1. Vercel → proyecto → **Settings → Domains** → añade `gecanor.com` y `www.gecanor.com`.
2. GoDaddy → **Mis productos → DNS** del dominio:
   - Registro **A**, nombre `@`, valor `76.76.21.21`
   - Registro **CNAME**, nombre `www`, valor `cname.vercel-dns.com`
   - Borra otros registros A de `@` que apunten a Readymag u otro servicio.
3. Espera (de minutos a unas horas). Vercel activa el HTTPS solo.

Si Vercel te muestra valores DNS distintos en la pantalla de Domains, usa los que te indique Vercel.

## Formulario

Envía a **sonia@gecanor.com** con FormSubmit. La primera vez que alguien envíe el formulario en la web publicada, llegará a sonia@gecanor.com un email "Activate Form": hay que pulsar el botón (mira también en spam). Si FormSubmit no responde, se abre el correo del visitante con la consulta redactada.

## Servicios externos que usa

- Google Fonts (Archivo, IBM Plex Mono) y Fontshare (Satoshi, gratuita uso comercial — revisa su licencia).
- React y Babel desde unpkg.com.
- FormSubmit para el formulario.

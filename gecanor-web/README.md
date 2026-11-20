# Gecanor Beauty Tech — web (diseño Lab)

Web estática lista para Vercel. No necesita instalar nada ni compilar.

## Estructura

```
gecanor-lab-web/
  index.html              → /
  services/index.html     → /services
  get-started/index.html  → /get-started
  support.js              motor de las páginas (no tocar)
  i18n.js, lab-i18n.js    traducciones EN / ES / CAT
  vercel.json             URLs limpias + caché de assets
  assets/                 vídeos, logos, fotos
```

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

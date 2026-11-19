# Gecanor — Web (Next.js)

Web corporativa de Gecanor Beauty Tech. Tres páginas: Home, Services y Get Started, con selector de idioma EN / ES / CAT, vídeos de proyecto con carga diferida y todas las animaciones del diseño original.

- **Framework:** Next.js 14 (App Router) + React 18
- **Estilos:** CSS global mínimo (resets, keyframes, media queries) + estilos en línea, exactamente los valores del diseño
- **Sin backend.** El formulario abre el correo del visitante con los datos ya redactados hacia `sonia@gecanor.com`

---

## 1. Ejecutar la web en tu ordenador

Necesitas **Node.js 18.17 o superior**. Compruébalo con `node -v`; si no lo tienes, descárgalo de [nodejs.org](https://nodejs.org) (versión LTS).

1. Abre el Terminal (Mac) o PowerShell (Windows).
2. Entra en la carpeta del proyecto:
   ```bash
   cd ruta/hasta/gecanor-web
   ```
3. Instala las dependencias (solo la primera vez):
   ```bash
   npm install
   ```
4. Arranca el servidor de desarrollo:
   ```bash
   npm run dev
   ```
5. Abre <http://localhost:3000> en el navegador. Los cambios que guardes se recargan solos.

Para comprobar la versión de producción antes de publicar:

```bash
npm run build
npm start
```

`npm run build` debe terminar sin errores. Si falla, el mensaje indica el archivo y la línea.

---

## 2. Subir el proyecto a GitHub

1. Crea una cuenta en [github.com](https://github.com) si no la tienes.
2. En GitHub: botón **+** (arriba derecha) → **New repository**.
   - Repository name: `gecanor-web`
   - Visibilidad: **Private** (recomendado)
   - **No** marques "Add a README file"
   - **Create repository**
3. En el Terminal, dentro de la carpeta del proyecto:
   ```bash
   git init
   git add .
   git commit -m "Gecanor web"
   git branch -M main
   git remote add origin https://github.com/TU-USUARIO/gecanor-web.git
   git push -u origin main
   ```
   Sustituye `TU-USUARIO` por tu usuario de GitHub. Si pide credenciales, usa tu usuario y un **Personal Access Token** (GitHub → Settings → Developer settings → Personal access tokens → Generate new token, con permiso `repo`).

Para subir cambios más adelante:

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

> Los vídeos ocupan bastante. GitHub avisa a partir de 50 MB por archivo y rechaza los de más de 100 MB. Si algún `.mp4` supera los 100 MB, comprímelo antes de subirlo (ver sección 5).

---

## 3. Desplegar en Vercel

1. Entra en [vercel.com](https://vercel.com) y regístrate con **Continue with GitHub**.
2. **Add New… → Project**.
3. Vercel lista tus repositorios: pulsa **Import** en `gecanor-web`.
4. No cambies nada en la pantalla de configuración. Vercel detecta Next.js solo:
   - Framework Preset: **Next.js**
   - Build Command: `next build`
   - Output Directory: (vacío)
   - Root Directory: la carpeta que contiene el `package.json`. Si subiste el repositorio con la carpeta `gecanor-web` dentro, escribe `gecanor-web` aquí.
5. **Deploy**. Tarda 1–3 minutos.
6. Al terminar tendrás una URL tipo `https://gecanor-web.vercel.app`. Ábrela y revisa la web.

A partir de ahora, cada `git push` a `main` publica automáticamente.

---

## 4. Conectar tu dominio de GoDaddy

### En Vercel

1. Abre tu proyecto → pestaña **Settings** → **Domains**.
2. Escribe tu dominio (por ejemplo `gecanor.com`) y pulsa **Add**.
3. Añade también `www.gecanor.com` cuando te lo ofrezca. Vercel te mostrará los registros DNS que necesitas. Serán estos:

   | Tipo  | Nombre (Host) | Valor                    |
   |-------|---------------|--------------------------|
   | A     | `@`           | `76.76.21.21`            |
   | CNAME | `www`         | `cname.vercel-dns.com`   |

   Usa siempre los valores exactos que muestre tu panel de Vercel, no estos de memoria: pueden cambiar.

### En GoDaddy

4. Entra en [godaddy.com](https://godaddy.com) → **Mis productos** → junto al dominio, **DNS** (o "Administrar DNS").
5. En **Registros**:
   - Busca el registro **A** con Nombre `@`. Pulsa el lápiz (editar) y pon como Valor `76.76.21.21`. TTL: 1 hora. **Guardar**.
   - Busca el **CNAME** con Nombre `www`. Edítalo y pon como Valor `cname.vercel-dns.com`. **Guardar**.
   - Si GoDaddy tiene un registro A o CNAME de aparcamiento (`Parked`, `_domainconnect`, redirecciones a "Coming soon"), bórralo o desactívalo: interfiere.
6. Si GoDaddy muestra un **reenvío de dominio** (Domain Forwarding) activo, elimínalo.

### Esperar y comprobar

7. Los cambios de DNS tardan entre 10 minutos y 48 horas (normalmente menos de 1 hora).
8. Vuelve a Vercel → Settings → Domains. Cuando aparezca **Valid Configuration** en verde, tu dominio ya sirve la web con HTTPS automático.
9. Abre `https://gecanor.com` y `https://www.gecanor.com` para confirmar.

---

## 5. Recursos que debes sustituir tú

Todos los archivos están en `public/assets/`. Para cambiar cualquiera, sustituye el archivo **manteniendo el mismo nombre**: no hay que tocar el código.

### Ya optimizado

Las imágenes del proyecto ya están redimensionadas y listas para producción:

| Archivo | Antes | Ahora |
|---|---|---|
| `gecanor-logo.png` | 8192 × 3458 px | **1800 × 760 px** |
| `gecanor-logo-white.png` | 8192 × 3458 px | **600 × 253 px** |
| `oficina.png` | 2340 × 4156 px | **1600 × 2842 px** |
| 8 logos de marca (`brand-*.png`) | hasta 8192 px de ancho | **600 px de ancho** |

Los SVG (`gr.svg`, `brand-xskinlab.svg`, `brand-clara.svg`) son vectoriales: no necesitan optimización.

El icono de pestaña se genera en `app/icon.png` a partir de la marca `gr.`; sustituye ese archivo si quieres otro.

### Vídeos: dos pendientes de comprimir

Los 14 vídeos suman unos **31 MB**, pero solo el de portada se descarga al entrar: los 13 de proyecto cargan de forma diferida al acercarse a la pantalla y se pausan al salir. Doce de ellos pesan entre 1 y 2,8 MB, un tamaño correcto para web.

Solo conviene comprimir estos dos:

| Archivo | Peso actual | Objetivo |
|---|---|---|
| `public/assets/hero.mp4` | 5,8 MB | **2–3 MB** (es lo primero que carga la web) |
| `public/assets/proj-gloa.mp4` | 5,3 MB | **1,5–2 MB** |

Comprímelos con [ffmpeg](https://ffmpeg.org) sin cambiar el nombre del archivo:

```bash
# portada (mantener 1920 px de ancho)
ffmpeg -i hero.mp4 -vf "scale=1920:-2" -c:v libx264 -crf 27 -preset slow -movflags +faststart -an hero-nuevo.mp4

# vídeo de proyecto (1280 px basta: se muestra a media columna)
ffmpeg -i proj-gloa.mp4 -vf "scale=1280:-2" -c:v libx264 -crf 27 -preset slow -movflags +faststart -an proj-gloa-nuevo.mp4
```

Si no tienes ffmpeg, sube los dos archivos a un compresor web (por ejemplo [freeconvert.com/video-compressor](https://www.freeconvert.com/video-compressor)) y descarga el resultado con el mismo nombre.

### Recursos que faltan

| Recurso | Dónde va | Nota |
|---|---|---|
| Webs de **Evara haircare**, **Cosmefarm** y **Orae Supplements** | `lib/data.js`, campo `href` de cada proyecto (ahora `'#work'`) | Cuando tengas las URLs, sustitúyelas ahí |
| Imagen para compartir en redes (1200×630 px) | `public/og-image.png` | Avísame y la conecto en `app/layout.jsx` |

### Tipografía y licencias

- La tipografía es **Inter**, servida por Google Fonts a través de `next/font` (licencia SIL Open Font License, uso comercial libre). No hay que instalar nada.
- Los logos de las 11 marcas y los vídeos de proyecto son material de tus clientes. Asegúrate de tener su permiso para mostrarlos.
- No se ha usado ninguna imagen, icono o fuente de terceros con copyright.

---

## 6. Formulario de contacto

El formulario de **Get Started** envía las consultas directamente a **sonia@gecanor.com** a través de [FormSubmit](https://formsubmit.co), un servicio gratuito sin registro. El visitante no necesita tener correo configurado: pulsa Submit, ve "SENT" y el email llega a la bandeja.

### Activación (solo una vez, obligatoria)

1. Publica la web y envía **una consulta de prueba** desde el formulario.
2. FormSubmit mandará a sonia@gecanor.com un email titulado **"Action Required: Activate FormSubmit on…"**. Revisa también spam.
3. Pulsa **Activate Form** en ese email.
4. A partir de ahí, cada consulta llega a sonia@gecanor.com como una tabla con todos los campos. Si respondes al email, la respuesta va directamente al email del cliente.

Hasta que no se active, las consultas no se entregan.

### Ocultar la dirección (recomendado)

Tras activar, FormSubmit envía un segundo email con una dirección alias (una cadena aleatoria). Sustituye el email por ese alias en `app/get-started/page.jsx`:

```js
const CONTACT_EMAIL = 'el-alias-que-te-envían';
```

Así sonia@gecanor.com no aparece en el código público y recibe menos spam.

## 7. Estructura de archivos

```
gecanor-web/
├── app/
│   ├── globals.css            Resets, keyframes (grSpin, grMarquee, grCue) y media queries
│   ├── layout.jsx             Layout raíz, fuente Inter, metadatos SEO, LangProvider
│   ├── page.jsx               Home
│   ├── services/page.jsx      Services
│   └── get-started/page.jsx   Get Started (formulario)
├── components/
│   ├── LangProvider.jsx       Contexto de idioma + persistencia en localStorage
│   ├── TopNav.jsx             Get Started + selector EN / ES / CAT
│   ├── PinnedLogo.jsx         Logo gr. fijo animado (máscara SVG)
│   ├── Footer.jsx             Footer común a las tres páginas
│   └── WorkWithUs.jsx         Banda negra "Work with us!"
├── lib/
│   ├── data.js                Proyectos, marcas, servicios, textos de lista
│   └── i18n.js                Diccionario EN / ES / CAT y motor de traducción
├── public/assets/             Vídeos, logos e imágenes
├── package.json
├── next.config.mjs
├── jsconfig.json              Alias @/ para importar
└── .gitignore
```

---

## 8. Cómo editar el contenido

| Qué quieres cambiar | Archivo |
|---|---|
| Proyectos del Work (nombre, web, vídeo, etiquetas) | `lib/data.js` → `PROJECTS` |
| Logos del muro de marcas y su tamaño (`w` en px) | `lib/data.js` → `BRANDS_TOP`, `BRANDS_BOTTOM` |
| Las 7 líneas de servicios de la Home | `lib/data.js` → `STATEMENT_LINES` |
| Textos de la página Services | `app/services/page.jsx` y `lib/data.js` |
| Traducciones al español y catalán | `lib/i18n.js` |
| Direcciones, email, copyright | `components/Footer.jsx` y `app/page.jsx` |

La traducción funciona por diccionario: cada texto en inglés tiene su equivalente en `lib/i18n.js`. Si añades un texto nuevo en inglés y quieres que se traduzca, añade su entrada allí con el mismo texto exacto como clave.

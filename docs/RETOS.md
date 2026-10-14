# Problemas que resolví

[← Volver al inicio](../README.md)

Problemas reales del proyecto, muchos encontrados probando en un iPhone real. Para cada uno está el síntoma, la causa raíz y la solución. Los marcados con ⚠️ se previnieron antes de que llegaran a producción.

## Móvil e iOS

| Síntoma | Causa raíz | Solución |
|---|---|---|
| El botón "Confirmar" no llegaba al RSVP en el celular | `scroll-snap-stop: always` bloquea los saltos directos a un ancla | Quitarlo: se sacrifica el enganche forzado en scroll rápido a cambio de que los botones funcionen |
| El salto "rebotaba" a la sección anterior, solo en iPhone | Bug conocido de iOS Safari con scroll-snap + salto de ancla | Apagar `scroll-snap-type` durante el `scrollIntoView` y prenderlo después ([ver código](../fragmentos/salto_de_ancla_ios.js)) |
| La música no sonaba sola | Los navegadores bloquean el autoplay con sonido, sobre todo en móvil | Botón flotante: el toque del usuario es la interacción que exige el navegador. En los diseños con apertura, el mismo toque que abre la invitación arranca la canción |
| ⚠️ El latido hecho con Web Audio no sonaría con el switch de silencio del iPhone | Safari trata el audio web como "ambiente" | `navigator.audioSession.type = 'playback'` (Safari 17+) |
| El fondo fijo brincaba al esconderse la barra de Safari | `100vh` cambia de tamaño con la barra | Escena `position: fixed` con altura `100lvh`; `background-attachment: fixed` no funciona en iPhone |
| La canción no cargaba al cambiar de red o al abrir por HTTPS | La URL se guardaba con la IP de la compu (contenido mixto) | Si apunta a nuestro `/static/`, usar solo la ruta relativa |

## Backend y Django

| Síntoma | Causa raíz | Solución |
|---|---|---|
| El RSVP devolvía 403 | La cookie `csrftoken` nunca se generaba: el template no usa `{% csrf_token %}` | `@ensure_csrf_cookie` en la vista y el token en el header `X-CSRFToken` del `fetch` |
| El countdown iba 6 horas adelantado | `TIME_ZONE = 'UTC'`: la hora capturada se tomaba como UTC | `TIME_ZONE = 'America/Mexico_City'` |
| ⚠️ El anti-spam habría bloqueado a todos los invitados a la vez | `REMOTE_ADDR` es el balanceador del hosting, igual para todos | Leer la IP real de la cabecera del balanceador, configurable por settings |
| El RSVP daba 403 a través del túnel HTTPS de pruebas | El `Origin` del túnel no estaba en `CSRF_TRUSTED_ORIGINS` | Aceptar los dominios del túnel solo en `DEBUG` |
| Las fotos de la galería daban 404 | No existían `MEDIA_URL` ni `MEDIA_ROOT` | Configurarlos y servir `/media/` en desarrollo |

## JavaScript y CSS

| Síntoma | Causa raíz | Solución |
|---|---|---|
| El botón de música a veces no pausaba | Su listener se registraba dentro del countdown, que corre cada segundo: un listener nuevo por segundo | Registrar el listener una sola vez, fuera del intervalo |
| Cambios de CSS que "no se aplicaban" | Un bloque duplicado más abajo ganaba por la cascada | Una sola regla por selector, organizada por secciones en el orden visual |
| Páginas en blanco entre secciones | Secciones de `100vh` sin contenido (galería sin fotos) | Pintarlas solo si hay datos |
| Las tarjetas de un diseño desacomodaban la cuadrícula | Un `::before` en un grid ocupa una celda de la colocación automática | `::before` absoluto anclado al área completa del grid (`grid-area: 1 / 1 / -1 / -1`) |
| Una cornisa absoluta desbordaba la pantalla 27 px | Una regla `.rsvp > * {width: 100%}` también le pegaba | Excluirla con `:not(.cornisa, .folio)` dentro de `:where()` para no subir la especificidad |
| En una animación con `<use>` de SVG, los estados no cambiaban | Los selectores CSS no entran a la copia que crea `<use>` | Cambiar variables CSS, que sí se heredan dentro de la copia |

## Tipografía

| Síntoma | Causa raíz | Solución |
|---|---|---|
| "Mateo" se leía "Matco" | El eje de tamaño óptico (`opsz`) en automático adelgaza los trazos finos a tamaños grandes | Fijar `opsz` a ~30-40 % del tamaño real |
| "MISIÓN" se leía "MISIóN" en letra pixel | Press Start 2P encoge las mayúsculas con acento | Cambiar a Pixelify Sans |
| En el marcador, el 5 parecía S | Letra pixel | Los números en VT323 |
| "Sáb" salía "Sab" | `date:"D"` de Django da la abreviatura sin acento | `date:"l"\|slice:":3"` |

# Fragmentos del código

[← Volver al inicio](../README.md)

Piezas representativas, tal como están en el proyecto. El código completo es privado; si quieres revisarlo, pídeme acceso.

| Archivo | Qué muestra |
|---|---|
| [`limite_de_envios.py`](limite_de_envios.py) | Rate limit propio sobre la caché de Django: ventanas fijas por conexión y por invitación, IP solo como hash y manejo correcto de la IP detrás de un balanceador. |
| [`fotos_de_clientes.py`](fotos_de_clientes.py) | Procesamiento de las fotos que suben los clientes: verificación con Pillow, rotación EXIF, redimensión, JPEG optimizado y eliminación del GPS. |
| [`niveles_de_paquete.py`](niveles_de_paquete.py) | Cómo la vista cruza el paquete pagado con lo que soporta el diseño, y arma el template desde el `slug_tema`. |
| [`salto_de_ancla_ios.js`](salto_de_ancla_ios.js) | El arreglo para el bug de iOS Safari con scroll-snap y saltos de ancla. |

Los comentarios están en español porque es el idioma en el que trabajo el proyecto.

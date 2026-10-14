"""
Fragmento de views.py: la vista cruza el paquete que pagó el cliente
(imagen / interactiva / premium) con lo que soporta el diseño elegido.
Así un cliente de paquete básico nunca ve funciones que no compró,
y ningún diseño pinta una sección que no sabe dibujar.
"""


def _pintar_invitacion(request, invitacion, **extra):
    """La invitación con su plantilla. La usan la vista pública y la vista previa del pedido."""
    contexto = {
        "invitacion": invitacion,
        "plantilla": invitacion.plantilla,
        # nivel controla qué bloques pinta el template (ver comentario en el HTML)
        "mostrar_rsvp": invitacion.nivel != "imagen" and invitacion.plantilla.soporta_rsvp,
        "mostrar_musica": invitacion.nivel == "premium" and invitacion.plantilla.soporta_musica,
        "mostrar_galeria": invitacion.nivel != "imagen" and invitacion.plantilla.soporta_galeria,
        "iconos_pwa": iconos_pwa(invitacion.plantilla),
        # la foto de la portada (o la primera de la galería); la piden los diseños con foto
        "foto_portada": invitacion.foto_portada_src,
    }
    votacion = _votacion_habilitada(invitacion)
    contexto["mostrar_votacion"] = votacion is not None
    contexto["votacion"] = votacion or {}
    contexto.update(extra)
    # el nombre de la plantilla HTML sale del slug_tema, así cada diseño
    # es literalmente un archivo distinto y no si/else gigantes en un solo template
    return render(request, f"invitaciones/temas/{invitacion.plantilla.slug_tema}.html", contexto)

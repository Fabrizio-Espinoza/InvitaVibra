// Fragmento del motor (base_interactiva.html).
// La invitación se divide en pantallas de 100dvh enganchadas con CSS scroll-snap.
// En iOS Safari, saltar a un #ancla con scroll-snap activo "rebota" a la
// pantalla anterior. Se reprodujo en un iPhone real y se resolvió así:

// --- Arreglo para un bug de iOS Safari: cuando scroll-snap está activo,
// saltar a un #ancla a veces "rebota" de vuelta a la sección anterior.
// La solución: apagar el snap justo antes de saltar, y prenderlo de
// nuevo cuando la animación de scroll ya terminó.
document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', function (e) {
        const destino = document.querySelector(this.getAttribute('href'));
        if (!destino) return;
        e.preventDefault();

        document.documentElement.style.scrollSnapType = 'none';
        destino.scrollIntoView({ behavior: 'smooth', block: 'start' });

        setTimeout(() => {
            document.documentElement.style.scrollSnapType = '';
        }, 1000);
    });
});

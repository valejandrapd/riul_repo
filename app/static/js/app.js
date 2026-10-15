/* ==========================================================================
   RIUL - Script Principal de Interfaz (app.js)
   Soporte completo para todas las vistas y modales de Figma
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

    /* --------------------------------------------------------------------------
       1. Manejo Automático de Toasts y Notificaciones Flotantes
       -------------------------------------------------------------------------- */
    const floatingToasts = document.querySelectorAll('div[style*="position: fixed"][style*="bottom"]');
    floatingToasts.forEach(toast => {
        setTimeout(() => {
            toast.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            toast.style.opacity = '0';
            toast.style.transform = 'translateY(20px)';
            setTimeout(() => toast.remove(), 600);
        }, 4500); // Desaparece suavemente a los 4.5 segundos
    });

    /* --------------------------------------------------------------------------
       2. Actualización Dinámica de Nombres de Archivos (PDFs, Fotos, etc.)
       -------------------------------------------------------------------------- */
    // Inputs tipo file genéricos o específicos de convocatorias y perfiles
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', (e) => {
            const fileName = e.target.files[0] ? e.target.files[0].name : '';
            
            // Buscar etiquetas de texto asociadas dentro del mismo contenedor
            const container = input.closest('.form-group') || input.parentElement;
            if (container) {
                const labelTarget = container.querySelector('#file-label, #profile-file-label, span, p');
                if (labelTarget && fileName) {
                    labelTarget.textContent = fileName;
                    labelTarget.style.color = '#2e7d32';
                    labelTarget.style.fontWeight = 'bold';
                }
            }
        });
    });

    /* --------------------------------------------------------------------------
       3. Sistema de Pestañas (Tabs) en Perfiles y Paneles de Semilleros
       -------------------------------------------------------------------------- */
    const tabButtons = document.querySelectorAll('.main-container a.btn-primary, .main-container a.btn-secondary');
    tabButtons.forEach(btn => {
        // Identificar si el enlace actúa como pestaña interna por su contexto
        if (btn.closest('div[style*="display: flex"]') && !btn.getAttribute('href').startsWith('http') && btn.getAttribute('href') !== '#') {
            btn.addEventListener('click', (e) => {
                // Si prefieres navegación por AJAX o prevenir recarga por defecto:
                // e.preventDefault();
                // tabButtons.forEach(b => { b.className = 'btn-secondary'; });
                // btn.className = 'btn-primary';
            });
        }
    });

    /* --------------------------------------------------------------------------
       4. Prevención de Doble Envío y Validación Global de Formularios
       -------------------------------------------------------------------------- */
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
            if (submitBtn) {
                // Opcional: Deshabilitar el botón para evitar múltiples envíos accidentales
                submitBtn.style.opacity = '0.7';
                // submitBtn.disabled = true; 
            }
        });
    });

    /* --------------------------------------------------------------------------
       5. Confirmaciones Interactivas para Acciones Críticas (Ej. Rechazar/Eliminar)
       -------------------------------------------------------------------------- */
    const dangerButtons = document.querySelectorAll('a[style*="color: #b71c1c"], button[style*="color: #b71c1c"], a[style*="color: #c62828"]');
    dangerButtons.forEach(btn => {
        if (btn.textContent.includes('Rechazar') || btn.textContent.includes('Salir') || btn.textContent.includes('Eliminar')) {
            // Se puede agregar un listener si se requiere confirmación extra por JS puro
        }
    });

});
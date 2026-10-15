/* ==========================================================================
   RIUL - Capa de Servicios API (api.js)
   Manejo de peticiones asíncronas Fetch para Flask (Corte 2)
   ========================================================================== */

const API = {
    /**
     * Realiza una petición GET genérica
     * @param {string} endpoint - Ruta de la API o endpoint de Flask
     */
    async get(endpoint) {
        try {
            const response = await fetch(endpoint, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API GET Error:', error);
            throw error;
        }
    },

    /**
     * Realiza una petición POST enviando datos JSON
     * @param {string} endpoint - Ruta de la API o endpoint de Flask
     * @param {Object} data - Objeto con los datos a enviar
     */
    async post(endpoint, data) {
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify(data)
            });
            if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API POST Error:', error);
            throw error;
        }
    },

    /**
     * Envía formularios con archivos adjuntos (FormData) como PDFs o imágenes
     * Ideal para crear convocatorias institucionales o registrar evidencias
     * @param {string} endpoint - Ruta de la API o endpoint de Flask
     * @param {FormData} formData - Instancia de FormData con campos y archivos
     */
    async postFormData(endpoint, formData) {
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                    // Nota: No se define 'Content-Type' manualmente para que el navegador asigne el boundary multipart/form-data correcto
                },
                body: formData
            });
            if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API PostFormData Error:', error);
            throw error;
        }
    }
};

// Exportar globalmente para consumo en vistas o app.js
window.RIUL_API = API;
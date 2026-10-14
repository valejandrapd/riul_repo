-- ============================================================
-- SCRIPT DML: CARGA DE DATOS INICIALES (RIUL)
-- ============================================================

USE riul_db;

-- 1. Insertar Facultades y Programas
INSERT INTO facultad (nombre, descripcion) VALUES
('Ingeniería', 'Facultad de Ingeniería - Sede Principal'),
('Derecho', 'Facultad de Derecho y Ciencias Sociales');

INSERT INTO programa_academico (nombre, id_facultad) VALUES
('Ingeniería de Sistemas', 1),
('Ingeniería Industrial', 1),
('Derecho', 2);

-- 2. Insertar Usuarios de Prueba (Cumpliendo la restricción @unilibre.edu.co)
INSERT INTO usuario (nombre, apellido, correo, contrasena_hash, rol, id_programa, puntos_xp) VALUES
('Admin', 'RIUL', 'admin@unilibre.edu.co', 'scrypt:32768:8:1$hash_admin', 'ADMIN', 1, 500),
('Carlos', 'Mendoza', 'carlos.mendoza@unilibre.edu.co', 'scrypt:32768:8:1$hash_docente', 'DOCENTE_LIDER', 1, 350),
('Ana', 'Gomez', 'ana.gomez@unilibre.edu.co', 'scrypt:32768:8:1$hash_estudiante', 'ESTUDIANTE_INVESTIGADOR', 1, 120);

-- 3. Insertar Semillero y Proyecto
INSERT INTO semillero (nombre, sigla, descripcion, linea_investigacion, id_lider, nivel_estrellas) VALUES
('Semillero de Inteligencia Artificial y Software', 'SIAS', 'Enfocado en desarrollo de software moderno y aprendizaje automático.', 'Ingeniería de Software y datos', 2, 5);

INSERT INTO proyecto (titulo, resumen, estado, porcentaje_avance, fecha_inicio, id_semillero) VALUES
('Plataforma Web RIUL con Gamificación', 'Desarrollo de un sistema de gestión de investigación para la UniLibre.', 'EN_EJECUCION', 65.00, '2026-02-01', 1);

-- 4. Insignias de Gamificación
INSERT INTO insignia (nombre, descripcion, icono_url, puntos_requeridos) VALUES
('Primer Aporte', 'Otorgada por subir la primera evidencia de investigación.', '/assets/badges/badge1.png', 50),
('Ponente Estrella', 'Otorgada por presentar una ponencia en evento institucional.', '/assets/badges/badge2.png', 150);

INSERT INTO usuario_insignia (id_usuario, id_insignia) VALUES (3, 1);
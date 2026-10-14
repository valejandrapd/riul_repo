-- ============================================================
-- SCRIPT DDL: BASE DE DATOS RIUL (Red de Investigación UniLibre)
-- Motor: MySQL 8.0 / MariaDB
-- ============================================================

DROP DATABASE IF EXISTS riul_db;
CREATE DATABASE riul_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE riul_db;

-- ------------------------------------------------------------
-- 1. ESTRUCTURA ACADÉMICA Y USUARIOS
-- ------------------------------------------------------------

CREATE TABLE facultad (
    id_facultad INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL UNIQUE,
    descripcion TEXT
) ENGINE=InnoDB;

CREATE TABLE programa_academico (
    id_programa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    id_facultad INT NOT NULL,
    FOREIGN KEY (id_facultad) REFERENCES facultad(id_facultad) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    contrasena_hash VARCHAR(255) NOT NULL,
    rol ENUM('ADMIN', 'DOCENTE_LIDER', 'ESTUDIANTE_INVESTIGADOR', 'VISITANTE') NOT NULL DEFAULT 'ESTUDIANTE_INVESTIGADOR',
    id_programa INT,
    puntos_xp INT DEFAULT 0,
    activo BOOLEAN DEFAULT TRUE,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_correo_unilibre CHECK (correo LIKE '%@unilibre.edu.co')
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- 2. SEMILLEROS Y VINCULACIÓN
-- ------------------------------------------------------------

CREATE TABLE semillero (
    id_semillero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL UNIQUE,
    sigla VARCHAR(20),
    descripcion TEXT NOT NULL,
    linea_investigacion VARCHAR(200) NOT NULL,
    id_lider INT NOT NULL,
    nivel_estrellas INT DEFAULT 1,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_lider) REFERENCES usuario(id_usuario) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE solicitud_vinculacion (
    id_solicitud INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_semillero INT NOT NULL,
    estado ENUM('PENDIENTE', 'APROBADO', 'RECHAZADO') DEFAULT 'PENDIENTE',
    mensaje TEXT,
    fecha_solicitud TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_estudiante) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_semillero) REFERENCES semillero(id_semillero) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE integrante_semillero (
    id_usuario INT NOT NULL,
    id_semillero INT NOT NULL,
    rol_semillero VARCHAR(50) DEFAULT 'Miembro',
    fecha_ingreso DATE NOT NULL,
    PRIMARY KEY (id_usuario, id_semillero),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_semillero) REFERENCES semillero(id_semillero) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- 3. PROYECTOS Y PUBLICACIONES ACADÉMICAS
-- ------------------------------------------------------------

CREATE TABLE proyecto (
    id_proyecto INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    resumen TEXT,
    estado ENUM('FORMULACION', 'EN_EJECUCION', 'FINALIZADO', 'CANCELADO') DEFAULT 'FORMULACION',
    porcentaje_avance DECIMAL(5,2) DEFAULT 0.00,
    fecha_inicio DATE,
    fecha_fin DATE,
    id_semillero INT NOT NULL,
    FOREIGN KEY (id_semillero) REFERENCES semillero(id_semillero) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE publicacion (
    id_publicacion INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    resumen TEXT,
    tipo ENUM('ARTICULO', 'PONENCIA', 'LIBRO', 'PATENTE', 'POSTER') NOT NULL,
    url_documento VARCHAR(255),
    fecha_publicacion DATE NOT NULL,
    id_proyecto INT,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE autor_publicacion (
    id_usuario INT NOT NULL,
    id_publicacion INT NOT NULL,
    es_autor_principal BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id_usuario, id_publicacion),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion) ON DELETE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- 4. GAMIFICACIÓN, LOGROS E INSIGNIAS
-- ------------------------------------------------------------

CREATE TABLE insignia (
    id_insignia INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT NOT NULL,
    icono_url VARCHAR(255),
    puntos_requeridos INT DEFAULT 0
) ENGINE=InnoDB;

CREATE TABLE usuario_insignia (
    id_usuario INT NOT NULL,
    id_insignia INT NOT NULL,
    fecha_otorgado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_usuario, id_insignia),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_insignia) REFERENCES insignia(id_insignia) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE logro_evidencia (
    id_logro INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    archivo_evidencia VARCHAR(255) NOT NULL,
    puntos_otorgados INT DEFAULT 0,
    estado ENUM('EN_REVISION', 'APROBADO', 'RECHAZADO') DEFAULT 'EN_REVISION',
    id_evaluador INT,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_estudiante) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_evaluador) REFERENCES usuario(id_usuario) ON DELETE SET NULL
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- 5. CONVOCATORIAS E INTERACCIONES
-- ------------------------------------------------------------

CREATE TABLE convocatoria (
    id_convocatoria INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_apertura DATE NOT NULL,
    fecha_cierre DATE NOT NULL,
    monto_financiacion DECIMAL(12,2) DEFAULT 0.00,
    activa BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

CREATE TABLE comentario_feed (
    id_comentario INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_publicacion INT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_comentario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    FOREIGN KEY (id_publicacion) REFERENCES publicacion(id_publicacion) ON DELETE CASCADE
) ENGINE=InnoDB;
from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Config
from app.extensions import db

# Importación de Blueprints
from app.routes.auth_routes import auth_bp
from app.routes.web_routes import web_bp
from app.routes.usuario_routes import usuario_bp
from app.routes.semillero_routes import semillero_bp
from app.routes.proyecto_routes import proyecto_bp
from app.routes.convocatoria_routes import convocatoria_bp
from app.routes.insignia_routes import insignia_bp
from app.routes.publicacion_routes import publicacion_bp
from app.routes.facultad_routes import facultad_bp
from app.routes.programa_academico_routes import programa_bp
from app.routes.logro_evidencia_routes import logro_bp
from app.routes.solicitud_vinculacion_routes import solicitud_bp

def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config.from_object(Config)

    db.init_app(app)
    JWTManager(app)

    # Registro de Blueprints
    app.register_blueprint(web_bp)
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(usuario_bp, url_prefix="/api/usuarios")
    app.register_blueprint(semillero_bp, url_prefix="/api/semilleros")
    app.register_blueprint(proyecto_bp, url_prefix="/api/proyectos")
    app.register_blueprint(convocatoria_bp, url_prefix="/api/convocatorias")
    app.register_blueprint(insignia_bp, url_prefix="/api/insignias")
    app.register_blueprint(publicacion_bp, url_prefix="/api/publicaciones")
    app.register_blueprint(facultad_bp, url_prefix="/api/facultades")
    app.register_blueprint(programa_bp, url_prefix="/api/programas")
    app.register_blueprint(logro_bp, url_prefix="/api/logros")
    app.register_blueprint(solicitud_bp, url_prefix="/api/solicitudes")

    return app
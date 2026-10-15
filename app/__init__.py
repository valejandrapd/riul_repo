from flask import Flask
from flask_jwt_extended import JWTManager

from app.config import Config
from app.extensions import db

# Importamos las rutas (Blueprints) de RIUL
from app.routes.auth_routes import auth_bp
from app.routes.web_routes import web_bp


def create_app():

    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates"
    )

    app.config.from_object(Config)

    db.init_app(app)

    JWTManager(app)

    # Registro de Blueprints / Rutas
    app.register_blueprint(web_bp)  # Rutas HTML (login, dashboards)

    app.register_blueprint(
        auth_bp,
        url_prefix="/api/auth"
    )

    with app.app_context():
        # Importamos todos los modelos para que SQLAlchemy reconozca las tablas de RIUL
        from app.models.user import User
        # Aquamas adelante importaremos los modelos de RIUL (Semillero, Proyecto, Insignia, etc.)

        # db.create_all()  # Opcional, ya que los scripts schema.sql y seed.sql en Docker crean todo en MySQL

    return app
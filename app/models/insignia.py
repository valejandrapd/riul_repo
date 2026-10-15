from app.extensions import db

class Insignia(db.Model):
    __tablename__ = 'insignia'

    id_insignia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    icono_url = db.Column(db.String(255))
    puntos_requeridos = db.Column(db.Integer, default=0)
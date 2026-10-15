from app.extensions import db

class Facultad(db.Model):
    __tablename__ = 'facultad'

    id_facultad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
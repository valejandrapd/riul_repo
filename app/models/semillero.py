from app.extensions import db

class Semillero(db.Model):
    __tablename__ = 'semillero'

    id_semillero = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    sigla = db.Column(db.String(20))
    descripcion = db.Column(db.Text)
    linea_investigacion = db.Column(db.String(150))
    id_lider = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    nivel_estrellas = db.Column(db.Integer, default=1)
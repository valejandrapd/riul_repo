from app.extensions import db

class AutorPublicacion(db.Model):
    __tablename__ = 'autor_publicacion'

    id_publicacion = db.Column(db.Integer, db.ForeignKey('publicacion.id_publicacion'), primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), primary_key=True)
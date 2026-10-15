from app.extensions import db

class Publicacion(db.Model):
    __tablename__ = 'publicacion'

    id_publicacion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
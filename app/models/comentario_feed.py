from app.extensions import db

class ComentarioFeed(db.Model):
    __tablename__ = 'comentario_feed'

    id_comentario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    contenido = db.Column(db.Text, nullable=False)
    fecha_comentario = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    id_publicacion = db.Column(db.Integer, db.ForeignKey('publicacion.id_publicacion'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
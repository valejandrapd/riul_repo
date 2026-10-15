from app.extensions import db

class UsuarioInsignia(db.Model):
    __tablename__ = 'usuario_insignia'

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), primary_key=True)
    id_insignia = db.Column(db.Integer, db.ForeignKey('insignia.id_insignia'), primary_key=True)
    fecha_obtencion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
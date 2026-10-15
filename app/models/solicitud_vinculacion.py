from app.extensions import db

class SolicitudVinculacion(db.Model):
    __tablename__ = 'solicitud_vinculacion'

    id_solicitud = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_semillero = db.Column(db.Integer, db.ForeignKey('semillero.id_semillero'), nullable=False)
    estado = db.Column(db.Enum('PENDIENTE', 'APROBADA', 'RECHAZADA'), default='PENDIENTE')
    fecha_solicitud = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
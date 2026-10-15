from app.extensions import db

class IntegranteSemillero(db.Model):
    __tablename__ = 'integrante_semillero'

    id_integrante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_semillero = db.Column(db.Integer, db.ForeignKey('semillero.id_semillero'), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    rol_en_semillero = db.Column(db.String(100))
    fecha_ingreso = db.Column(db.Date)
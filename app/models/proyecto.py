from app.extensions import db

class Proyecto(db.Model):
    __tablename__ = 'proyecto'

    id_proyecto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    resumen = db.Column(db.Text)
    estado = db.Column(db.Enum('EN_EJECUCION', 'FINALIZADO', 'SUSPENDIDO'), default='EN_EJECUCION')
    porcentaje_avance = db.Column(db.Numeric(5, 2), default=0.00)
    fecha_inicio = db.Column(db.Date)
    id_semillero = db.Column(db.Integer, db.ForeignKey('semillero.id_semillero'), nullable=False)
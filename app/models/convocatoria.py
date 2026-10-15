from app.extensions import db

class Convocatoria(db.Model):
    __tablename__ = 'convocatoria'

    id_convocatoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text)
    fecha_limite = db.Column(db.Date)
    id_semillero = db.Column(db.Integer, db.ForeignKey('semillero.id_semillero'), nullable=False)
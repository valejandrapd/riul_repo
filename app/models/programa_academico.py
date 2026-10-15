from app.extensions import db

class ProgramaAcademico(db.Model):
    __tablename__ = 'programa_academico'

    id_programa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    id_facultad = db.Column(db.Integer, db.ForeignKey('facultad.id_facultad'), nullable=False)
from app.extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum('ADMIN', 'DOCENTE_LIDER', 'ESTUDIANTE_INVESTIGADOR'), nullable=False)
    id_programa = db.Column(db.Integer, db.ForeignKey('programa_academico.id_programa'), nullable=True)
    puntos_xp = db.Column(db.Integer, default=0)
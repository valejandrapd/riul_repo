from app.extensions import db

class LogroEvidencia(db.Model):
    __tablename__ = 'logro_evidencia'

    id_logro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text)
    archivo_url = db.Column(db.String(255))
    puntos_otorgados = db.Column(db.Integer, default=0)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
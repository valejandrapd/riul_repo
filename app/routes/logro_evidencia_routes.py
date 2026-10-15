from flask import Blueprint, jsonify
from app.models.logro_evidencia import LogroEvidencia

logro_bp = Blueprint('logro_bp', __name__)

@logro_bp.route('/', methods=['GET'])
def listar_logros():
    logros = LogroEvidencia.query.all()
    resultado = [{"id": l.id_logro, "titulo": l.titulo, "puntos": l.puntos_otorgados} for l in logros]
    return jsonify(resultado), 200
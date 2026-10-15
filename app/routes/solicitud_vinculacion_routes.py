from flask import Blueprint, jsonify
from app.models.solicitud_vinculacion import SolicitudVinculacion

solicitud_bp = Blueprint('solicitud_bp', __name__)

@solicitud_bp.route('/', methods=['GET'])
def listar_solicitudes():
    solicitudes = SolicitudVinculacion.query.all()
    resultado = [{"id": s.id_solicitud, "estado": s.estado} for s in solicitudes]
    return jsonify(resultado), 200
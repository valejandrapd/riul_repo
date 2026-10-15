from flask import Blueprint, jsonify
from app.models.convocatoria import Convocatoria

convocatoria_bp = Blueprint('convocatoria_bp', __name__)

@convocatoria_bp.route('/', methods=['GET'])
def listar_convocatorias():
    convocatorias = Convocatoria.query.all()
    resultado = [{
        "id": c.id_convocatoria,
        "titulo": c.titulo,
        "descripcion": c.descripcion,
        "fecha_limite": str(c.fecha_limite)
    } for c in convocatorias]
    return jsonify(resultado), 200
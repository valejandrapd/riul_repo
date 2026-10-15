from flask import Blueprint, jsonify
from app.models.insignia import Insignia

insignia_bp = Blueprint('insignia_bp', __name__)

@insignia_bp.route('/', methods=['GET'])
def listar_insignias():
    insignias = Insignia.query.all()
    resultado = [{
        "id": i.id_insignia,
        "nombre": i.nombre,
        "descripcion": i.descripcion,
        "puntos": i.puntos_requeridos
    } for i in insignias]
    return jsonify(resultado), 200
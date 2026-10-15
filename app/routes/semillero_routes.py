from flask import Blueprint, jsonify
from app.models.semillero import Semillero

semillero_bp = Blueprint('semillero_bp', __name__)

@semillero_bp.route('/', methods=['GET'])
def listar_semilleros():
    semilleros = Semillero.query.all()
    resultado = [{
        "id": s.id_semillero,
        "nombre": s.nombre,
        "sigla": s.sigla,
        "descripcion": s.descripcion,
        "linea_investigacion": s.linea_investigacion,
        "nivel_estrellas": s.nivel_estrellas
    } for s in semilleros]
    return jsonify(resultado), 200
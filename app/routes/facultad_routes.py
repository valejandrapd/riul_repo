from flask import Blueprint, jsonify
from app.models.facultad import Facultad

facultad_bp = Blueprint('facultad_bp', __name__)

@facultad_bp.route('/', methods=['GET'])
def listar_facultades():
    facultades = Facultad.query.all()
    resultado = [{"id": f.id_facultad, "nombre": f.nombre} for f in facultades]
    return jsonify(resultado), 200
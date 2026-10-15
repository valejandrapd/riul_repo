from flask import Blueprint, jsonify
from app.models.proyecto import Proyecto

proyecto_bp = Blueprint('proyecto_bp', __name__)

@proyecto_bp.route('/', methods=['GET'])
def listar_proyectos():
    proyectos = Proyecto.query.all()
    resultado = [{
        "id": p.id_proyecto,
        "titulo": p.titulo,
        "resumen": p.resumen,
        "estado": p.estado,
        "avance": float(p.porcentaje_avance) if p.porcentaje_avance else 0.0
    } for p in proyectos]
    return jsonify(resultado), 200
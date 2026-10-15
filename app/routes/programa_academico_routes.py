from flask import Blueprint, jsonify
from app.models.programa_academico import ProgramaAcademico

programa_bp = Blueprint('programa_academico_bp', __name__)

@programa_bp.route('/', methods=['GET'])
def listar_programas():
    programas = ProgramaAcademico.query.all()
    resultado = [{"id": p.id_programa, "nombre": p.nombre} for p in programas]
    return jsonify(resultado), 200
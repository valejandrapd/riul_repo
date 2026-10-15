from flask import Blueprint, jsonify
from app.models.publicacion import Publicacion

publicacion_bp = Blueprint('publicacion_bp', __name__)

@publicacion_bp.route('/', methods=['GET'])
def listar_publicaciones():
    publicaciones = Publicacion.query.all()
    resultado = [{
        "id": p.id_publicacion,
        "titulo": p.titulo,
        "contenido": p.contenido,
        "fecha": str(p.fecha_creacion)
    } for p in publicaciones]
    return jsonify(resultado), 200
from flask import Blueprint, jsonify
from app.models.usuario import Usuario

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    resultado = [{
        "id": u.id_usuario,
        "nombre": u.nombre,
        "apellido": u.apellido,
        "correo": u.correo,
        "rol": u.rol,
        "puntos_xp": u.puntos_xp
    } for u in usuarios]
    return jsonify(resultado), 200
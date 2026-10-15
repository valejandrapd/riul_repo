from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from app.models.usuario import Usuario

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')

    usuario = Usuario.query.filter_by(correo=correo).first()
    if not usuario or usuario.contrasena_hash != contrasena:
        return jsonify({"msg": "Correo o contraseña incorrectos"}), 401

    access_token = create_access_token(identity={"id_usuario": usuario.id_usuario, "rol": usuario.rol})
    return jsonify({"access_token": access_token, "rol": usuario.rol, "nombre": usuario.nombre}), 200
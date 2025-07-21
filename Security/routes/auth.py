from flask import Blueprint, request, jsonify
from models import db, Usuario, RefreshToken
from utils.token import gerar_tokens, verificar_refresh_token
import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(email=data['email']).first()
    if not usuario or not bcrypt.checkpw(data['senha'].encode(), usuario.senha):
        return jsonify({"erro": "Credenciais inválidas"}), 401
    access, refresh = gerar_tokens(usuario.id, usuario.role)
    db.session.add(RefreshToken(token=refresh, usuario_id=usuario.id))
    db.session.commit()
    return jsonify({"access_token": access, "refresh_token": refresh})

@auth.route('/auth/refresh', methods=['POST'])
def refresh():
    data = request.get_json()
    token = data.get('refresh_token')
    try:
        payload = verificar_refresh_token(token)
        db_token = RefreshToken.query.filter_by(token=token).first()
        if not db_token:
            return jsonify({"erro": "Refresh Token inválido"}), 401
        usuario = Usuario.query.get(payload['sub'])
        access, _ = gerar_tokens(usuario.id, usuario.role)
        return jsonify({"access_token": access})
    except:
        return jsonify({"erro": "Token inválido ou expirado"}), 401

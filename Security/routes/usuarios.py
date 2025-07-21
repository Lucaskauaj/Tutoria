from flask import Blueprint, request, jsonify
from models import Usuario
from middlewares.jwt_required import jwt_required

usuarios = Blueprint('usuarios', __name__)

@usuarios.route('/usuarios/<int:id>', methods=['GET'])
@jwt_required()
def get_usuario(id):
    if request.user['sub'] != id and request.user['role'] != 'ADMIN':
        return jsonify({"erro": "Acesso negado"}), 403
    user = Usuario.query.get(id)
    return jsonify({"id": user.id, "email": user.email, "role": user.role})

@usuarios.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    hashed = bcrypt.hashpw(data['senha'].encode(), bcrypt.gensalt())
    novo = Usuario(email=data['email'], senha=hashed, role="USER")
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": "Usuário criado com sucesso"})

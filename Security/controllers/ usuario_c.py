from models import db, Usuario
import bcrypt

def criar_usuario_controller(email, senha):
    if Usuario.query.filter_by(email=email).first():
        return None, "E-mail já registrado"
    hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    novo_usuario = Usuario(email=email, senha=hashed, role='USER')
    db.session.add(novo_usuario)
    db.session.commit()
    return novo_usuario, None

def get_usuario_controller(user_id):
    usuario = Usuario.query.get(user_id)
    if not usuario:
        return None, "Usuário não encontrado"
    return usuario, None

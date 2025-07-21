from models import db, Usuario, RefreshToken
from utils.token import gerar_tokens, verificar_refresh_token
import bcrypt

def login_controller(email, senha):
    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not bcrypt.checkpw(senha.encode(), usuario.senha):
        return None, None, "Credenciais inválidas"
    access_token, refresh_token = gerar_tokens(usuario.id, usuario.role)
    db.session.add(RefreshToken(token=refresh_token, usuario_id=usuario.id))
    db.session.commit()
    return access_token, refresh_token, None

def refresh_controller(token):
    try:
        payload = verificar_refresh_token(token)
        db_token = RefreshToken.query.filter_by(token=token).first()
        if not db_token:
            return None, "Refresh token não encontrado"
        usuario = Usuario.query.get(payload['sub'])
        new_access, _ = gerar_tokens(usuario.id, usuario.role)
        return new_access, None
    except:
        return None, "Token inválido ou expirado"

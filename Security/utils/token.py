import jwt
from datetime import datetime, timedelta

ACCESS_SECRET = "segredo_curto"
REFRESH_SECRET = "segredo_longo"

def gerar_tokens(user_id, role):
    access_token = jwt.encode({
        "sub": user_id,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }, ACCESS_SECRET, algorithm="HS256")

    refresh_token = jwt.encode({
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(days=7)
    }, REFRESH_SECRET, algorithm="HS256")

    return access_token, refresh_token

def verificar_access_token(token):
    return jwt.decode(token, ACCESS_SECRET, algorithms=["HS256"])

def verificar_refresh_token(token):
    return jwt.decode(token, REFRESH_SECRET, algorithms=["HS256"])

from functools import wraps
from flask import request, jsonify
from utils.token import verificar_access_token

def jwt_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return jsonify({"erro": "Token ausente"}), 401
            try:
                token = auth_header.split(" ")[1]
                data = verificar_access_token(token)
                request.user = data  # Injeta dados no request
                if role and data["role"] != role:
                    return jsonify({"erro": "Acesso negado"}), 403
            except:
                return jsonify({"erro": "Token inválido ou expirado"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

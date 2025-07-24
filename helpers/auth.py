import jwt
import datetime
from flask import request, jsonify
from functools import wraps

SECRET_KEY = "encodeingKey"

def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({'error': 'Authorization token required'}), 401

        token = auth_header.split(" ")[1]
        decoded = decode_token(token)
        if not decoded:
            return jsonify({'error': 'Invalid or expired token'}), 401

        request.user_id = decoded['user_id']
        return f(*args, **kwargs)
    return wrapper

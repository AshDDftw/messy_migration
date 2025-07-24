import json
from flask import jsonify
from werkzeug.security import check_password_hash
from helpers.db import get_db_connection
from helpers.auth import generate_token

def login(request):
    try:
        data = json.loads(request.get_data())
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, password FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[1], password):
            token = generate_token(user[0])
            return jsonify({'status': 'success', 'token': token}), 200
        else:
            return jsonify({'status': 'failed'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

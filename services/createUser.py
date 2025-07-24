import json
from flask import jsonify
from werkzeug.security import generate_password_hash
from helpers.db import get_db_connection

def create_user(request):
    try:
        data = json.loads(request.get_data())
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            return jsonify({'error': 'All fields are required'}), 400

        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check for duplicate email
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            return jsonify({'error': 'Email already exists'}), 409


        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                       (name, email, hashed_password))
        conn.commit()
        return jsonify({'message': 'User created'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

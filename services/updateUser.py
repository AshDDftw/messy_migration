import json
from flask import jsonify
from helpers.db import get_db_connection

def update_user(user_id, request):
    try:
        data = json.loads(request.get_data())
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({'error': 'Name and email are required'}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({'message': 'User updated'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

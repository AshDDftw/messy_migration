from flask import jsonify
from helpers.db import get_db_connection

def get_user(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()

        if user:
            return jsonify({'id': user[0], 'name': user[1], 'email': user[2]}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

from flask import jsonify
from helpers.db import get_db_connection

def delete_user(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({'message': f'User {user_id} deleted'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

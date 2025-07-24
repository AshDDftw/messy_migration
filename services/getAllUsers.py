from flask import jsonify
from helpers.db import get_db_connection

def get_all_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, password FROM users")
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]
        users = [dict(zip(columns, row)) for row in rows]

        return jsonify(users), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

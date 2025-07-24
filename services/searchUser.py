from flask import jsonify
from helpers.db import get_db_connection

def search_users(request):
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Please provide a name to search'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]
        users = [dict(zip(columns, row)) for row in rows]

        return jsonify(users), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

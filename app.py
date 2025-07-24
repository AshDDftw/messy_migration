from flask import Flask, request
from services import getAllUsers, getUser, createUser, updateUser, deleteUser, searchUser, loginUser
from helpers.auth import token_required

app = Flask(__name__)

# conn = sqlite3.connect('users.db', check_same_thread=False)
# cursor = conn.cursor()

@app.route('/')
def home():
    return "User Management System"

@app.route('/users', methods=['GET'])
@token_required
def get_all_users():
    return getAllUsers.get_all_users()
    # cursor.execute("SELECT * FROM users")
    # users = cursor.fetchall()
    # return str(users)

@app.route('/user/<user_id>', methods=['GET'])
@token_required
def get_user(user_id):
    return getUser.get_user(user_id)
    # print(user_id)
    # query = f"SELECT * FROM users WHERE id = '{user_id}'"
    # cursor.execute(query)
    # user = cursor.fetchone()
    
    # if user:
    #     return str(user)
    # else:
    #     return "User not found"

@app.route('/users', methods=['POST'])
def create_user():
    return createUser.create_user(request)
    # data = request.get_data()
    # data = json.loads(data)
    
    # name = data['name']
    # email = data['email']
    # password = data['password']
    
    # cursor.execute(f"INSERT INTO users (name, email, password) VALUES ('{name}', '{email}', '{password}')")
    # conn.commit()
    
    # print("User created successfully!")
    # return "User created"

@app.route('/user/<user_id>', methods=['PUT'])
@token_required
def update_user(user_id):
    return updateUser.update_user(user_id, request)
    # data = request.get_data()
    # data = json.loads(data)
    
    # name = data.get('name')
    # email = data.get('email')
    
    # if name and email:
    #     cursor.execute(f"UPDATE users SET name = '{name}', email = '{email}' WHERE id = '{user_id}'")
    #     conn.commit()
    #     return "User updated"
    # else:
    #     return "Invalid data"

@app.route('/user/<user_id>', methods=['DELETE'])
@token_required
def delete_user(user_id):
    # cursor.execute(f"DELETE FROM users WHERE id = '{user_id}'")
    # conn.commit()
    deleteUser.delete_user(user_id)
    # print(f"User {user_id} deleted")
    return "User deleted"

@app.route('/search', methods=['GET'])
@token_required
def search_users():
    return searchUser.search_users(request)
    # name = request.args.get('name')
    
    # if not name:
    #     return "Please provide a name to search"
    
    # cursor.execute(f"SELECT * FROM users WHERE name LIKE '%{name}%'")
    # users = cursor.fetchall()
    # return str(users)

@app.route('/login', methods=['POST'])
def login():
    return loginUser.login(request)
    # data = json.loads(request.get_data())
    # email = data['email']
    # password = data['password']
    
    # cursor.execute(f"SELECT * FROM users WHERE email = '{email}' AND password = '{password}'")
    # user = cursor.fetchone()
    
    # if user:
    #     return jsonify({"status": "success", "user_id": user[0]})
    # else:
    #     return jsonify({"status": "failed"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
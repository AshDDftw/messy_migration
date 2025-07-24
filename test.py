import requests
import random
import string
import time

BASE_URL = "http://localhost:5009"

def random_string(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_users(n=10):
    print(f"Creating {n} users...")
    for i in range(n):
        data = {
            "name": f"User{i}_{random_string()}",
            "email": f"user{i}_{random_string()}@example.com",
            "password": "password123"
        }
        r = requests.post(f"{BASE_URL}/users", json=data)
        print(f"[{i+1}] {r.status_code}: {r.json() if 'application/json' in r.headers.get('Content-Type', '') else r.text}")
        time.sleep(0.05)  # Small delay to avoid overwhelming the server

def get_all_users():
    print("\nFetching all users...")
    r = requests.get(f"{BASE_URL}/users")
    try:
        users = r.json()
        print(f"Status: {r.status_code}, Users retrieved: {len(users)}")
        return users
    except:
        print(f"Failed to parse users. Response: {r.text}")
        return []

def search_user(query):
    print(f"\nSearching users with name '{query}'...")
    r = requests.get(f"{BASE_URL}/search", params={"name": query})
    try:
        print(f"Status: {r.status_code}, Results: {r.json()}")
    except:
        print(f"Failed to search. Response: {r.text}")

def login_user(email, password):
    print(f"\nLogging in with: {email}")
    r = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})
    try:
        print(f"Status: {r.status_code}, Response: {r.json()}")
        return r.json().get("user_id")
    except:
        print(f"Login failed. Response: {r.text}")
        return None

def get_user(user_id):
    print(f"\nGetting user with ID {user_id}...")
    r = requests.get(f"{BASE_URL}/user/{user_id}")
    try:
        print(f"Status: {r.status_code}, Data: {r.json()}")
    except:
        print(f"Failed to fetch user. Response: {r.text}")

def update_user(user_id):
    print(f"\nUpdating user ID {user_id}...")
    data = {
        "name": "UpdatedName",
        "email": "updated_email@example.com"
    }
    r = requests.put(f"{BASE_URL}/user/{user_id}", json=data)
    try:
        print(f"Status: {r.status_code}, Response: {r.json()}")
    except:
        print(f"Failed to update user. Response: {r.text}")

def delete_user(user_id):
    print(f"\nDeleting user ID {user_id}...")
    r = requests.delete(f"{BASE_URL}/user/{user_id}")
    try:
        print(f"Status: {r.status_code}, Response: {r.json()}")
    except:
        print(f"Failed to delete user. Response: {r.text}")

if __name__ == "__main__":
    # Step 1: Create test users
    create_users(10)

    # Step 2: Fetch all users
    users = get_all_users()

    if users:
        test_user = users[0]
        user_id = test_user['id']
        email = test_user['email']

        # Step 3: Search user
        search_user(test_user["name"][:4])

        # Step 4: Login
        login_user(email, "password123")

        # Step 5: Get user by ID
        get_user(user_id)

        # Step 6: Update user
        update_user(user_id)

        # Step 7: Delete user
        delete_user(user_id)
    else:
        print("No users found. Aborting further tests.")

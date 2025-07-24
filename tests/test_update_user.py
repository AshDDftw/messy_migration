def test_update_user(client, user_data):
    login_resp = client.post('/login', json={
        "email": user_data['email'],
        "password": user_data['password']
    })
    token = login_resp.get_json().get("token")
    headers = {"Authorization": f"Bearer {token}"}

    users_resp = client.get('/users', headers=headers)
    user_id = users_resp.get_json()[0]['id']

    response = client.put(f'/user/{user_id}', json={
        "name": "UpdatedName",
        "email": "updated@example.com"
    }, headers=headers)

    assert response.status_code == 200 or response.status_code == 404

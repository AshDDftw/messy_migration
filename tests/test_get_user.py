def test_get_user(client, user_data):
    login_resp = client.post('/login', json={
        "email": user_data['email'],
        "password": user_data['password']
    })
    token = login_resp.get_json().get("token")
    headers = {"Authorization": f"Bearer {token}"}

    users_resp = client.get('/users', headers=headers)
    user_id = users_resp.get_json()[0]['id']

    response = client.get(f'/user/{user_id}', headers=headers)

    assert response.status_code == 200
    assert isinstance(response.get_json(), dict)

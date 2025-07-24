def test_get_users_protected(client, user_data):
 
    login_resp = client.post('/login', json={
        "email": user_data['email'],
        "password": user_data['password']
    })
    token = login_resp.get_json().get('token')

    headers = {"Authorization": f"Bearer {token}"}
    response = client.get('/users', headers=headers)

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

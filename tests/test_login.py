def test_login_and_get_token(client, user_data):
    response = client.post('/login', json={
        "email": user_data['email'],
        "password": user_data['password']
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'token' in json_data

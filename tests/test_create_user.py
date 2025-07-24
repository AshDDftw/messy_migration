def test_create_user(client, user_data):
    response = client.post('/users', json=user_data)
    assert response.status_code in [201, 409]

def test_search_user(client, user_data):
    login_resp = client.post('/login', json={
        "email": user_data['email'],
        "password": user_data['password']
    })
    token = login_resp.get_json().get("token")
    headers = {"Authorization": f"Bearer {token}"}

    # Search
    name_query = user_data['name'].split()[0][:4]
    response = client.get(f'/search?name={name_query}', headers=headers)

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

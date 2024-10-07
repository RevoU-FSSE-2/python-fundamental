def test_hit(client, appjson):
    response = client.get("/user", headers=appjson)
    assert response.status_code == 200
    assert response.json == [
        {"first_name": "iwant", "id": 1, "last_name": "kece"},
        {"first_name": "admin", "id": 2, "last_name": "administrator"},
        {"first_name": "john", "id": 3, "last_name": "travolta"},
    ]

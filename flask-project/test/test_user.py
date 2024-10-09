from models.user import User


def test_get_user(client, appjson, generate_fake_user):
    response = client.get("/user", headers=appjson)
    assert response.status_code == 200
    assert response.json == [
        {"first_name": "iwant", "id": 1, "last_name": "kece"},
        {"first_name": "admin", "id": 2, "last_name": "administrator"},
        {"first_name": "john", "id": 3, "last_name": "travolta"},
    ]


def test_success_create_user(client, appjson, test_db):
    # presentation layer
    payload = {"first_name": "jane", "last_name": "doe", "password": "password"}
    response = client.post("/user", headers=appjson, json=payload)
    # business layer
    assert response.status_code == 201
    assert "id" in response.json
    user_id = response.json["id"]
    
    # data layer
    user: User = test_db.session.query(User).get(user_id)
    assert user.id == user_id
    assert user.first_name == payload["first_name"]
    assert user.last_name == payload["last_name"]

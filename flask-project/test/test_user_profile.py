def test_get_profile(client, generate_fake_user):
    response = client.get("/profile")
    assert response.status_code == 200
    assert response.json == [
        {"full_name": "iwant kece", "email": "iwant@gmail.com"},
        {"full_name": "admin administrator", "email": "admin@gmail.com"},
        {"full_name": "john travolta", "email": "john@gmail.com"},
    ]
    
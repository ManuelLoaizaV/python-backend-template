from fastapi.testclient import TestClient


def test_users_list_supports_limit_offset_and_name_filter(client: TestClient) -> None:
    created_names = ["Alice", "Bob", "Alicia", "Charlie"]
    for name in created_names:
        create_response = client.post("/users", json={"name": name})
        assert create_response.status_code == 201

    response = client.get("/users", params={"limit": 2, "offset": 1, "name": "ali"})

    assert response.status_code == 200
    assert response.json() == [
        {"id": 3, "name": "Alicia"},
    ]


def test_users_list_uses_default_pagination(client: TestClient) -> None:
    for name in ["One", "Two"]:
        create_response = client.post("/users", json={"name": name})
        assert create_response.status_code == 201

    response = client.get("/users")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "One"},
        {"id": 2, "name": "Two"},
    ]

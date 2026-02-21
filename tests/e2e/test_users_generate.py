from fastapi.testclient import TestClient

from src.api.dependencies.third_party import get_user_name_generator
from src.application.app import app


class FakeUserNameGenerator:
    def generate_name(self, *, purpose: str | None = None) -> str:
        if purpose:
            return f"{purpose.title()} User"
        return "Generated User"


def test_generate_user_creates_user_from_external_service(client: TestClient) -> None:
    app.dependency_overrides[get_user_name_generator] = lambda: FakeUserNameGenerator()

    try:
        response = client.post("/users/generate", json={"purpose": "marketing"})
    finally:
        app.dependency_overrides.pop(get_user_name_generator, None)

    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Marketing User"}


def test_generate_user_returns_503_when_not_configured(
    client: TestClient,
    monkeypatch,
) -> None:
    monkeypatch.setattr("src.infrastructure.config.settings.gemini_api_key", None)

    response = client.post("/users/generate", json={"purpose": "support"})

    assert response.status_code == 503
    assert response.json() == {"detail": "Gemini integration is not configured"}

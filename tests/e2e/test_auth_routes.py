from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from data.factories import user_factory


class TestRegisterUser:
    async def test_register_user_success(self, client: AsyncClient) -> None:
        # GIVEN a valid registration for a non-existing user
        payload = {
            "username": "mloaiza",
            "password": "Password123$",
            "full_name": "Manuel Loaiza",
        }

        # WHEN we send a POST request to the registration endpoint
        response = await client.post(url="api/v1/auth/register", json=payload)

        # THEN the user should be created
        data = response.json()
        assert response.status_code == 201
        assert data["username"] == payload["username"]
        assert data["full_name"] == payload["full_name"]
        assert "id" in data

    async def test_register_user_invalid_password_fails(self, client: AsyncClient) -> None:
        # GIVEN a payload with a password that fails our custom validation.
        payload = {
            "username": "invalid",
            "full_name": "Invalid User",
        }
        bad_passwords = [
            "Short",  # length less than 8
            "NoNumbers!!!",  # missing digit
            "NoSpecialChar123",  # missing special character
        ]

        for bad_password in bad_passwords:
            payload["password"] = bad_password

            # WHEN we send a POST request to the registration endpoint
            response = await client.post(url="api/v1/auth/register", json=payload)

            # THEN validation errors are caught
            assert response.status_code == 422
            data = response.json()
            assert data["detail"][0]["loc"] == ["body", "password"]

    async def test_register_user_conflict_when_username_exists(
        self, client: AsyncClient, db: AsyncSession
    ) -> None:
        # GIVEN an existing user in the database
        existing_username = "mloaiza"
        await user_factory.create_user(db, username=existing_username)

        payload = {
            "username": existing_username,
            "password": "NewPassword123$",
            "full_name": "Manuel Loaiza",
        }

        # WHEN we send a POST request with the duplicate username
        response = await client.post(url="api/v1/auth/register", json=payload)

        # THEN the server should reject the registration with a conflict
        assert response.status_code == 409

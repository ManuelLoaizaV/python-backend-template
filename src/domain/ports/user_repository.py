from typing import Protocol

from domain.entities.user import UserEntity


class UserRepository(Protocol):
    def list_users(
        self,
        *,
        limit: int,
        offset: int,
        name: str | None = None,
    ) -> list[UserEntity]: ...

    def create_user(self, name: str) -> UserEntity: ...

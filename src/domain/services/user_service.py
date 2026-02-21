from src.domain.entities.user import UserEntity
from src.domain.ports.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def list_users(
        self,
        *,
        limit: int,
        offset: int,
        name: str | None = None,
    ) -> list[UserEntity]:
        return self.repository.list_users(limit=limit, offset=offset, name=name)

    def create_user(self, name: str) -> UserEntity:
        return self.repository.create_user(name=name)

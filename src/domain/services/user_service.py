from domain.entities.user import UserEntity
from domain.ports.user_name_generator import UserNameGenerator
from domain.ports.user_repository import UserRepository


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

    def create_generated_user(
        self,
        generator: UserNameGenerator,
        *,
        purpose: str | None = None,
    ) -> UserEntity:
        generated_name = generator.generate_name(purpose=purpose)
        normalized_name = " ".join(generated_name.split())[:100].strip()
        if not normalized_name:
            raise ValueError("Generated user name is empty")

        return self.repository.create_user(name=normalized_name)

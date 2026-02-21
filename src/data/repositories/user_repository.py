from sqlalchemy.orm import Session

from src.data.models.user_model import UserModel
from src.domain.entities.user import UserEntity


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_users(
        self,
        *,
        limit: int,
        offset: int,
        name: str | None = None,
    ) -> list[UserEntity]:
        query = self.db.query(UserModel)

        if name is not None:
            query = query.filter(UserModel.name.ilike(f"%{name}%"))

        rows = query.order_by(UserModel.id).offset(offset).limit(limit).all()
        return [UserEntity(id=row.id, name=row.name) for row in rows]

    def create_user(self, name: str) -> UserEntity:
        row = UserModel(name=name)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return UserEntity(id=row.id, name=row.name)

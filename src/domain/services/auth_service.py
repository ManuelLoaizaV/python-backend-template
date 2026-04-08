from sqlalchemy.orm import Session

from data.repositories import user_repository
from domain.entities.user_entities import User
from domain.exceptions.user_exceptions import UserAlreadyExistsError


def register_user(username: str, password: str, full_name: str, db: Session) -> User:
    existing_user = user_repository.get_by_username(db, username)
    if existing_user is not None:
        raise UserAlreadyExistsError(username)
    hashed_password = password  # TODO: replace this with a hashing util function
    db_user = user_repository.save(db, username, full_name, hashed_password)
    return User.model_validate(db_user)

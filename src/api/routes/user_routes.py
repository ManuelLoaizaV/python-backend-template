from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from api.dependencies.db import get_db
from api.dependencies.third_party import get_user_name_generator
from api.schemas.user_schemas import UserCreate, UserGenerate, UserData
from data.repositories.user_repository import UserRepository
from domain.exceptions.third_party import ThirdPartyIntegrationError
from domain.ports.user_name_generator import UserNameGenerator
from domain.services.user_service import UserService

router = APIRouter()


@router.get("", response_model=list[UserData])
def list_users(
    db: Session = Depends(get_db),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    name: str | None = Query(default=None, min_length=1, max_length=100),
) -> list[UserData]:
    service = UserService(UserRepository(db))
    users = service.list_users(limit=limit, offset=offset, name=name)
    return [UserData(id=user.id, name=user.name) for user in users]


@router.post("", response_model=UserData, status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)) -> UserData:
    service = UserService(UserRepository(db))
    user = service.create_user(name=payload.name)
    return UserData(id=user.id, name=user.name)


@router.post("/generate", response_model=UserData, status_code=201)
def generate_user(
    payload: UserGenerate,
    db: Session = Depends(get_db),
    generator: UserNameGenerator = Depends(get_user_name_generator),
) -> UserData:
    service = UserService(UserRepository(db))
    try:
        user = service.create_generated_user(generator, purpose=payload.purpose)
    except ThirdPartyIntegrationError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to generate user name from third-party service",
        ) from exc
    return UserData(id=user.id, name=user.name)

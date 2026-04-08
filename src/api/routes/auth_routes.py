from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.schemas.auth_schemas import RegisterRequest
from api.schemas.user_schemas import UserResponse
from domain.services import auth_service
from infrastructure.postgres import get_session

auth_router = APIRouter()


@auth_router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    register_request: RegisterRequest,
    db: Annotated[Session, Depends(get_session)],
) -> UserResponse:
    """Register a new user account."""
    registered_user = auth_service.register_user(**register_request.model_dump(), db=db)
    return UserResponse(**registered_user.model_dump())

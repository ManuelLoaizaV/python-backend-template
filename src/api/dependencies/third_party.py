from fastapi import HTTPException, status

from src.domain.ports.user_name_generator import UserNameGenerator
from src.domain.third_party.gemini_user_name_generator import GeminiUserNameGenerator
from src.infrastructure.config import settings


def get_user_name_generator() -> UserNameGenerator:
    if not settings.gemini_api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Gemini integration is not configured",
        )

    return GeminiUserNameGenerator(
        api_key=settings.gemini_api_key,
        model=settings.gemini_model,
    )

from fastapi import APIRouter

from api.routes.auth_routes import auth_router
from api.routes.health_routes import health_router

router = APIRouter()

router.include_router(router=auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(router=health_router, prefix="/healthz", tags=["Health"])

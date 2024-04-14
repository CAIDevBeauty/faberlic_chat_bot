from fastapi import APIRouter

from .api.endpoints import health, intents

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["health"])
router.include_router(intents.router, prefix="/intents", tags=["intents"])

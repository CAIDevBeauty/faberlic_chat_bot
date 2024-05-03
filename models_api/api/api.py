from fastapi import APIRouter

from api.endpoints import health, intents, slots

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["health"])
router.include_router(intents.router, prefix="/intents", tags=["intents"])
router.include_router(slots.router, prefix="/slots", tags=["slots"])

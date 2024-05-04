from fastapi import APIRouter

from api.endpoints import faq, health, intents, rag, slots

router = APIRouter()

router.include_router(rag.router, prefix="/rag", tags=["rag"])
router.include_router(faq.router, prefix="/faq", tags=["faq"])
router.include_router(health.router, prefix="/health", tags=["health"])
router.include_router(intents.router, prefix="/intents", tags=["intents"])
router.include_router(slots.router, prefix="/slots", tags=["slots"])

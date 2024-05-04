from fastapi import APIRouter

from api.endpoints import health, faq

router = APIRouter()

router.include_router(faq.router, prefix="/faq", tags=["faq"])
router.include_router(health.router, prefix="/health", tags=["health"])
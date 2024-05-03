from fastapi import APIRouter

from api.endpoints import health, rag

router = APIRouter()

router.include_router(rag.router, prefix="/rag", tags=["rag"])
router.include_router(health.router, prefix="/health", tags=["health"])
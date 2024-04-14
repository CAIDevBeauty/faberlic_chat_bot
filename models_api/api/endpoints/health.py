from fastapi import APIRouter, status

router = APIRouter()


@router.get("/")
async def health() -> int:
    return status.HTTP_200_OK

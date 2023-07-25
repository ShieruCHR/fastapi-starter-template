from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def api_v1_main_root():
    return "Hello World from API v1!"

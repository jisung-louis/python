from fastapi import APIRouter

router = APIRouter(prefix='/api')

from service import stat_service

# [2] REST API 정의
@router.get("/stats")
async def get_stats():
    return stat_service.get_stats()
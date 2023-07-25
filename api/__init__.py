from glob import glob
from fastapi import APIRouter

from .v1 import router as v1_router

api_router = APIRouter(prefix="/api")

# Register API Routers
api_router.include_router(v1_router)

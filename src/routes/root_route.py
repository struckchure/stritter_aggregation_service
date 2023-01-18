from fastapi import APIRouter

from routes import strit_routes

router = APIRouter(prefix="/api/v1")
router.include_router(strit_routes.router)

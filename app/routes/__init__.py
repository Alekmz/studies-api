from fastapi import APIRouter
from app.routes import study_routes, user_routes

router = APIRouter()

router.include_router(study_routes.router, prefix="/studies", tags=["studies"])
router.include_router(user_routes.router, prefix="/users", tags=["users"])

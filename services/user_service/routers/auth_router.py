from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.user_service.database import get_db
from services.user_service.schemas.auth_schema import (
    LoginRequest,
    LoginResponse
)
from services.user_service.schemas.user_schema import (
    UserCreate,
    UserResponse
)
from services.user_service.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.create_user(db, user)


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    return UserService.login(db, request)
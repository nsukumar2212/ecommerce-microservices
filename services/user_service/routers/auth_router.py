import random
from services.user_service.services.otp_service import OTPService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user_service.services.otp_service import OTPService
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
@router.post("/test-email-otp")
def test_email_otp(email: str):

    otp = OTPService.generate_otp()

    OTPService.send_email_otp(
        email,
        otp
    )

    return {
        "message": "OTP sent successfully"
    }
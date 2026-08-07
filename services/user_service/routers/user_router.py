from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.user_service.database import get_db
from services.user_service.schemas.user_schema import (
    UserResponse,
    UserUpdate
)
from services.user_service.schemas.user_schema import (
    UserResponse,
    UserUpdate,
    ChangePassword
)
from services.user_service.services.user_service import UserService
from shared.auth.auth_dependency import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get(
    "/me",
    response_model=UserResponse
)
def get_profile(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.get_current_user_profile(db, payload)


@router.put(
    "/me",
    response_model=UserResponse
)
def update_profile(
    request: UserUpdate,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.update_profile(
        db,
        payload,
        request
    )
@router.put("/change-password")
def change_password(
    request: ChangePassword,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    UserService.change_password(
        db,
        payload,
        request
    )

    return {
        "message": "Password changed successfully"
    }
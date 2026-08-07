from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.user_service.database import get_db
from services.user_service.schemas.user_schema import UserResponse
from services.user_service.schemas.admin_schema import UpdateRole
from services.user_service.services.user_service import UserService

from shared.auth.role_dependency import admin_required

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users", response_model=list[UserResponse])
def get_all_users(
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.get_all_users(db)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.get_user_by_id(db, user_id)


@router.put("/users/{user_id}/role", response_model=UserResponse)
def update_role(
    user_id: int,
    request: UpdateRole,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.update_role(db, user_id, request)


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.delete_user(db, user_id)
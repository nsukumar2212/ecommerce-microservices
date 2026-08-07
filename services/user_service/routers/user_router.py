from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.auth.role_dependency import admin_required
from services.user_service.schemas.admin_schema import UpdateRole
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
from services.user_service.schemas.address_schema import (
    AddressCreate,
    AddressUpdate,
    AddressResponse
)
from services.user_service.services.user_service import UserService
from shared.auth.auth_dependency import get_current_user
from shared.auth.role_dependency import admin_required
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
@router.post(
    "/address",
    response_model=AddressResponse
)
def add_address(
    request: AddressCreate,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.add_address(db, payload, request)


@router.get(
    "/address",
    response_model=list[AddressResponse]
)
def get_addresses(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.get_addresses(db, payload)


@router.put(
    "/address/{address_id}",
    response_model=AddressResponse
)
def update_address(
    address_id: int,
    request: AddressUpdate,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.update_address(
        db,
        payload,
        address_id,
        request
    )


@router.delete("/address/{address_id}")
def delete_address(
    address_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return UserService.delete_address(
        db,
        payload,
        address_id
    )
@router.get("/admin/users")
def get_all_users(
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.get_all_users(db)


@router.get("/admin/users/{user_id}")
def get_user(
    user_id: int,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.get_user_by_id(
        db,
        user_id
    )


@router.put("/admin/users/{user_id}/role")
def update_role(
    user_id: int,
    request: UpdateRole,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.update_role(
        db,
        user_id,
        request
    )


@router.delete("/admin/users/{user_id}")
def delete_user(
    user_id: int,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return UserService.delete_user(
        db,
        user_id
    )
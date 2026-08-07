from fastapi import HTTPException

from services.user_service.crud.user_crud import UserCRUD
from services.user_service.models.user import User
from services.user_service.schemas.user_schema import (
    UserCreate,
    UserUpdate
)

from shared.security.password import (
    hash_password,
    verify_password
)

from shared.auth.jwt_handler import create_access_token


class UserService:

    @staticmethod
    def create_user(db, user: UserCreate):

        # Check email
        existing_email = UserCRUD.get_user_by_email(db, user.email)

        if existing_email:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        # Check phone
        existing_phone = UserCRUD.get_user_by_phone(db, user.phone)

        if existing_phone:
            raise HTTPException(
                status_code=400,
                detail="Phone number already registered"
            )

        db_user = User(
            full_name=user.full_name,
            email=user.email,
            password=hash_password(user.password),
            phone=user.phone,
            role_id=user.role_id
        )

        return UserCRUD.create_user(db, db_user)

    @staticmethod
    def login(db, request):

        user = UserCRUD.get_user_by_email(db, request.email)

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(request.password, user.password):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            {
                "sub": user.email,
                "role": user.role_id
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    @staticmethod
    def get_current_user_profile(db, payload):

        email = payload.get("sub")

        user = UserCRUD.get_user_by_email(db, email)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    @staticmethod
    def update_profile(db, payload, request: UserUpdate):

        email = payload.get("sub")

        user = UserCRUD.get_user_by_email(db, email)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        existing_phone = UserCRUD.get_user_by_phone(db, request.phone)

        if existing_phone and existing_phone.user_id != user.user_id:
            raise HTTPException(
                status_code=400,
                detail="Phone number already exists"
            )

        user.full_name = request.full_name
        user.phone = request.phone

        return UserCRUD.update_user(db, user)
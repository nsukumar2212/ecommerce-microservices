from fastapi import HTTPException
from services.user_service.crud.user_crud import UserCRUD
from services.user_service.models.user import User
from services.user_service.schemas.user_schema import UserCreate
from shared.security.password import hash_password


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
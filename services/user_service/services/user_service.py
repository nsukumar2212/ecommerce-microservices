from fastapi import HTTPException
from services.user_service.schemas.admin_schema import UpdateRole
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
from services.user_service.crud.address_crud import AddressCRUD
from services.user_service.models.address import Address
from services.user_service.schemas.address_schema import (
    AddressCreate,
    AddressUpdate
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
    @staticmethod
    def change_password(db, payload, request):

        # Get logged-in user's email from JWT
        email = payload.get("sub")

        # Find user
        user = UserCRUD.get_user_by_email(db, email)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Verify current password
        if not verify_password(
            request.current_password,
            user.password
        ):
            raise HTTPException(
                status_code=400,
                detail="Current password is incorrect"
            )

        # Hash new password
        user.password = hash_password(request.new_password)

        # Save changes
        return UserCRUD.update_user(db, user)
    @staticmethod
    def add_address(db, payload, request: AddressCreate):

        email = payload.get("sub")

        user = UserCRUD.get_user_by_email(db, email)

        address = Address(
            user_id=user.user_id,
            address_line=request.address_line,
            city=request.city,
            state=request.state,
            pincode=request.pincode,
            country=request.country
        )

        return AddressCRUD.create_address(db, address)


    @staticmethod
    def get_addresses(db, payload):

        email = payload.get("sub")

        user = UserCRUD.get_user_by_email(db, email)

        return AddressCRUD.get_addresses_by_user(
            db,
            user.user_id
        )


    @staticmethod
    def update_address(db, payload, address_id, request: AddressUpdate):

        email = payload.get("sub")

        user = UserCRUD.get_user_by_email(db, email)

        address = AddressCRUD.get_address_by_id(db, address_id)

        if not address:
            raise HTTPException(
                status_code=404,
                detail="Address not found"
            )

        if address.user_id != user.user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        address.address_line = request.address_line
        address.city = request.city
        address.state = request.state
        address.pincode = request.pincode
        address.country = request.country

        return AddressCRUD.update_address(db, address)


    @staticmethod
    def delete_address(db, payload, address_id):

        email = payload.get("sub")

        user = UserCRUD.get_user_by_email(db, email)

        address = AddressCRUD.get_address_by_id(db, address_id)

        if not address:
            raise HTTPException(
                status_code=404,
                detail="Address not found"
            )

        if address.user_id != user.user_id:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        AddressCRUD.delete_address(db, address)

        return {
            "message": "Address deleted successfully"
        }
    @staticmethod
    def get_all_users(db):

        return UserCRUD.get_all_users(db)

    @staticmethod
    def get_user_by_id(db, user_id):

        user = UserCRUD.get_user_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    @staticmethod
    def delete_user(db, user_id):

        user = UserCRUD.get_user_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        UserCRUD.delete_user(db, user)

        return {
            "message": "User deleted successfully"
        }

    @staticmethod
    def update_role(db, user_id, request: UpdateRole):

        user = UserCRUD.get_user_by_id(db, user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return UserCRUD.update_role(
            db,
            user,
            request.role_id
        )
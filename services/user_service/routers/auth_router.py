from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.user_service.database import get_db
from services.user_service.schemas.user_schema import UserCreate
from services.user_service.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.create_user(db, user)
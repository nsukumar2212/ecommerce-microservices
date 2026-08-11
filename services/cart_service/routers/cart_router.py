from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.cart_service.database import get_db
from services.cart_service.schemas.cart_schema import CartResponse
from services.cart_service.services.cart_service import CartService

from shared.auth.auth_dependency import get_current_user


router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post(
    "",
    response_model=CartResponse
)
def create_or_get_cart(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return CartService.get_or_create_cart(
        db,
        user_id
    )


@router.get(
    "",
    response_model=CartResponse
)
def get_my_cart(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return CartService.get_cart(
        db,
        user_id
    )


@router.delete("")
def clear_my_cart(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return CartService.clear_cart(
        db,
        user_id
    )
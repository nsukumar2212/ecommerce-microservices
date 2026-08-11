from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.cart_service.database import get_db

from services.cart_service.schemas.cart_item_schema import (
    CartItemCreate,
    CartItemUpdate,
    CartItemResponse
)

from services.cart_service.services.cart_item_service import (
    CartItemService
)

from shared.auth.auth_dependency import get_current_user


router = APIRouter(
    prefix="/cart/items",
    tags=["Cart Items"]
)


@router.post(
    "",
    response_model=CartItemResponse
)
def add_item(
    request: CartItemCreate,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return CartItemService.add_item(
        db,
        user_id,
        request
    )


@router.get(
    "",
    response_model=list[CartItemResponse]
)
def get_cart_items(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return CartItemService.get_cart_items(
        db,
        user_id
    )


@router.put(
    "/{cart_item_id}",
    response_model=CartItemResponse
)
def update_item(
    cart_item_id: int,
    request: CartItemUpdate,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return CartItemService.update_item(
        db,
        user_id,
        cart_item_id,
        request
    )


@router.delete("/{cart_item_id}")
def remove_item(
    cart_item_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return CartItemService.remove_item(
        db,
        user_id,
        cart_item_id
    )
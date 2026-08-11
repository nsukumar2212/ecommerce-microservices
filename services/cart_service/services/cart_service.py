from fastapi import HTTPException

from services.cart_service.crud.cart_crud import CartCRUD
from services.cart_service.models.cart import Cart


class CartService:

    @staticmethod
    def get_or_create_cart(db, user_id: int):

        cart = CartCRUD.get_cart_by_user_id(
            db,
            user_id
        )

        if cart:
            return cart

        cart = Cart(
            user_id=user_id
        )

        return CartCRUD.create_cart(
            db,
            cart
        )

    @staticmethod
    def get_cart(db, user_id: int):

        cart = CartCRUD.get_cart_by_user_id(
            db,
            user_id
        )

        if not cart:
            raise HTTPException(
                status_code=404,
                detail="Cart not found"
            )

        return cart

    @staticmethod
    def clear_cart(db, user_id: int):

        cart = CartCRUD.get_cart_by_user_id(
            db,
            user_id
        )

        if not cart:
            raise HTTPException(
                status_code=404,
                detail="Cart not found"
            )

        CartCRUD.delete_cart(
            db,
            cart
        )

        return {
            "message": "Cart cleared successfully"
        }
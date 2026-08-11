import httpx
from fastapi import HTTPException

from services.cart_service.crud.cart_crud import CartCRUD
from services.cart_service.crud.cart_item_crud import CartItemCRUD
from services.cart_service.models.cart_item import CartItem


class CartItemService:

    @staticmethod
    def add_item(
        db,
        user_id: int,
        request
    ):

        # Quantity validation
        if request.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity must be greater than 0"
            )

        # Get user's cart
        cart = CartCRUD.get_cart_by_user_id(
            db,
            user_id
        )

        if not cart:

            from services.cart_service.models.cart import Cart

            cart = Cart(
                user_id=user_id
            )

            cart = CartCRUD.create_cart(
                db,
                cart
            )

        # Check if product already exists
        existing_item = CartItemCRUD.get_item(
            db,
            cart.cart_id,
            request.product_id
        )

        if existing_item:

            existing_item.quantity += request.quantity

            return CartItemCRUD.update_item(
                db,
                existing_item
            )

        # Create new cart item
        cart_item = CartItem(
            cart_id=cart.cart_id,
            product_id=request.product_id,
            quantity=request.quantity
        )

        return CartItemCRUD.create_cart_item(
            db,
            cart_item
        )

    @staticmethod
    def get_cart_items(
        db,
        user_id: int
    ):

        cart = CartCRUD.get_cart_by_user_id(
            db,
            user_id
        )

        if not cart:
            raise HTTPException(
                status_code=404,
                detail="Cart not found"
            )

        return CartItemCRUD.get_items_by_cart(
            db,
            cart.cart_id
        )

    @staticmethod
    def update_item(
        db,
        user_id: int,
        cart_item_id: int,
        request
    ):

        if request.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity must be greater than 0"
            )

        cart_item = CartItemCRUD.get_item_by_id(
            db,
            cart_item_id
        )

        if not cart_item:
            raise HTTPException(
                status_code=404,
                detail="Cart item not found"
            )

        cart = CartCRUD.get_cart_by_user_id(
            db,
            user_id
        )

        if not cart or cart_item.cart_id != cart.cart_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot modify this cart item"
            )

        cart_item.quantity = request.quantity

        return CartItemCRUD.update_item(
            db,
            cart_item
        )

    @staticmethod
    def remove_item(
        db,
        user_id: int,
        cart_item_id: int
    ):

        cart_item = CartItemCRUD.get_item_by_id(
            db,
            cart_item_id
        )

        if not cart_item:
            raise HTTPException(
                status_code=404,
                detail="Cart item not found"
            )

        cart = CartCRUD.get_cart_by_user_id(
            db,
            user_id
        )

        if not cart or cart_item.cart_id != cart.cart_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot remove this cart item"
            )

        CartItemCRUD.delete_item(
            db,
            cart_item
        )

        return {
            "message": "Cart item removed successfully"
        }
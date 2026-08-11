import httpx
from decimal import Decimal
from pathlib import Path
import os

from dotenv import load_dotenv
from fastapi import HTTPException
from sqlalchemy.orm import Session

from services.order_service.crud.order_crud import OrderCRUD
from services.order_service.crud.order_item_crud import OrderItemCRUD

from services.order_service.models.order import Order
from services.order_service.models.order_item import OrderItem


# --------------------------------
# Load Order Service .env
# --------------------------------

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)


# --------------------------------
# Service URLs
# --------------------------------

CART_SERVICE_URL = os.getenv(
    "CART_SERVICE_URL",
    "http://127.0.0.1:8003"
)

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://127.0.0.1:8002"
)


class OrderService:

    # --------------------------------
    # Create Order
    # --------------------------------

    @staticmethod
    def create_order(
        db: Session,
        user_id: int,
        authorization: str
    ):

        # --------------------------------
        # 1. Get user's cart
        # --------------------------------

        try:
            response = httpx.get(
                f"{CART_SERVICE_URL}/api/v1/cart/items",
                headers={
                    "Authorization": authorization
                }
            )

        except httpx.RequestError:
            raise HTTPException(
                status_code=503,
                detail="Cart Service unavailable"
            )

        # --------------------------------
        # Check Cart Service response
        # --------------------------------

        if response.status_code != 200:
            raise HTTPException(
                status_code=503,
                detail="Unable to get cart items"
            )

        cart_items = response.json()

        # --------------------------------
        # 2. Check cart
        # --------------------------------

        if not cart_items:
            raise HTTPException(
                status_code=400,
                detail="Cart is empty"
            )

        # --------------------------------
        # 3. Calculate total
        # --------------------------------

        total_amount = Decimal("0.00")

        product_details = []

        # --------------------------------
        # 4. Get product prices
        # --------------------------------

        for item in cart_items:

            product_id = item["product_id"]
            quantity = item["quantity"]

            try:
                response = httpx.get(
                    f"{PRODUCT_SERVICE_URL}/api/v1/products/{product_id}"
                )

            except httpx.RequestError:
                raise HTTPException(
                    status_code=503,
                    detail="Product Service unavailable"
                )

            # Product not found
            if response.status_code == 404:
                raise HTTPException(
                    status_code=404,
                    detail=f"Product {product_id} not found"
                )

            # Other Product Service errors
            if response.status_code != 200:
                raise HTTPException(
                    status_code=503,
                    detail="Unable to get product details"
                )

            product = response.json()

            # --------------------------------
            # Get product price
            # --------------------------------

            price = Decimal(
                str(product["price"])
            )

            item_total = price * quantity

            total_amount += item_total

            product_details.append({
                "product_id": product_id,
                "quantity": quantity,
                "price": price
            })

        # --------------------------------
        # 5. Create Order
        # --------------------------------

        order = Order(
            user_id=user_id,
            total_amount=total_amount,
            status="pending"
        )

        order = OrderCRUD.create_order(
            db,
            order
        )

        # --------------------------------
        # 6. Create Order Items
        # --------------------------------

        for product in product_details:

            order_item = OrderItem(
                order_id=order.order_id,
                product_id=product["product_id"],
                quantity=product["quantity"],
                price=product["price"]
            )

            OrderItemCRUD.create_order_item(
                db,
                order_item
            )

        # --------------------------------
        # 7. Return created order
        # --------------------------------

        return OrderCRUD.get_order_by_id(
            db,
            order.order_id
        )


    # --------------------------------
    # Get Single Order
    # --------------------------------

    @staticmethod
    def get_order(
        db: Session,
        user_id: int,
        order_id: int
    ):

        order = OrderCRUD.get_order_by_id(
            db,
            order_id
        )

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Order not found"
            )

        # Make sure user owns the order
        if order.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot access this order"
            )

        return order


    # --------------------------------
    # Get Current User's Orders
    # --------------------------------

    @staticmethod
    def get_my_orders(
        db: Session,
        user_id: int
    ):

        return OrderCRUD.get_orders_by_user(
            db,
            user_id
        )
import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from services.payment_service.crud.payment_crud import PaymentCRUD
from services.payment_service.models.payment import Payment


class PaymentService:

    @staticmethod
    def create_payment(
        db: Session,
        user_id: int,
        order_id: int,
        amount,
        payment_method: str
    ):

        # Check whether payment already exists
        existing_payment = PaymentCRUD.get_payment_by_order_id(
            db,
            order_id
        )

        if existing_payment:
            raise HTTPException(
                status_code=400,
                detail="Payment already exists for this order"
            )

        # Validate amount
        if amount <= 0:
            raise HTTPException(
                status_code=400,
                detail="Payment amount must be greater than 0"
            )

        # Validate payment method
        allowed_methods = [
            "card",
            "upi",
            "netbanking",
            "cod"
        ]

        if payment_method.lower() not in allowed_methods:
            raise HTTPException(
                status_code=400,
                detail="Invalid payment method"
            )

        # Generate mock transaction ID
        transaction_id = (
            "TXN-" + uuid.uuid4().hex[:12].upper()
        )

        # Create payment
        payment = Payment(
            order_id=order_id,
            user_id=user_id,
            amount=amount,
            payment_method=payment_method.lower(),
            transaction_id=transaction_id,
            status="success"
        )

        payment = PaymentCRUD.create_payment(
            db,
            payment
        )

        return payment

    @staticmethod
    def get_payment(
        db: Session,
        user_id: int,
        payment_id: int
    ):

        payment = PaymentCRUD.get_payment_by_id(
            db,
            payment_id
        )

        if not payment:
            raise HTTPException(
                status_code=404,
                detail="Payment not found"
            )

        if payment.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot access this payment"
            )

        return payment

    @staticmethod
    def get_payment_by_order(
        db: Session,
        user_id: int,
        order_id: int
    ):

        payment = PaymentCRUD.get_payment_by_order_id(
            db,
            order_id
        )

        if not payment:
            raise HTTPException(
                status_code=404,
                detail="Payment not found for this order"
            )

        if payment.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot access this payment"
            )

        return payment

    @staticmethod
    def get_my_payments(
        db: Session,
        user_id: int
    ):

        return PaymentCRUD.get_payments_by_user(
            db,
            user_id
        )
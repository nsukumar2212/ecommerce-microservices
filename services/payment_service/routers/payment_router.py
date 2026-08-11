from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.payment_service.database import get_db
from services.payment_service.schemas.payment_schema import (
    PaymentCreate,
    PaymentResponse
)
from services.payment_service.services.payment_service import (
    PaymentService
)

from shared.auth.auth_dependency import get_current_user


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post(
    "",
    response_model=PaymentResponse
)
def create_payment(
    request: PaymentCreate,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return PaymentService.create_payment(
        db,
        user_id,
        request.order_id,
        request.amount,
        request.payment_method
    )


@router.get(
    "",
    response_model=list[PaymentResponse]
)
def get_my_payments(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return PaymentService.get_my_payments(
        db,
        user_id
    )


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def get_payment(
    payment_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return PaymentService.get_payment(
        db,
        user_id,
        payment_id
    )


@router.get(
    "/order/{order_id}",
    response_model=PaymentResponse
)
def get_payment_by_order(
    order_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return PaymentService.get_payment_by_order(
        db,
        user_id,
        order_id
    )
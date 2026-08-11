from fastapi import (
    APIRouter,
    Depends
)

from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer
)

from sqlalchemy.orm import Session

from services.order_service.database import get_db

from services.order_service.services.order_service import (
    OrderService
)

from shared.auth.auth_dependency import get_current_user


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


security = HTTPBearer()


@router.post("")
def create_order(
    payload=Depends(get_current_user),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    user_id = payload.get("user_id")

    authorization = f"Bearer {credentials.credentials}"

    return OrderService.create_order(
        db,
        user_id,
        authorization
    )


@router.get("")
def get_my_orders(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_id = payload.get("user_id")

    return OrderService.get_my_orders(
        db,
        user_id
    )


@router.get("/{order_id}")
def get_order(
    order_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user_id = payload.get("user_id")

    return OrderService.get_order(
        db,
        user_id,
        order_id
    )
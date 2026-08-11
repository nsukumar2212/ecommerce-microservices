from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.notification_service.database import get_db

from services.notification_service.schemas.notification_schema import (
    NotificationCreate,
    NotificationResponse
)

from services.notification_service.services.notification_service import (
    NotificationService
)

from shared.auth.auth_dependency import get_current_user


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)


@router.post(
    "",
    response_model=NotificationResponse
)
def create_notification(
    request: NotificationCreate,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return NotificationService.create_notification(
        db,
        user_id,
        request.order_id,
        request.type,
        request.message
    )


@router.get(
    "",
    response_model=list[NotificationResponse]
)
def get_my_notifications(
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return NotificationService.get_my_notifications(
        db,
        user_id
    )


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse
)
def get_notification(
    notification_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return NotificationService.get_notification(
        db,
        user_id,
        notification_id
    )


@router.put(
    "/{notification_id}/read",
    response_model=NotificationResponse
)
def mark_as_read(
    notification_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return NotificationService.mark_as_read(
        db,
        user_id,
        notification_id
    )


@router.delete(
    "/{notification_id}"
)
def delete_notification(
    notification_id: int,
    payload=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user_id = payload.get("user_id")

    return NotificationService.delete_notification(
        db,
        user_id,
        notification_id
    )
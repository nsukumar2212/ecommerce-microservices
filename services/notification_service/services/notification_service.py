from fastapi import HTTPException
from sqlalchemy.orm import Session

from services.notification_service.crud.notification_crud import (
    NotificationCRUD
)

from services.notification_service.models.notification import (
    Notification
)


class NotificationService:

    @staticmethod
    def create_notification(
        db: Session,
        user_id: int,
        order_id: int | None,
        notification_type: str,
        message: str
    ):

        notification = Notification(
            user_id=user_id,
            order_id=order_id,
            type=notification_type,
            message=message,
            status="unread"
        )

        return NotificationCRUD.create_notification(
            db,
            notification
        )


    @staticmethod
    def get_notification(
        db: Session,
        user_id: int,
        notification_id: int
    ):

        notification = NotificationCRUD.get_notification_by_id(
            db,
            notification_id
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found"
            )

        if notification.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot access this notification"
            )

        return notification


    @staticmethod
    def get_my_notifications(
        db: Session,
        user_id: int
    ):

        return NotificationCRUD.get_notifications_by_user(
            db,
            user_id
        )


    @staticmethod
    def mark_as_read(
        db: Session,
        user_id: int,
        notification_id: int
    ):

        notification = NotificationCRUD.get_notification_by_id(
            db,
            notification_id
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found"
            )

        if notification.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot modify this notification"
            )

        notification.status = "read"

        return NotificationCRUD.update_notification(
            db,
            notification
        )


    @staticmethod
    def delete_notification(
        db: Session,
        user_id: int,
        notification_id: int
    ):

        notification = NotificationCRUD.get_notification_by_id(
            db,
            notification_id
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found"
            )

        if notification.user_id != user_id:
            raise HTTPException(
                status_code=403,
                detail="You cannot delete this notification"
            )

        NotificationCRUD.delete_notification(
            db,
            notification
        )

        return {
            "message": "Notification deleted successfully"
        }
from sqlalchemy.orm import Session

from services.notification_service.models.notification import Notification


class NotificationCRUD:

    @staticmethod
    def create_notification(
        db: Session,
        notification: Notification
    ):
        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification

    @staticmethod
    def get_notification_by_id(
        db: Session,
        notification_id: int
    ):
        return db.query(Notification).filter(
            Notification.notification_id == notification_id
        ).first()

    @staticmethod
    def get_notifications_by_user(
        db: Session,
        user_id: int
    ):
        return db.query(Notification).filter(
            Notification.user_id == user_id
        ).order_by(
            Notification.created_at.desc()
        ).all()

    @staticmethod
    def update_notification(
        db: Session,
        notification: Notification
    ):
        db.commit()
        db.refresh(notification)

        return notification

    @staticmethod
    def delete_notification(
        db: Session,
        notification: Notification
    ):
        db.delete(notification)
        db.commit()
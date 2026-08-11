from sqlalchemy.orm import Session

from services.order_service.models.order import Order


class OrderCRUD:

    @staticmethod
    def create_order(
        db: Session,
        order: Order
    ):
        db.add(order)
        db.commit()
        db.refresh(order)

        return order

    @staticmethod
    def get_order_by_id(
        db: Session,
        order_id: int
    ):
        return db.query(Order).filter(
            Order.order_id == order_id
        ).first()

    @staticmethod
    def get_orders_by_user(
        db: Session,
        user_id: int
    ):
        return db.query(Order).filter(
            Order.user_id == user_id
        ).order_by(
            Order.created_at.desc()
        ).all()

    @staticmethod
    def update_order(
        db: Session,
        order: Order
    ):
        db.commit()
        db.refresh(order)

        return order
from sqlalchemy.orm import Session

from services.order_service.models.order_item import OrderItem


class OrderItemCRUD:

    @staticmethod
    def create_order_item(
        db: Session,
        order_item: OrderItem
    ):
        db.add(order_item)
        db.commit()
        db.refresh(order_item)

        return order_item

    @staticmethod
    def get_items_by_order(
        db: Session,
        order_id: int
    ):
        return db.query(OrderItem).filter(
            OrderItem.order_id == order_id
        ).all()
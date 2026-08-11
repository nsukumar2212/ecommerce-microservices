from sqlalchemy.orm import Session

from services.cart_service.models.cart_item import CartItem


class CartItemCRUD:

    @staticmethod
    def create_cart_item(
        db: Session,
        cart_item: CartItem
    ):
        db.add(cart_item)
        db.commit()
        db.refresh(cart_item)
        return cart_item

    @staticmethod
    def get_item_by_id(
        db: Session,
        cart_item_id: int
    ):
        return db.query(CartItem).filter(
            CartItem.cart_item_id == cart_item_id
        ).first()

    @staticmethod
    def get_item(
        db: Session,
        cart_id: int,
        product_id: int
    ):
        return db.query(CartItem).filter(
            CartItem.cart_id == cart_id,
            CartItem.product_id == product_id
        ).first()

    @staticmethod
    def get_items_by_cart(
        db: Session,
        cart_id: int
    ):
        return db.query(CartItem).filter(
            CartItem.cart_id == cart_id
        ).all()

    @staticmethod
    def update_item(
        db: Session,
        cart_item: CartItem
    ):
        db.commit()
        db.refresh(cart_item)
        return cart_item

    @staticmethod
    def delete_item(
        db: Session,
        cart_item: CartItem
    ):
        db.delete(cart_item)
        db.commit()
from sqlalchemy.orm import Session

from services.cart_service.models.cart import Cart


class CartCRUD:

    @staticmethod
    def create_cart(db: Session, cart: Cart):
        db.add(cart)
        db.commit()
        db.refresh(cart)
        return cart

    @staticmethod
    def get_cart_by_user_id(db: Session, user_id: int):
        return db.query(Cart).filter(
            Cart.user_id == user_id
        ).first()

    @staticmethod
    def get_cart_by_id(db: Session, cart_id: int):
        return db.query(Cart).filter(
            Cart.cart_id == cart_id
        ).first()

    @staticmethod
    def delete_cart(db: Session, cart: Cart):
        db.delete(cart)
        db.commit()
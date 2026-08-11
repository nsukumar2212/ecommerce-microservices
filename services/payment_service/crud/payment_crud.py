from sqlalchemy.orm import Session

from services.payment_service.models.payment import Payment


class PaymentCRUD:

    @staticmethod
    def create_payment(
        db: Session,
        payment: Payment
    ):
        db.add(payment)
        db.commit()
        db.refresh(payment)

        return payment

    @staticmethod
    def get_payment_by_id(
        db: Session,
        payment_id: int
    ):
        return db.query(Payment).filter(
            Payment.payment_id == payment_id
        ).first()

    @staticmethod
    def get_payment_by_order_id(
        db: Session,
        order_id: int
    ):
        return db.query(Payment).filter(
            Payment.order_id == order_id
        ).first()

    @staticmethod
    def get_payments_by_user(
        db: Session,
        user_id: int
    ):
        return db.query(Payment).filter(
            Payment.user_id == user_id
        ).order_by(
            Payment.created_at.desc()
        ).all()

    @staticmethod
    def update_payment(
        db: Session,
        payment: Payment
    ):
        db.commit()
        db.refresh(payment)

        return payment
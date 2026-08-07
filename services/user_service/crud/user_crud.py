from sqlalchemy.orm import Session
from services.user_service.models.user import User


class UserCRUD:

    @staticmethod
    def create_user(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_user_by_phone(db: Session, phone: str):
        return db.query(User).filter(User.phone == phone).first()

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def update_user(db: Session, user: User):

        db.commit()
        db.refresh(user)

        return user
    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(
            User.user_id == user_id
        ).first()

    @staticmethod
    def delete_user(db: Session, user: User):
        db.delete(user)
        db.commit()

    @staticmethod
    def update_role(db: Session, user: User, role_id: int):
        user.role_id = role_id
        db.commit()
        db.refresh(user)
        return user
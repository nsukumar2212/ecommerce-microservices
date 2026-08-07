from sqlalchemy.orm import Session

from services.user_service.models.address import Address


class AddressCRUD:

    @staticmethod
    def create_address(db: Session, address: Address):
        db.add(address)
        db.commit()
        db.refresh(address)
        return address

    @staticmethod
    def get_addresses_by_user(db: Session, user_id: int):
        return db.query(Address).filter(
            Address.user_id == user_id
        ).all()

    @staticmethod
    def get_address_by_id(db: Session, address_id: int):
        return db.query(Address).filter(
            Address.address_id == address_id
        ).first()

    @staticmethod
    def update_address(db: Session, address: Address):
        db.commit()
        db.refresh(address)
        return address

    @staticmethod
    def delete_address(db: Session, address: Address):
        db.delete(address)
        db.commit()
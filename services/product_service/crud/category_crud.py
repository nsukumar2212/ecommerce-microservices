from sqlalchemy.orm import Session

from services.product_service.models.category import Category


class CategoryCRUD:

    @staticmethod
    def create_category(db: Session, category: Category):
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def get_all_categories(db: Session):
        return db.query(Category).all()

    @staticmethod
    def get_category_by_id(db: Session, category_id: int):
        return db.query(Category).filter(
            Category.category_id == category_id
        ).first()

    @staticmethod
    def get_category_by_name(db: Session, category_name: str):
        return db.query(Category).filter(
            Category.category_name == category_name
        ).first()

    @staticmethod
    def update_category(db: Session, category: Category):
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def delete_category(db: Session, category: Category):
        db.delete(category)
        db.commit()
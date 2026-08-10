from sqlalchemy.orm import Session

from services.product_service.models.product import Product


class ProductCRUD:

    @staticmethod
    def create_product(db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_all_products(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_product_by_id(db: Session, product_id: int):
        return db.query(Product).filter(
            Product.product_id == product_id
        ).first()

    @staticmethod
    def get_product_by_name(db: Session, product_name: str):
        return db.query(Product).filter(
            Product.product_name == product_name
        ).first()

    @staticmethod
    def get_products_by_category(db: Session, category_id: int):
        return db.query(Product).filter(
            Product.category_id == category_id
        ).all()

    @staticmethod
    def update_product(db: Session, product: Product):
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete_product(db: Session, product: Product):
        db.delete(product)
        db.commit()
from fastapi import HTTPException

from services.product_service.crud.product_crud import ProductCRUD
from services.product_service.crud.category_crud import CategoryCRUD
from services.product_service.models.product import Product


class ProductService:

    @staticmethod
    def create_product(db, request):

        # Check if category exists
        category = CategoryCRUD.get_category_by_id(
            db,
            request.category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        product = Product(
            product_name=request.product_name,
            brand=request.brand,
            price=request.price,
            description=request.description,
            image=request.image,
            stock=request.stock,
            category_id=request.category_id
        )

        return ProductCRUD.create_product(
            db,
            product
        )

    @staticmethod
    def get_all_products(db):

        return ProductCRUD.get_all_products(db)

    @staticmethod
    def get_product_by_id(
        db,
        product_id
    ):

        product = ProductCRUD.get_product_by_id(
            db,
            product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product

    @staticmethod
    def update_product(
        db,
        product_id,
        request
    ):

        product = ProductCRUD.get_product_by_id(
            db,
            product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        category = CategoryCRUD.get_category_by_id(
            db,
            request.category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        product.product_name = request.product_name
        product.brand = request.brand
        product.price = request.price
        product.description = request.description
        product.image = request.image
        product.stock = request.stock
        product.category_id = request.category_id

        return ProductCRUD.update_product(
            db,
            product
        )

    @staticmethod
    def delete_product(
        db,
        product_id
    ):

        product = ProductCRUD.get_product_by_id(
            db,
            product_id
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        ProductCRUD.delete_product(
            db,
            product
        )

        return {
            "message": "Product deleted successfully"
        }
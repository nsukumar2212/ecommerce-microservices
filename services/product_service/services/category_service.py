from fastapi import HTTPException

from services.product_service.crud.category_crud import CategoryCRUD
from services.product_service.models.category import Category
from services.product_service.schemas.category_schema import (
    CategoryCreate,
    CategoryUpdate
)


class CategoryService:

    @staticmethod
    def create_category(db, request: CategoryCreate):

        existing = CategoryCRUD.get_category_by_name(
            db,
            request.category_name
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Category already exists"
            )

        category = Category(
            category_name=request.category_name
        )

        return CategoryCRUD.create_category(
            db,
            category
        )

    @staticmethod
    def get_all_categories(db):
        return CategoryCRUD.get_all_categories(db)

    @staticmethod
    def get_category_by_id(db, category_id):

        category = CategoryCRUD.get_category_by_id(
            db,
            category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        return category

    @staticmethod
    def update_category(
        db,
        category_id,
        request: CategoryUpdate
    ):

        category = CategoryCRUD.get_category_by_id(
            db,
            category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        category.category_name = request.category_name

        return CategoryCRUD.update_category(
            db,
            category
        )

    @staticmethod
    def delete_category(db, category_id):

        category = CategoryCRUD.get_category_by_id(
            db,
            category_id
        )

        if not category:
            raise HTTPException(
                status_code=404,
                detail="Category not found"
            )

        CategoryCRUD.delete_category(
            db,
            category
        )

        return {
            "message": "Category deleted successfully"
        }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.product_service.database import get_db
from services.product_service.schemas.category_schema import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)
from services.product_service.services.category_service import CategoryService

from shared.auth.role_dependency import admin_required

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post(
    "",
    response_model=CategoryResponse
)
def create_category(
    request: CategoryCreate,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return CategoryService.create_category(
        db,
        request
    )


@router.get(
    "",
    response_model=list[CategoryResponse]
)
def get_all_categories(
    db: Session = Depends(get_db)
):
    return CategoryService.get_all_categories(db)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse
)
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    return CategoryService.get_category_by_id(
        db,
        category_id
    )


@router.put(
    "/{category_id}",
    response_model=CategoryResponse
)
def update_category(
    category_id: int,
    request: CategoryUpdate,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return CategoryService.update_category(
        db,
        category_id,
        request
    )


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return CategoryService.delete_category(
        db,
        category_id
    )
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.product_service.database import get_db

from services.product_service.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from services.product_service.services.product_service import ProductService

from shared.auth.role_dependency import admin_required


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "",
    response_model=ProductResponse
)
def create_product(
    request: ProductCreate,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return ProductService.create_product(
        db,
        request
    )


@router.get(
    "",
    response_model=list[ProductResponse]
)
def get_all_products(
    db: Session = Depends(get_db)
):
    return ProductService.get_all_products(db)


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return ProductService.get_product_by_id(
        db,
        product_id
    )


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    request: ProductUpdate,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return ProductService.update_product(
        db,
        product_id,
        request
    )


@router.delete(
    "/{product_id}"
)
def delete_product(
    product_id: int,
    payload=Depends(admin_required),
    db: Session = Depends(get_db)
):
    return ProductService.delete_product(
        db,
        product_id
    )
from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    product_name: str
    brand: str
    price: float
    description: str | None = None
    image: str | None = None
    stock: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    product_id: int

    model_config = ConfigDict(
        from_attributes=True
    )
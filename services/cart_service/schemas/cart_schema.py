from pydantic import BaseModel, ConfigDict


class CartResponse(BaseModel):
    cart_id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )
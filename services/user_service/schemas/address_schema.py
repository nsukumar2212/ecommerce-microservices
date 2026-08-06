from pydantic import BaseModel, ConfigDict


class AddressBase(BaseModel):
    address_line: str
    city: str
    state: str
    pincode: str
    country: str


class AddressCreate(AddressBase):
    pass


class AddressResponse(AddressBase):
    address_id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
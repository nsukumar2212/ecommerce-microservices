from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str


class UserCreate(UserBase):
    password: str
    role_id: int


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    user_id: int
    role_id: int

    model_config = ConfigDict(from_attributes=True)
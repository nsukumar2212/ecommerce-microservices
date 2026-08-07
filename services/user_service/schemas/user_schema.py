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


class UserUpdate(BaseModel):
    full_name: str
    phone: str


class UserResponse(UserBase):
    user_id: int
    role_id: int

    model_config = ConfigDict(from_attributes=True)
class ChangePassword(BaseModel):
    current_password: str
    new_password: str

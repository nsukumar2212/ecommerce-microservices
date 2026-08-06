from pydantic import BaseModel, ConfigDict


class RoleBase(BaseModel):
    role_name: str


class RoleResponse(RoleBase):
    role_id: int

    model_config = ConfigDict(from_attributes=True)
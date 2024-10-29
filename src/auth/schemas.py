from fastapi_users import schemas
from datetime import date


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    firstname: str
    lastname: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    id: int
    email: str
    password: str
    firstname: str
    lastname: str
    date_birth: date
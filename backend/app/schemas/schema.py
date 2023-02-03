from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: bool = False


class DisplayUser(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False

class UpdatePassword(BaseModel):
    current_password: str
    new_password: str


class UpdateEmail(BaseModel):
    email: str

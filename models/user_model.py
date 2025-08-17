from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    confirm_password:Optional[str] = None

class UserLogin(UserBase):
    password: str

class UserInDB(UserBase):
    id: int




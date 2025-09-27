from enum import Enum
from pydantic import BaseModel
from typing import Optional

class UserRole(str, Enum):
    STUDENT = "student"
    FACULTY = "faculty"

class User(BaseModel):
    email: str
    hashed_password: str
    role: UserRole
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None
    role: UserRole | None = None
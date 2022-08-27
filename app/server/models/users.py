from typing import Optional
from datetime import datetime
from uuid import uuid4, UUID
from pydantic import Field, EmailStr, BaseModel


class User(BaseModel):
    id: UUID = Field(..., alias="_id", default=uuid4)
    username: str = Field(..., description="Username", unique_items=True)
    email: EmailStr = Field(..., description="Email", unique_items=True)
    hashed_password: str

    def __repr__(self):
        return f"<User {self.username}>"

    def __str__(self) -> str:
        return self.email

    def __hash__(self) -> int:
        return hash(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    class Collection:
        name = "users"


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=50, description="user username")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None




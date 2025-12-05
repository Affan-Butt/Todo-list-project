from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    email: str
    password: str  # Plain password (will be hashed in service layer)


class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True  # For SQLAlchemy compatibility

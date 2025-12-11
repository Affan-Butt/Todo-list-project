from pydantic import BaseModel
from typing import Optional


# ==============================
# Create Todo (Request Body)
# ==============================
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None


# ==============================
# Update Todo (Request Body)
# ==============================
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# ==============================
# Response Schema
# ==============================
class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    owner_id: int

    class Config:
        from_attributes = True  # Works with SQLAlchemy ORM

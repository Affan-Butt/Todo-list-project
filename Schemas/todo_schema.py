from pydantic import BaseModel
from typing import Optional


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    owner_id: int  # Keep as ID for API consistency

    class Config:
        from_attributes = True  # For SQLAlchemy compatibility

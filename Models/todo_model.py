from sqlalchemy import Column, Integer, String, ForeignKey
from Database.db import Base
from pydantic import BaseModel, ConfigDict
from typing import Optional

# SQLAlchemy Database Model


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500))
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

# Pydantic Models


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

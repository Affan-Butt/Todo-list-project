from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from Database.db import Base
from sqlalchemy import create_engine  # Add this import if missing
from sqlalchemy.orm import sessionmaker, declarative_base  # Add if missing


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

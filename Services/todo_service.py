from sqlalchemy.orm import Session
from Repository.todo_repository import create_todo, list_todos_by_owner


def add_todo_for_user(db: Session, title: str, description: str | None, owner_id: int):
    return create_todo(db, title, description, owner_id)


def get_todos_for_user(db: Session, owner_id: int):
    return list_todos_by_owner(db, owner_id)

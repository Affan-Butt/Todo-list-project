from sqlalchemy.orm import Session
from Models.todo_model import Todo


def create_todo(db: Session, title: str, description: str | None, owner_id: int):
    todo = Todo(title=title, description=description, owner_id=owner_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def list_todos_by_owner(db: Session, owner_id: int):
    return db.query(Todo).filter(Todo.owner_id == owner_id).all()

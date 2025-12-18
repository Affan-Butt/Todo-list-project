from typing import List, Optional
from sqlalchemy.orm import Session
from Models.todo_model import Todo
from sqlalchemy import or_


def create_todo(db: Session, title: str, description: str | None, owner_id: int) -> Todo:
    todo = Todo(
        title=title,
        description=description,
        completed=False,
        owner_id=owner_id
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


async def list_todos_by_owner(db: Session, owner_id: int, search: str | None = None) -> List[Todo]:
    query = db.query(Todo).filter(Todo.owner_id == owner_id)

    if search:  # Agar search term hai
        query = query.filter(
            or_(
                # title mein search (case-insensitive)
                Todo.title.ilike(f"%{search}%"),
            )
        )

    return query.all()


def get_todo_by_id_and_owner(db: Session, todo_id: int, owner_id: int) -> Optional[Todo]:
    return (
        db.query(Todo)
        .filter(Todo.id == todo_id, Todo.owner_id == owner_id)
        .first()
    )


def update_todo_entity(
    db: Session,
    todo: Todo,
    title: str | None,
    description: str | None,
    completed: bool | None,
) -> Todo:
    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if completed is not None:
        todo.completed = completed

    db.commit()
    db.refresh(todo)
    return todo


def delete_todo_entity(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()

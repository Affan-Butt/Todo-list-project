from sqlalchemy.orm import Session

from Schemas.todo_schema import TodoCreate, TodoUpdate        # << recommended import
from Models.todo_model import Todo
from Repository.todo_repository import (
    create_todo,
    list_todos_by_owner,
    get_todo_by_id_and_owner,
    update_todo_entity,
    delete_todo_entity,
)


def create_todo_service(db: Session, todo_in: TodoCreate, user_id: int) -> Todo:
    return create_todo(
        db,
        title=todo_in.title,
        description=todo_in.description,
        owner_id=user_id,
    )


async def get_todos_service(db: Session, user_id: int, search: str | None = None) -> List[TodoResponse]:
    # search pass
    return await list_todos_by_owner(db, owner_id=user_id, search=search)


def get_todo_service(db: Session, todo_id: int, user_id: int):
    return get_todo_by_id_and_owner(db, todo_id=todo_id, owner_id=user_id)


def update_todo_service(db: Session, todo: Todo, todo_in: TodoUpdate):
    return update_todo_entity(
        db,
        todo,
        title=todo_in.title,
        description=todo_in.description,
        completed=todo_in.completed,
    )


def delete_todo_service(db: Session, todo: Todo):
    delete_todo_entity(db, todo)

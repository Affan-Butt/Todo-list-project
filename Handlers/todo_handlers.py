from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from Models.user_model import User
from Schemas.todo_schema import TodoCreate, TodoUpdate, TodoResponse
from Services.todo_service import (
    create_todo_service,
    get_todos_service,
    get_todo_service,
    update_todo_service,
    delete_todo_service,
)


async def create_todo_handler(todo_data: TodoCreate, current_user: User, db: Session) -> TodoResponse:
    return create_todo_service(db, todo_data, current_user.id)


async def get_todos_handler(current_user: User, db: Session) -> List[TodoResponse]:
    return get_todos_service(db, current_user.id)


async def get_todo_handler(todo_id: int, current_user: User, db: Session) -> TodoResponse:
    todo = get_todo_service(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


async def update_todo_handler(todo_id: int, todo_data: TodoUpdate, current_user: User, db: Session):
    todo = get_todo_service(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return update_todo_service(db, todo, todo_data)


async def delete_todo_handler(todo_id: int, current_user: User, db: Session):
    todo = get_todo_service(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    delete_todo_service(db, todo)
    return {"message": "Todo deleted successfully"}

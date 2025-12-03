from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from Database.db import get_db
from Models.user_model import User
from Models.todo_model import Todo
from Auth.auth_models import TodoCreate, TodoUpdate, TodoResponse
from Services.auth_service import get_current_user
from Services.todo_service import (
    create_todo_service,
    get_todos_service,
    get_todo_service,
    update_todo_service,
    delete_todo_service,
)


async def create_todo_handler(
    todo_data: TodoCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> TodoResponse:
    todo = create_todo_service(db, todo_data, current_user.id)
    return todo


async def get_todos_handler(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> List[TodoResponse]:
    return get_todos_service(db, current_user.id)


async def get_todo_handler(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> TodoResponse:
    todo = get_todo_service(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


async def update_todo_handler(
    todo_id: int,
    todo_data: TodoUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> TodoResponse:
    todo = get_todo_service(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated = update_todo_service(db, todo, todo_data)
    return updated


async def delete_todo_handler(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    todo = get_todo_service(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    delete_todo_service(db, todo)
    return {"message": "Todo deleted successfully"}

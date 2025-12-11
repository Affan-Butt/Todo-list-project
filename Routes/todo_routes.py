from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Database.db import get_db
from Models.user_model import User
from Services.auth_service import get_current_user
from Schemas.todo_schema import TodoCreate, TodoUpdate, TodoResponse
from Handlers.todo_handlers import (
    create_todo_handler,
    get_todos_handler,
    get_todo_handler,
    update_todo_handler,
    delete_todo_handler,
)

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoResponse, status_code=201)
async def create_todo(
    todo_data: TodoCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await create_todo_handler(todo_data, current_user, db)


@router.get("/", response_model=List[TodoResponse])
async def get_todos(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await get_todos_handler(current_user, db)


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await get_todo_handler(todo_id, current_user, db)


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    todo_data: TodoUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await update_todo_handler(todo_id, todo_data, current_user, db)


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return await delete_todo_handler(todo_id, current_user, db)

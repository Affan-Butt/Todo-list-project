from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Auth.auth_routes import get_current_user
from Database.db import get_db
from Models.todo_model import TodoCreate, TodoOut  # Fixed import
from Services.todo_service import add_todo_for_user, get_todos_for_user
from Models.user_model import User as UserModel

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.post("/", response_model=TodoOut)
async def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    created = add_todo_for_user(
        db, todo.title, todo.description, current_user.id)
    return created


@router.get("/", response_model=list[TodoOut])
async def list_my_todos(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    todos = get_todos_for_user(db, current_user.id)
    return todos

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.db import get_db
from Auth.auth_models import UserLogin, UserCreate
from Services.auth_service import (
    verify_password,
    create_access_token,
    create_user_service,
)
from Repository.user_repository import get_user_by_email


async def login_handler(
    login_data: UserLogin,
    db: Session = Depends(get_db),
):
    user = get_user_by_email(db, email=login_data.email)
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


async def register_handler(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    existing = get_user_by_email(db, email=user_data.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    new_user = create_user_service(db, user_data)
    return {"message": "User created successfully", "user_id": new_user.id}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Auth.auth_models import UserLogin, UserCreate
from Database.db import get_db
from Services.auth_service import create_user_service
from Repository.user_repository import get_user_by_email
from Services.auth_service import verify_password, create_access_token

router = APIRouter()

@router.post("/register")
async def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    # Check if user already exists
    existing = get_user_by_email(db, email=user_data.email)
    if existing:
        from fastapi import HTTPException
        from fastapi import status

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # Create user
    new_user = create_user_service(db, user_data)
    return {"message": "User created successfully", "user_id": new_user.id}


@router.post("/login")
async def login(
    login_data: UserLogin,
    db: Session = Depends(get_db),
):
    # Get user and verify password
    user = get_user_by_email(db, email=login_data.email)
    if not user or not verify_password(login_data.password, user.hashed_password):
        from fastapi import HTTPException
        from fastapi import status

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create JWT token
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

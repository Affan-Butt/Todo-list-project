from fastapi import FastAPI
from Auth.auth_routes import router as auth_router
from Routes.todo_routes import router as todo_router
from Database.db import Base, engine
from Middlewares import logging_middleware, jwt_logging_middleware

from Models.user_model import User
from Models.todo_model import Todo

app = FastAPI(title="Todo JWT API with Postgres", version="1.0.0")

app.middleware("http")(jwt_logging_middleware)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(todo_router, tags=["Todos"])


@app.get("/")
async def root():
    return {"message": "Todo API working! /docs 👉"}


@app.on_event("startup")
async def startup_event():
    # Base.metadata.create_all(bind=engine)  # <-- is line ko abhi comment rehne do
    print("✅ Startup: DB ready")


# main.py, Routes, Handlers, Services, Repository, Schemas,
# Models, Database

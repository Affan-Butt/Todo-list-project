from fastapi import FastAPI

from Auth.auth_routes import router as auth_router
from Routes.todo_routes import router as todo_router
from Database.db import Base, engine
from Models.user_model import User
from Models.todo_model import Todo

app = FastAPI(
    title="Todo JWT API with Postgres",
    description="Secure Todo API with JWT Authentication",
    version="1.0.0",
    debug=True,
)


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created: users, todos")
    print("🚀 API ready at http://127.0.0.1:8000/docs")


app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(todo_router, prefix="/todos", tags=["Todos"])


@app.get("/")
async def root():
    return {"message": "Todo API working! Go to /docs 👉"}


# main.py, Routes, Handlers, Services, Models, Database, Repository, Schemas,

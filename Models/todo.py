from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str | None = None


class TodoOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    owner: str

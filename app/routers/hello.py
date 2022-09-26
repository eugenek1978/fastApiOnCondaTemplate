from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/greets",
    tags=["greets"],
    responses={404: {"description": "Not found"}},
)


class Person(BaseModel):
    name: str
    id: int


@router.get("/")
def greet_default():
    return {"name": "John"}


@router.get("/{name}")
def greet_by_name(name: str):
    return {"name": name}

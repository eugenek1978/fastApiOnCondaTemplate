from fastapi import FastAPI
from .routers import hello

app = FastAPI()

app.include_router(hello.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

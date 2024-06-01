from typing import Union

from fastapi import FastAPI

app = FastAPI(
    title="Customer Request Notification System",
    description="API for handling customer requests and sending notifications to varios channels.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"Hello": "World 2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q, "message": "Hello World Updated"}
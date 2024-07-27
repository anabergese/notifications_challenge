import json

import uvicorn
from domain.models import Message
from fastapi import BackgroundTasks, Depends, FastAPI

from .models import ResponseModel, TopicValidator
from .redis_config import (
    create_redis_connection,
    get_add_message_to_redis_queue,
    publish_message,
)

app = FastAPI(
    title="Application Service",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
    responses={
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    },
)


async def publish_to_r(data: dict):
    publish_message("task_queue", json.dumps(data))


@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Application Service is up and running."}


# @app.post("/message", response_model=ResponseModel)
# async def add_message_to_queue(
#     request: TopicValidator,
#     redis_conn=Depends(create_redis_connection),
#     add_message_to_redis_queue=Depends(get_add_message_to_redis_queue),
# ):
#     message = Message.create(topic=request.topic, description=request.description)
#     add_message_to_redis_queue(message, redis_conn)
#     return ResponseModel(status=200, message="Your message was received. Thanks")


@app.post("/notification", response_model=ResponseModel)
async def notification_message(message: Message, background_tasks: BackgroundTasks):
    data = {"topic": message.topic, "description": message.description}
    background_tasks.add_task(publish_to_r, data)
    return ResponseModel(status=200, message="Your message was received. Thanks")


@app.post("/message", response_model=ResponseModel)
async def add_message_to_queue(
    request: TopicValidator,
    background_tasks: BackgroundTasks,
    redis_conn=Depends(create_redis_connection),
    add_message_to_redis_queue=Depends(get_add_message_to_redis_queue),
):
    message = Message(topic=request.topic, description=request.description)
    background_tasks.add_task(add_message_to_redis_queue, message, redis_conn)
    return ResponseModel(status=200, message="Your message was received. Thanks")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

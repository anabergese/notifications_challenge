import json

import uvicorn
from domain.models import Message
from fastapi import BackgroundTasks, Depends, FastAPI

from .dependencies import get_publish_to_channel, get_redis_connection
from .models import ResponseModel, TopicValidator

app = FastAPI(
    title="Application Service",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
    responses={
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    },
)


@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Application Service is up and running."}


@app.post("/notification", response_model=ResponseModel)
async def add_message_to_queue(
    request: TopicValidator,
    background_tasks: BackgroundTasks,
    redis_conn=Depends(get_redis_connection),
    publish_to_channel=Depends(get_publish_to_channel),
):
    message = Message(topic=request.topic, description=request.description)
    background_tasks.add_task(publish_to_channel, message, redis_conn)
    return ResponseModel(status=200, message="Your message was received. Thanks")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

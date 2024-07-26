from fastapi import FastAPI, Depends
import uvicorn
from entrypoints.models import TopicValidator, ResponseModel
from domain.models import Message
from entrypoints.dependencies import get_redis_connection, get_add_message_to_redis_queue

app = FastAPI(
    title="Application Service",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
    responses={
        404: {"description": "Not Found"},
        500: {"description": "Internal Server Error"},
    }
)

# redis_conn = get_redis_connection()

@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Application Service is up and running."}

@app.post("/message", response_model=ResponseModel)
async def add_message_to_queue(
    request: TopicValidator,
    redis_conn = Depends(get_redis_connection),
    add_message_to_redis_queue = Depends(get_add_message_to_redis_queue)
    ):
    message = Message.create(topic=request.topic, description=request.description)
    add_message_to_redis_queue(message, redis_conn)
    return ResponseModel(status=200, message="Your message was received. Thanks")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
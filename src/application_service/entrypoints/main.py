from fastapi import FastAPI, Depends
import uvicorn
import logging
from entrypoints.models import TopicValidator, ResponseModel
from domain.models import Message
from entrypoints.config import get_redis_connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    redis_conn = Depends(get_redis_connection)
    ):
    # message = {
    #     "id": str(uuid4()),
    #     "topic": request.topic,
    #     "description": request.description
    # }
    message = Message.create(topic=request.topic, description=request.description)
    message_json = message.model_dump_json()
    redis_conn.lpush('task_queue', message_json)
    logger.info("Message added to queue: %s", message_json)
    return ResponseModel(status=200, message="Your message was received. Thanks")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
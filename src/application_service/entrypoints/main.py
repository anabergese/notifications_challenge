from uuid import uuid4
import json
from fastapi import FastAPI, HTTPException
import uvicorn
import logging
from entrypoints.models import RequestModel, ResponseModel, Error
from entrypoints.config import get_redis_connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Application Service",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
    responses={
        404: {"description": "Not Found", "model": Error},
        500: {"description": "Internal Server Error", "model": Error},
    }
)

redis_conn = get_redis_connection()

@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Application Service is up and running."}

@app.post("/add-task", response_model=ResponseModel)
async def add_task_to_queue(request: RequestModel):
    if not request.topic or not request.description:
        raise HTTPException(status_code=400, detail="Invalid request")
    
    message = {
        "id": str(uuid4()),
        "topic": request.topic,
        "description": request.description
    }

    task_json = json.dumps(message)
    redis_conn.lpush('task_queue', task_json)
    logger.info("Task added to queue: %s", task_json)
    return ResponseModel(status=200, message="Job added to queue")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
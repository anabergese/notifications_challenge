from uuid import uuid4
import json
from fastapi import FastAPI, HTTPException
import uvicorn
import redis
from entrypoints.models import RequestModel, ResponseModel

app = FastAPI(
    title="Application Service",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
)

redis_conn = redis.Redis(host='redis', port=6379, db=0)

@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Application Service"}

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
    print(f"Task added to queue: {task_json}")

    return ResponseModel(status=200, message="Job added to queue")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
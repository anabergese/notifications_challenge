from uuid import uuid4
from json import dumps
from fastapi import FastAPI, HTTPException, Depends
import uvicorn
import redis
from redis import Redis
# from rq import Queue
from src.application_service.entrypoints.routes import application_service_routes
from src.application_service.entrypoints.models import RequestModel, ResponseModel
# from src.notification_services.worker import process_message

app = FastAPI(
    title="Application Service",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
)
app.include_router(application_service_routes.router, prefix="/application-service")

# redis_conn = Redis(host="redis", port=6379)
# task_queue = Queue("task_queue", connection=redis_conn)
def redis_db():
    db = redis.Redis(
        host="redis",
        port=6379,
        db=0,
        decode_responses=True,
    )

    # make sure redis is up and running
    db.ping()

    return db

@app.get("/")
def read_root():
    """Server is up and running."""
    return {"message": "Application Service"}

@app.post("/add-job", response_model=ResponseModel)
async def add_job_to_queue(request: RequestModel, db: Redis = Depends(redis_db)):
    if not request.topic or not request.description:
        raise HTTPException(status_code=400, detail="Invalid request")
    
    message = {
        "id": str(uuid4()),
        "topic": request.topic,
        "description": request.description
    }

    message_json = dumps(message)
    print(f"Adding message to queue: {message_json}")  # Mensaje de depuración antes de agregar a la cola
    # task_queue.enqueue(process_message, message_json)
    db.lpush("task_queue", message_json)
    print("Message successfully added to queue")  # Mensaje de confirmación después de agregar a la cola

    return ResponseModel(status=200, message="Job added to queue")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
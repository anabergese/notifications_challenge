import os
from redis import Redis
from uuid import uuid4
from json import dumps
from fastapi import APIRouter, HTTPException, Depends
from src.application_service.entrypoints.models import RequestModel, ResponseModel
from src.application_service.domain.events import EventProvider, BotEventProvider
from src.application_service.domain.event_handlers import EventLogger, EventForwarder

router = APIRouter()
logger = EventLogger()
forwarder = EventForwarder()

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_conn = Redis(host=redis_host, port=redis_port)
queue_name = "notification_queue"

def redis_db():
    db = Redis(
        host=redis_host,
        port=redis_port,
        db=0,
        decode_responses=True,
    )
    db.ping()
    return db

def redis_queue_push(db, message):
    db.lpush(queue_name, message)

@router.post("/notify", response_model=ResponseModel)
async def receive_request(request: RequestModel, event_provider: EventProvider = Depends(BotEventProvider)):
    # 1. Validar la solicitud
    if not request.topic or not request.description:
        raise HTTPException(status_code=400, detail="Invalid request")

    # 2. Crear un evento
    event = event_provider.create_event(request)
    
    # 3. Registrar el evento
    logger.log_event(event)

    # 4. Reenviar el evento
    forwarder.forward_event(event)

    return ResponseModel(status=200, message="Event received, logged, and forwarded")

@router.post("/add-job", response_model=ResponseModel)
async def add_job_to_queue(request: RequestModel):
    if not request.topic or not request.description:
        raise HTTPException(status_code=400, detail="Invalid request")
    
    message = {
        "id": str(uuid4()),
        "topic": request.topic,
        "description": request.description
    }

    message_json = dumps(message)
    redis_queue_push(redis_conn, message_json)

    return ResponseModel(status=200, message="Job added to queue")
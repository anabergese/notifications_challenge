from fastapi import APIRouter, HTTPException, Depends
from entrypoints.models import RequestModel, ResponseModel
from domain.events import EventProvider, BotEventProvider
from domain.event_handlers import EventLogger, EventForwarder

router = APIRouter()
logger = EventLogger()
forwarder = EventForwarder()

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
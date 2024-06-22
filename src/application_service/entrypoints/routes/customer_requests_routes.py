from fastapi import APIRouter, HTTPException
from src.application_service.entrypoints.request_response_schema import Request, Response
from src.application_service.domain.models import CreateRequestEvent
from src.application_service.domain.event_handlers import EventLogger, EventForwarder

router = APIRouter()
logger = EventLogger()
forwarder = EventForwarder()

@router.post("/notify", response_model=Response)
async def receive_request(request: Request):
    # Validar la solicitud
    if not request.topic or not request.description:
        raise HTTPException(status_code=400, detail="Invalid request")

    # Crear un evento
    event = CreateRequestEvent(topic=request.topic, description=request.description, source="CustomerBot", status="Received", id=1)

    # Registrar el evento
    logger.log_event(event)

    # Reenviar el evento
    forwarder.forward_event(event)

    return Response(status=200, message="Event received, logged, and forwarded")

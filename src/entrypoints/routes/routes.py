import logging

from fastapi import APIRouter, Depends, HTTPException, Response

from domain.events import NotificationCreated
from entrypoints.dependencies import get_message_bus
from service_layer.messagebus import MessageBus

from .models import NotificationRequest

router = APIRouter()


@router.get("/")
def read_root() -> Response:
    return Response(
        content='{"message": "Notification System is up and running."}',
        media_type="application/json",
    )


@router.post("/notify")
async def create_notification(
    notification: NotificationRequest,
    message_bus: MessageBus = Depends(get_message_bus),
) -> Response:
    try:
        await message_bus.handle(notification.map_to())
        return Response(
            content=f'{{"message": "Notification created for topic: {notification.topic}"}}',
            media_type="application/json",
        )
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error") from e

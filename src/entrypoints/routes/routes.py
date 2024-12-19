import logging

from fastapi import APIRouter, HTTPException, Response

from domain.events import NotificationCreated
from service_layer import messagebus

from .models import NotificationRequest

router = APIRouter()


@router.get("/")
def read_root() -> Response:
    return Response(
        content='{"message": "Notification System is up and running."}',
        media_type="application/json",
    )


@router.post("/notify")
async def create_notification(notification: NotificationRequest) -> Response:
    try:
        event = NotificationCreated(
            topic=notification.topic, description=notification.description
        )
        logging.info("Event received: %s", event)
        await messagebus.handle(event)
        return Response(
            content=f'{{"message": "Notification created for topic: {event.topic.value}"}}',
            media_type="application/json",
        )
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error") from e

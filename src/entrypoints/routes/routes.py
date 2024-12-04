import logging

from fastapi import APIRouter, HTTPException

from service_layer.service import NotificationService

from .models import NotificationRequest

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Notification System is up and running."}


@router.post("/notify")
async def create_notification(notification: NotificationRequest):
    try:
        # Delegar la lógica de negocio al servicio
        event = await NotificationService.create_notification(
            topic=notification.topic, description=notification.description
        )
        logging.info("Event received: %s", event)
        return {"message": f"Notification created for topic: {event.topic.value}"}
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error") from e

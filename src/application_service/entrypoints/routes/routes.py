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
        print(f"DEBUG: Received event in endpoint: {event}")
        return {"message": f"Notification created for topic: {event.topic}"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve)) from ve

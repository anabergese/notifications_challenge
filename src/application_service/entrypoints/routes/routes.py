import logging

from fastapi import APIRouter, HTTPException
from redis_publisher import publish

from .models import NotificationRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Notification System is up and running."}


@router.post("/notify")
async def create_notification(
    notification: NotificationRequest,
):
    try:
        channel = "db_service"
        event = {
            "topic": f"{notification.topic}",
            "description": f"{notification.description}",
        }
        publish(channel, event)

        return {
            "message": f"Your message was received. Topic:{notification.topic}. Thanks"
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex)) from ex

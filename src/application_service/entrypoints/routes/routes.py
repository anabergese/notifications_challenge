import logging

from entrypoints.dependencies import get_notification_service
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException

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
    background_tasks: BackgroundTasks,
    notification_service=Depends(get_notification_service),
):
    try:
        background_tasks.add_task(notification_service.send_notification, notification)
        return {"message": "Your message was received. Thanks"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex)) from ex

import logging

from entrypoints.dependencies import get_channel, get_publish_to_channel
from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException

from .models import NotificationRequest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Notification System is up and running."}


@router.post("/notification")
async def add_notification_to_channel(
    request: NotificationRequest,
    background_tasks: BackgroundTasks,
    channel_connection=Depends(get_channel),
    publish_to_channel=Depends(get_publish_to_channel),
):
    try:
        notification = request.create_notification()
        background_tasks.add_task(publish_to_channel, notification, channel_connection)
        return {"message": "Your message was received. Thanks"}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex)) from ex

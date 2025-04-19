import logging
from typing import Any, Dict

from fastapi import APIRouter, Depends, Response, status

from application.messagebus import MessageBus
from entrypoints.dependencies import get_message_bus

from .models import ErrorResponse, NotificationRequest, NotificationResponse

router = APIRouter()


@router.get("/")
def read_root() -> Response:
    return Response(
        content='{"message": "Notification System is up and running."}',
        media_type="application/json",
    )


@router.get("/health")
async def health() -> Dict[str, Any]:
    return {"status": "pass", "description": "Notifications API"}


@router.post(
    "/notify",
    name="Create a new notification",
    summary="Create a new notification for a specific topic.",
    description="Creates a new notification that will be redirected to different channels.",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Notification created successfully.",
            "model": NotificationResponse,
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "description": "Validation error in the request.",
            "model": ErrorResponse,
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error.",
            "model": ErrorResponse,
        },
    },
)
async def create_notification(
    notification: NotificationRequest,
    message_bus: MessageBus = Depends(get_message_bus),
) -> NotificationResponse:
    notification_created = notification.map_to()
    logging.info("notification_created data type: %s", type(notification_created))
    await message_bus.handle(notification_created)
    return NotificationResponse(
        message="Notification created successfully.", topic=notification.topic
    )

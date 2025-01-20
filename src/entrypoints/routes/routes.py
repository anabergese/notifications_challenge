from fastapi import APIRouter, Depends, Response, status

from entrypoints.dependencies import get_message_bus
from service_layer.messagebus import MessageBus

from .models import ErrorResponse, NotificationRequest, NotificationResponse

router = APIRouter()


@router.get("/")
def read_root() -> Response:
    return Response(
        content='{"message": "Notification System is up and running."}',
        media_type="application/json",
    )


@router.post(
    "/notify",
    name="Create a new notification",
    summary="Create a new notification for a specific topic.",
    description="Allows creating a new notification for a specific topic by the bot, that will be redirected to different channels.",
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
    await message_bus.handle(notification.map_to())
    return NotificationResponse(
        message="Notification created successfully.", topic=notification.topic
    )

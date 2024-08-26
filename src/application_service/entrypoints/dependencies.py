from fastapi import HTTPException, Request
from infrastructure.redis import redis_client
from service_layer.redis_channel import RedisNotificationChannel
from service_layer.service import NotificationService


async def get_notification_service(request: Request):
    if not hasattr(request.app.state, "channel"):
        raise HTTPException(
            status_code=500, detail="Channel connection is not available."
        )
    # Crear una instancia de RedisNotificationChannel utilizando la conexión de Redis
    channel = RedisNotificationChannel(request.app.state.channel)
    return NotificationService(channel)


async def get_message_broker():
    return redis_client

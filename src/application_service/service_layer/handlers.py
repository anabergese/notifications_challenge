from domain.enums import RedisChannels
from domain.events import NotificationCreated
from redis_publisher import publish


async def handle_notification_created(event: NotificationCreated):
    """Handler para procesar el evento NotificationCreated."""
    # Publica el evento a Redis
    channel = RedisChannels.DB_SERVICE.value
    data = {
        "topic": event.topic,
        "description": event.description,
        "timestamp": event.timestamp.isoformat(),  # Convertir a string si necesario
    }
    await publish(channel, data)  # Asegúrate de que `publish` también sea asíncrono

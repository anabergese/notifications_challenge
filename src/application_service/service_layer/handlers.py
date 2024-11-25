from domain.events import NotificationCreated
from redis_publisher import publish


async def handle_notification_created(event: NotificationCreated):
    """Handler para procesar el evento NotificationCreated."""
    # Publica el evento a Redis
    channel = "db_service"
    data = {"topic": event.topic, "description": event.description}
    await publish(channel, data)  # Asegúrate de que `publish` también sea asíncrono

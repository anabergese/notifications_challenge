from datetime import datetime, timezone

from domain.events import NotificationCreated
from service_layer.messagebus import handle


class NotificationService:
    @staticmethod
    async def create_notification(topic: str, description: str):
        # Generar el evento
        event = NotificationCreated(
            topic=topic,
            description=description,
            timestamp=datetime.now(timezone.utc),
        )
        # Pasar el evento al MessageBus
        await handle(event)

        return event

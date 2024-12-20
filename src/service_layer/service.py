import logging
from datetime import datetime, timezone

from domain.events import NotificationCreated

from . import messagebus


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
        try:
            await messagebus.handle(event)
        except Exception as e:
            logging.error("Error handling event: %s. Event: %s", e, event)
        return event

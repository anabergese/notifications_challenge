import logging

from domain.events import NotificationCreated

from . import messagebus


class NotificationService:
    @staticmethod
    async def create_notification(topic: str, description: str) -> NotificationCreated:
        # Generar el evento
        event = NotificationCreated(
            topic=topic,
            description=description,
        )

        # Pasar el evento al MessageBus
        try:
            await messagebus.handle(event)
        except (ValueError, TypeError, RuntimeError) as e:
            logging.error("Error handling event: %s. Event: %s", e, event)
        return event

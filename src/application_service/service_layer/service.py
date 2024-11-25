from domain.events import NotificationCreated
from service_layer.messagebus import handle


class NotificationService:
    @staticmethod
    async def create_notification(topic: str, description: str):
        # Lógica de negocio, si aplica, por ejemplo, validaciones.
        if not topic or not description:
            raise ValueError("Topic and description are required")

        # Generar el evento
        event = NotificationCreated(topic=topic, description=description)

        # Pasar el evento al MessageBus
        await handle(event)

        return event

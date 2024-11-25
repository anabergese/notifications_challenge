import asyncio

from application_service.domain.events import NotificationCreated
from application_service.service_layer.messagebus import handle, register_handler


async def dummy_handler(event):
    print(f"Handled event: {event.topic} - {event.description}")


# Registrar el handler de prueba
register_handler(NotificationCreated, dummy_handler)


async def test_messagebus():
    event = NotificationCreated(topic="test", description="Testing MessageBus")
    await handle(event)


# Ejecutar la prueba
if __name__ == "__main__":
    asyncio.run(test_messagebus())

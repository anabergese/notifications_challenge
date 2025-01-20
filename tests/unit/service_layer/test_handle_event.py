import logging
from collections.abc import Callable, Coroutine
from typing import Any

import pytest

from src.application.handlers import handle_notification_received
from src.application.messagebus import MessageBus
from src.domain.events import DomainEvent, NotificationReceived

EVENT_HANDLERS: dict[
    type[DomainEvent], list[Callable[..., Coroutine[Any, Any, None]]]
] = {
    NotificationReceived: [handle_notification_received],
}


@pytest.mark.asyncio
async def test_message_bus_handles_event():
    # Creamos un evento de prueba
    event = NotificationReceived(
        topic="sales", description="This is a test for sales notification"
    )

    # Creamos el MessageBus con los handlers registrados
    message_bus = MessageBus(
        handlers=EVENT_HANDLERS,
    )

    # El MessageBus maneja el evento
    await message_bus.handle(event)

    # Verificamos que los handlers del MessageBus siguen siendo un diccionario
    assert isinstance(message_bus.handlers, dict)

    # Aquí podrías verificar los efectos secundarios de `handle_notification_received`
    # Por ejemplo, si guarda algo en la base de datos o genera algún resultado


@pytest.mark.asyncio
async def test_handle_event():
    # Creamos un evento de prueba
    event = NotificationReceived(
        topic="sales", description="This is a test for sales notification"
    )

    # Ejecutamos el handler directamente
    result = await handle_notification_received(event)

    # Verificamos que el resultado sea un diccionario con los valores esperados
    assert isinstance(result, dict)
    assert result["topic"] == "sales"
    assert result["description"] == "This is a test for sales notification"
    assert result["version"] == "1.0"

    # Creamos el MessageBus y verificamos que maneja correctamente el evento
    message_bus = MessageBus(
        handlers=EVENT_HANDLERS,
    )
    await message_bus.handle(event)

    # Verificamos que los handlers del MessageBus siguen siendo un diccionario
    assert isinstance(message_bus.handlers, dict)

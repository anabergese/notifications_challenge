import asyncio

import pytest
from redis.exceptions import ConnectionError

from domain.enums import RedisChannels
from domain.events import NotificationCreated
from service_layer.handlers import handle_notification_created


@pytest.mark.asyncio
async def test_retry_with_exponential_backoff(mocker):
    # Mock del método publish del cliente Redis
    mock_publish = mocker.patch(
        "handle_notification_created.publish",
        side_effect=ConnectionError("Simulated connection error"),
    )

    # Mockear asyncio.sleep para controlar el tiempo de backoff
    mock_sleep = mocker.patch("asyncio.sleep", new_callable=mocker.AsyncMock)

    # Simular un evento NotificationCreated
    event = NotificationCreated(
        topic="sales",
        description="TestDesc TestDesc",
        timestamp=asyncio.run(asyncio.sleep(0.05)),
    )

    # Ejecutar el handler
    await handle_notification_created(event)

    # Verificar que publish fue llamado 3 veces (1 intento inicial + 2 reintentos)
    assert mock_publish.call_count == 3

    # Verificar que asyncio.sleep fue llamado con los valores de backoff exponencial: 2, 4 segundos
    mock_sleep.assert_any_call(2)
    mock_sleep.assert_any_call(4)

    # Verificar que el handler no hace más reintentos después del número máximo configurado
    assert mock_sleep.call_count == 2

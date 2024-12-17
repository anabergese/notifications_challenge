import asyncio

import pytest

from domain.enums import RedisChannels
from domain.events import NotificationCreated
from service_layer.handlers import handle_notification_created


@pytest.mark.asyncio
async def test_handle_notification_created_success(mocker, valid_inputs):
    """Test: publish se ejecuta sin errores."""

    event = NotificationCreated(**valid_inputs)
    mock_publish = mocker.patch("service_layer.handlers.publish", return_value=None)

    await handle_notification_created(event)

    mock_publish.assert_called_once_with(
        RedisChannels.DB_SERVICE.value,
        {
            "topic": "pricing",
            "description": "New pricing update available.",
            "timestamp": valid_inputs["timestamp"].isoformat(),
        },
    )

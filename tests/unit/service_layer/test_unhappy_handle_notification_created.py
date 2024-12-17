import asyncio

import pytest
from redis.exceptions import ConnectionError as RedisConnectionError

from domain.events import NotificationCreated
from service_layer.handlers import handle_notification_created


@pytest.mark.asyncio
async def test_handle_notification_created_with_retries(mocker, valid_inputs):
    """Test: publish falla varias veces antes de tener éxito."""

    event = NotificationCreated(**valid_inputs)
    mock_publish = mocker.patch(
        "service_layer.handlers.publish",
        side_effect=[
            RedisConnectionError("Fail 1"),
            RedisConnectionError("Fail 2"),
            None,
        ],
    )
    mock_sleep = mocker.patch("asyncio.sleep", return_value=None)

    await handle_notification_created(event)

    assert mock_publish.call_count == 3
    mock_sleep.assert_has_calls([mocker.call(2), mocker.call(4)])


@pytest.mark.asyncio
async def test_handle_notification_created_max_retries(mocker, valid_inputs):
    """Test: publish falla en todos los intentos."""

    event = NotificationCreated(**valid_inputs)
    mock_publish = mocker.patch(
        "service_layer.handlers.publish", side_effect=RedisConnectionError("Fail")
    )
    mock_sleep = mocker.patch("asyncio.sleep", return_value=None)
    mock_log_error = mocker.patch("logging.error")

    await handle_notification_created(event)

    assert mock_publish.call_count == 3
    mock_sleep.assert_has_calls([mocker.call(2), mocker.call(4)])
    mock_log_error.assert_called_once()


@pytest.mark.asyncio
async def test_handle_notification_created_unexpected_error(mocker, valid_inputs):
    """Test: publish lanza una excepción inesperada."""

    event = NotificationCreated(**valid_inputs)
    mock_publish = mocker.patch(
        "service_layer.handlers.publish", side_effect=ValueError("Unexpected error")
    )
    mock_log_critical = mocker.patch("logging.critical")

    await handle_notification_created(event)

    assert mock_publish.call_count == 1
    mock_log_critical.assert_called_once()

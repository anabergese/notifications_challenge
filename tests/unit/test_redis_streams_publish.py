import logging

import pytest

from config import get_redis_client
from domain import enums


async def custom_publish(stream_key: enums.RedisStreams.NOTIFICATIONS, event):  # type: ignore
    try:
        logging.info("Tipo de dato a ser publicado: %s", type(event))
        redis_client = get_redis_client()
        await redis_client.xadd(stream_key, event)
    except Exception as e:
        logging.error("Error publishing to stream: %s", str(e))
        raise


@pytest.mark.asyncio
async def test_publish_with_custom_implementation_dict():

    mock_event = {
        "topic": "pricing",
        "description": "344 aaa i will be a dev in 2025 this year!",
    }
    await custom_publish("notifications", mock_event)

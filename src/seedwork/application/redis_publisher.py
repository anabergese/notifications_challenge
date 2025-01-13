import logging
from dataclasses import asdict

from config import get_redis_client
from domain.enums import RedisStreams
from domain.events import NotificationCreated


async def publish(stream_key: RedisStreams, event: NotificationCreated) -> None:
    try:
        redis = get_redis_client()
        logging.info("Data type received by redis before publishing: %s", type(event))
        serialized_event = asdict(event)
        await redis.xadd(stream_key, serialized_event)
    except Exception as e:
        logging.error("Error publishing to stream: %s", str(e))
        raise

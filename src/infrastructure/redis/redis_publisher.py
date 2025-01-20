import logging
from dataclasses import asdict

from domain.enums import RedisStreams
from domain.events import NotificationCreated
from infrastructure.redis.redis_initialization import get_redis_client


async def publish(
    event: NotificationCreated, stream_key: RedisStreams = RedisStreams.NOTIFICATIONS
) -> None:
    try:
        redis = get_redis_client()
        logging.info("Data type received by redis before publishing: %s", type(event))
        serialized_event = asdict(event)
        await redis.xadd(stream_key.value, serialized_event)
    except Exception as e:
        logging.error("Error publishing to stream: %s", str(e))
        raise

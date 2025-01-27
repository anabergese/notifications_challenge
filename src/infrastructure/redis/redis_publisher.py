import logging
from dataclasses import asdict

from domain.events import NotificationCreated
from domain.publisher_enums import RedisStreams
from infrastructure.redis.redis_initialization import get_redis_client


async def publish(
    event: NotificationCreated, stream_key: RedisStreams = RedisStreams.NOTIFICATIONS
) -> None:
    try:
        redis = get_redis_client()
        logging.info("Publishing event in Redis Streams...")
        serialized_event = asdict(event)
        await redis.xadd(stream_key.value, serialized_event)
    except Exception as e:
        logging.error("Error publishing to stream: %s", str(e))
        raise

import logging
from dataclasses import asdict

from config import get_redis_client
from domain import enums, events

r = get_redis_client()


async def publish(stream_key: enums.RedisStreams.NOTIFICATIONS, event: events.Event):  # type: ignore
    try:
        logging.info("Data type received by redis before publishing: %s", type(event))
        serialized_event = asdict(event)
        await r.xadd(stream_key, serialized_event)
    except Exception as e:
        logging.error("Error publishing to stream: %s", str(e))
        raise

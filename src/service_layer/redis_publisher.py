import json
import logging

from infrastructure.redis_client import get_redis_client

logger = logging.getLogger(__name__)

r = get_redis_client()


async def publish(channel: str, event: dict):
    logging.info("Log from redis_publisher.py: channel=%s, event=%s", channel, event)
    await r.publish(channel, json.dumps((event)))

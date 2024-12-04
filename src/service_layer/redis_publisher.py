import json
import logging

from infrastructure.redis_client import get_redis_client

r = get_redis_client()


async def publish(channel: str, event: dict):
    logging.info("Publishing event...: channel=%s, event=%s", channel, event)
    await r.publish(channel, json.dumps((event)))

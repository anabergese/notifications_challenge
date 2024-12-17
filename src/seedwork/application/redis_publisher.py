import json
import logging

from config import get_redis_client
from domain import events

r = get_redis_client()


async def publish(channel: str, event: events.Event):
    logging.info("Publishing event...: channel=%s, event=%s", channel, event)
    await r.publish(channel, json.dumps((event)))

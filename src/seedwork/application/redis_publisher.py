import json
import logging
from dataclasses import asdict

from config import get_redis_client
from domain import events

r = get_redis_client()


async def publish(channel: str, event: events.Event) -> None:
    serialized_event = json.dumps(asdict(event))
    logging.info(
        "Publishing serialized event: %s to channel: %s", serialized_event, channel
    )
    await r.publish(channel, serialized_event)

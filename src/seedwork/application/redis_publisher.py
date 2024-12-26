import json
import logging
from dataclasses import asdict

from config import get_redis_client
from domain import events

r = get_redis_client()


async def publish(channel: str, event: events.Event):  # type: ignore
    logging.info("Tipo de dato a ser publicado: %s", type(event))
    serialized_event = json.dumps(asdict(event))
    logging.info(
        "Publishing serialized event: %s to channel: %s", serialized_event, channel
    )
    # Guardar el evento en una lista en Redis
    await r.rpush(f"{channel}", serialized_event)

    await r.publish(channel, serialized_event)

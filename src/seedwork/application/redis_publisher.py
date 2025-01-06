import logging
from dataclasses import asdict

from config import get_redis_client
from domain import events

r = get_redis_client()


async def publish(stream_key: str, event: events.Event):  # type: ignore
    try:
        logging.info("Tipo de dato a ser publicado: %s", type(event))
        serialized_event = asdict(event)
        logging.info(
            "Publishing serialized event: %s to stream: %s",
            serialized_event,
            stream_key,
        )
        # Publicar el evento en el stream
        await r.xadd(stream_key, serialized_event)
    except Exception as e:
        logging.error("Error publishing to stream: %s", str(e))
        raise

import asyncio
import logging

from domain.enums import RedisChannels
from domain.events import NotificationCreated
from redis.exceptions import ConnectionError, TimeoutError
from redis_publisher import publish

logger = logging.getLogger(__name__)


async def handle_notification_created(event: NotificationCreated):
    """Handler para procesar el evento NotificationCreated."""

    channel = RedisChannels.DB_SERVICE.value
    data = {
        "topic": event.topic,
        "description": event.description,
        "timestamp": event.timestamp.isoformat(),
    }

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            await publish(channel, data)
            logger.info(
                "Successfully published event to Redis channel %s: %s", channel, data
            )
            break  # Sal del bucle si la publicación es exitosa
        except (ConnectionError, TimeoutError) as redis_error:
            logger.warning(
                "Attempt %d failed to publish to Redis: %s", attempt, redis_error
            )
            if attempt < max_retries:
                await asyncio.sleep(2**attempt)  # Backoff exponencial: 2, 4, 8 segundos
            else:
                logger.error(
                    "Max retries reached. Failed to publish event to Redis: %s", data
                )
        except Exception as unexpected_error:
            logger.critical("Unexpected error in Redis operation: %s", unexpected_error)
            break  # Sal del bucle si ocurre un error no esperado

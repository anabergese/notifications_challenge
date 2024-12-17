import asyncio
import logging

from redis.exceptions import BusyLoadingError
from redis.exceptions import ConnectionError as RedisConnectionError
from redis.exceptions import TimeoutError as RedisTimeoutError

from domain.enums import RedisChannels
from domain.events import NotificationCreated
from seedwork.application.redis_publisher import publish


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
            await publish(channel, data)  # si hay error aqui va para DLQ
            logging.info("Event published %s: %s", channel, data)
            break
        except (
            RedisConnectionError,
            RedisTimeoutError,
            BusyLoadingError,
        ) as redis_error:
            logging.warning("Attempt %d failed to publish: %s", attempt, redis_error)
            if attempt < max_retries:
                await asyncio.sleep(2**attempt)  # Backoff exponencial: 2, 4, 8 segundos
            else:
                logging.error(
                    "Max retries reached. Failed to publish event to Redis: %s", data
                )
        except Exception as unexpected_error:
            logging.critical(
                "Unexpected error in Redis operation: %s", unexpected_error
            )
            break

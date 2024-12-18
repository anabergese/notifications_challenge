import asyncio
import logging

from redis.exceptions import BusyLoadingError
from redis.exceptions import ConnectionError as RedisConnectionError
from redis.exceptions import TimeoutError as RedisTimeoutError

from domain.enums import RedisChannels
from domain.events import NotificationCreated
from seedwork.application import redis_publisher


async def handle_notification_created(event: NotificationCreated) -> None:
    """Handler para procesar el evento NotificationCreated."""

    channel = RedisChannels.DB_SERVICE.value

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            await redis_publisher.publish(
                channel, event
            )  # si hay error aqui va para DLQ
            logging.info("Event published %s: %s", channel, event)
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
                    "Max retries reached. Failed to publish event to Redis: %s", event
                )
        except Exception as unexpected_error:
            logging.critical(
                "Unexpected error in Redis operation: %s", unexpected_error
            )
            break

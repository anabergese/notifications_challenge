import asyncio
import logging
from typing import Any, Callable, Coroutine, Dict, List, Literal, Type

from domain.events import Event, NotificationCreated, NotificationSaved


async def handle_notification_created(
    event: NotificationCreated,
    publish: Callable[[str, NotificationCreated], Coroutine[Any, Any, None]],
    stream_key: str = "notifications",
) -> None:

    max_retries: int = 3
    for attempt in range(1, max_retries + 1):
        try:
            await publish(stream_key, event)
            logging.info("Event published %s: %s", stream_key, event)
            break
        except (AttributeError, TypeError, ValueError) as data_error:
            logging.error("Data-related error during publish: %s", data_error)
            break
        except (TimeoutError, OSError, ConnectionError) as infra_error:
            logging.warning(
                "Attempt %d failed due to infrastructure error: %s",
                attempt,
                infra_error,
            )
            if attempt < max_retries:
                await asyncio.sleep(2**attempt)  # Backoff exponencial: 2, 4, 8 segundos
            else:
                logging.error("Max retries reached. Failed to publish event: %s", event)
        except Exception as unexpected_error:
            logging.critical(
                "Unexpected error during publish operation, going to DLQ: %s",
                unexpected_error,
            )
            break


async def handle_notification_saved(event: NotificationSaved) -> None:
    logging.info("NOTIFICATION SAVED IN DATABASE YEAH: %s", event)


INITIAL_HANDLERS: Dict[
    Type[Event],
    List[Callable[..., Coroutine[Any, Any, None]]],
] = {
    NotificationCreated: [handle_notification_created],
    NotificationSaved: [handle_notification_saved],
}

import logging
from typing import Any, Callable, Coroutine, Dict, List, Type

from domain.events import DomainEvent, NotificationCreated, NotificationReceived
from workers.orchestrator import NotificationOrchestrator


async def handle_notification_created(
    event: NotificationCreated,
    publish: Callable[[NotificationCreated], Coroutine[Any, Any, None]],
) -> None:
    try:
        await publish(event)
        logging.info("Event published: %s", event)
    except (AttributeError, TypeError, ValueError) as data_error:
        logging.error("Data-related error during publish: %s", data_error)


async def handle_notification_received(
    event: NotificationReceived, orchestrator: NotificationOrchestrator
):
    logging.info("Notificacion recibida y por ser enviada a orchestrator: %s", event)
    await orchestrator.process_message(event)


EVENT_HANDLERS: Dict[
    Type[DomainEvent],
    List[Callable[..., Coroutine[Any, Any, None]]],
] = {
    NotificationCreated: [handle_notification_created],
    NotificationReceived: [handle_notification_received],
}

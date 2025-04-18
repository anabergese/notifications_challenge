from typing import Any, Callable, Coroutine, Dict, List, Type

from domain.events import DomainEvent, NotificationCreated, NotificationReceived
from workers.orchestrator import NotificationOrchestrator


async def handle_notification_created(
    event: NotificationCreated,
    publish: Callable[[NotificationCreated], Coroutine[Any, Any, None]],
) -> None:
    await publish(event)


async def handle_notification_received(
    event: NotificationReceived, orchestrator: NotificationOrchestrator
):
    await orchestrator.process_message(event)


EVENT_HANDLERS: Dict[
    Type[DomainEvent],
    List[Callable[..., Coroutine[Any, Any, None]]],
] = {
    NotificationCreated: [handle_notification_created],
    NotificationReceived: [handle_notification_received],
}

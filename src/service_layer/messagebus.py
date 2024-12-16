import asyncio
from typing import Callable, Dict, List, Type

from domain import events

from .handlers import handle_notification_created


async def handle(event):
    """Invoca los handlers registrados para un evento dado."""
    for handler in HANDLERS[type(event)]:
        await handler(event)


HANDLERS: Dict[Type[events.Event], List[Callable]] = {
    events.NotificationCreated: [handle_notification_created],
}

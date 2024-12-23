import asyncio
import logging
from typing import Any, Callable, Coroutine, Dict, List, Type

from domain import events


class MessageBus:
    def __init__(
        self,
        handlers: Dict[
            Type[events.Event], List[Callable[..., Coroutine[Any, Any, None]]]
        ],
    ):
        """
        Inicializa el MessageBus con un diccionario de handlers.

        :param handlers: Un diccionario que asocia tipos de eventos con listas de handlers.
        """
        self.handlers = handlers

    async def handle(self, event: events.Event) -> None:
        """
        Maneja un evento invocando los handlers registrados para ese tipo de evento.
        """
        event_type = type(event)
        if event_type not in self.handlers:
            logging.error("No handlers registered for event type: %s", event_type)
            raise ValueError(f"No handlers registered for event type: {event_type}")

        for handler in self.handlers[type(event)]:
            try:
                logging.debug("Handling event %s with handler %s", event, handler)
                await handler(event)
            except Exception:
                logging.exception(
                    "Exception handling event %s with handler %s", event, handler
                )
                continue

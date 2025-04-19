import logging
from typing import Any, Callable, Coroutine, Dict, List, Type

from domain.events import DomainEvent

from .retry_mechanism import retry_with_backoff


class MessageBus:
    """Responsible for dispatching domain events to the appropriate handlers."""

    def __init__(
        self,
        handlers: Dict[
            Type[DomainEvent], List[Callable[..., Coroutine[Any, Any, None]]]
        ],
    ):
        self.handlers = handlers

    async def handle(self, event: DomainEvent) -> None:
        event_type = type(event)
        if event_type not in self.handlers:
            logging.error("No handlers registered for event type: %s", event_type)
            raise ValueError(f"No handlers registered for event type: {event_type}")

        for handler in self.handlers[event_type]:
            try:
                logging.info("Handling event %s with handler %s", event, handler)
                await retry_with_backoff(
                    func=handler,
                    args=(event,),
                    exceptions=(TimeoutError, OSError, ConnectionError),
                )
            except (TimeoutError, OSError, ConnectionError) as e:
                logging.critical(
                    "GOING TO DLQ: Exception handling event %s with handler %s, with error %s",
                    event,
                    handler,
                    e,
                )
                continue

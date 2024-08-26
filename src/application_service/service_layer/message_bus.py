import logging
from typing import Callable, Dict, List, Type

from domain.system_events import Event

logger = logging.getLogger(__name__)


class MessageBus:
    def __init__(self):
        self._handlers: Dict[Type[Event], List[Callable[[Event], None]]] = {}

    def subscribe(self, event_type: Type[Event], handler: Callable[[Event], None]):
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def publish(self, event: Event):
        event_type = type(event)
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                try:
                    logger.debug("Handling event %s with handler %s", event, handler)
                    handler(event)
                except Exception as e:
                    logger.exception("Exception handling event %s: %s", event, e)
                    continue  # Sigue con el siguiente handler en caso de fallo

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
        # Validación opcional para asegurarse de que el handler acepta un evento como parámetro
        if not callable(handler):
            raise ValueError(f"Handler {handler} is not callable")
        self._handlers[event_type].append(handler)

    def publish(self, event: Event):
        event_type = type(event)
        logger.info("Publishing event %s", event)

        if event_type in self._handlers:
            exceptions = []
            for handler in self._handlers[event_type]:
                try:
                    logger.debug("Handling event %s with handler %s", event, handler)
                    handler(event)
                except Exception as e:
                    logger.exception("Exception handling event %s: %s", event, e)
                    exceptions.append(e)
                    continue  # Sigue con el siguiente handler en caso de fallo

            if exceptions:
                # Si es necesario, puedes lanzar una excepción agregada o hacer algo con las excepciones acumuladas
                raise RuntimeError(
                    f"Exceptions occurred while handling event {event_type}: {exceptions}"
                )

        else:
            logger.warning("No handlers found for event type %s", event_type)

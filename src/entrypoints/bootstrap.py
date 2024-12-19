from typing import Callable, Dict, List, Type

from domain import events
from service_layer.handlers import handle_notification_created
from service_layer.messagebus import MessageBus


def bootstrap(
    handlers: Dict[Type[events.Event], List[Callable]] = None,
) -> MessageBus:
    """
    Initializes the application, injects dependencies, and returns the MessageBus.

    :param handlers: Optional custom handlers to override the defaults.
    :return: An initialized MessageBus.
    """
    default_handlers = {
        events.NotificationCreated: [handle_notification_created],
    }

    handlers = handlers or default_handlers

    message_bus = MessageBus(handlers=handlers)

    return message_bus

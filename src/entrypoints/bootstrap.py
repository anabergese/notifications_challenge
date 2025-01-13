import inspect
from typing import Any, Callable, Coroutine

from domain.enums import RedisStreams
from domain.events import NotificationCreated
from service_layer.handlers import INITIAL_HANDLERS
from service_layer.messagebus import MessageBus


def bootstrap(
    publish: Callable[[RedisStreams, NotificationCreated], Coroutine[Any, Any, None]]
) -> MessageBus:

    dependencies = {
        "publish": publish,
    }

    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies) for handler in event_handlers
        ]
        for event_type, event_handlers in INITIAL_HANDLERS.items()
    }

    return MessageBus(handlers=injected_event_handlers)


def inject_dependencies(
    handler: Callable[..., Any], dependencies: dict[str, Any]
) -> Callable[[Any], Any]:
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda event: handler(event, **deps)

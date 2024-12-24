import inspect
from typing import Any, Callable, Coroutine

from domain.enums import RedisChannels
from seedwork.application import redis_publisher
from service_layer.handlers import INITIAL_HANDLERS
from service_layer.messagebus import MessageBus


def bootstrap(
    publish: Callable[[str, Any], Coroutine[Any, Any, None]] = redis_publisher.publish,
) -> MessageBus:

    dependencies = {
        "publish": publish,
        "channel": RedisChannels,
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

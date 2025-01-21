import inspect
from typing import Any, Callable, Coroutine

from application.handlers import EVENT_HANDLERS
from application.messagebus import MessageBus
from domain.enums import RedisStreams
from domain.events import NotificationCreated
from workers.orchestrator import NotificationOrchestrator


async def bootstrap(
    publish: Callable[[NotificationCreated, RedisStreams], Coroutine[Any, Any, None]],
    orchestrator: NotificationOrchestrator,
) -> MessageBus:

    dependencies = {
        "publish": publish,
        "orchestrator": orchestrator,
    }

    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies) for handler in event_handlers
        ]
        for event_type, event_handlers in EVENT_HANDLERS.items()
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

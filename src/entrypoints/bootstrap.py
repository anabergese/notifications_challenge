import inspect
from typing import Any, Callable, Coroutine, List

from application.handlers import EVENT_HANDLERS
from application.messagebus import MessageBus
from domain.enums import RedisStreams, Topic
from domain.events import NotificationCreated
from infrastructure.redis import redis_publisher
from workers.notification_channels import (
    EmailNotifier,
    NewNotifier,
    Notifier,
    SlackNotifier,
)
from workers.orchestrator import NotificationOrchestrator

notifiers_mapping: dict[Topic, List[Notifier]] = {
    Topic.SALES: [SlackNotifier()],
    Topic.PRICING: [EmailNotifier()],
    Topic.NEWTOPIC: [SlackNotifier(), EmailNotifier(), NewNotifier()],
}


async def bootstrap(
    publish: Callable[
        [NotificationCreated, RedisStreams], Coroutine[Any, Any, None]
    ] = redis_publisher.publish,
    orchestrator: NotificationOrchestrator = NotificationOrchestrator(
        notifiers_mapping
    ),
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

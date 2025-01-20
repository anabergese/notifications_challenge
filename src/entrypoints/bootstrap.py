import inspect
from typing import Any, Callable, Coroutine, Optional

from domain.enums import RedisStreams, Topic
from domain.events import NotificationCreated
from infrastructure.redis import redis_publisher
from service_layer.handlers import INITIAL_HANDLERS
from service_layer.messagebus import MessageBus
from workers.notification_channels import EmailNotifier, Notifier, SlackNotifier
from workers.orchestrator import NotificationOrchestrator


async def bootstrap(
    publish: Callable[
        [NotificationCreated, RedisStreams], Coroutine[Any, Any, None]
    ] = redis_publisher.publish,
    orchestrator: Optional[NotificationOrchestrator] = None,
) -> MessageBus:

    notifiers_mapping: dict[str, Notifier] = {
        Topic.SALES: SlackNotifier(),
        Topic.PRICING: EmailNotifier(),
    }

    orchestrator = orchestrator or NotificationOrchestrator(notifiers_mapping)

    dependencies = {
        "publish": publish,
        "orchestrator": orchestrator,
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

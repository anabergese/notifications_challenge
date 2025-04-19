from typing import Annotated, Any, Callable, Coroutine

from fastapi import Depends

from application.messagebus import MessageBus
from domain.events import NotificationCreated
from domain.publisher_enums import RedisStreams
from domain.topic_enums import Topic
from entrypoints.bootstrap import bootstrap
from infrastructure.redis.redis_publisher import publish
from workers.email_notifier import EmailNotifier
from workers.notification_orchestrator import NotificationOrchestrator
from workers.notifier import Notifier
from workers.slack_notifier import SlackNotifier


def get_publisher() -> (
    Callable[[NotificationCreated, RedisStreams], Coroutine[Any, Any, None]]
):
    return publish


def get_notifiers_mapping() -> dict[Topic, list[Notifier]]:
    return {
        Topic.SALES: [SlackNotifier()],
        Topic.PRICING: [EmailNotifier()],
    }


def get_orchestrator(
    notifiers_mapping: Annotated[
        dict[Topic, list[Notifier]], Depends(get_notifiers_mapping)
    ],
) -> NotificationOrchestrator:
    return NotificationOrchestrator(notifiers_mapping)


async def get_message_bus(
    publisher: Annotated[
        Callable[[NotificationCreated, RedisStreams], Coroutine[Any, Any, None]],
        Depends(get_publisher),
    ],
    orchestrator: Annotated[NotificationOrchestrator, Depends(get_orchestrator)],
) -> MessageBus:
    return await bootstrap(
        publish=publisher,
        orchestrator=orchestrator,
    )

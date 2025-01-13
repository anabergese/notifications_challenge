import asyncio
from typing import Any, Awaitable, Callable, Optional

from notification_channels import EmailNotifier, Notifier, SlackNotifier
from orchestrator import NotificationOrchestrator

from config import setup_logging
from domain.enums import RedisStreams, Topic
from seedwork.application.redis_consumer import start_redis_consumer

setup_logging()

notifiers_mapping: dict[str, Notifier] = {
    Topic.SALES: SlackNotifier(),
    Topic.PRICING: EmailNotifier(),
}

# Dict of strategies with functions, without starting them.
consumer_strategies: dict[str, Callable[[NotificationOrchestrator], Awaitable[Any]]] = {
    "redis": lambda orchestrator: start_redis_consumer(
        stream_key=RedisStreams.NOTIFICATIONS,
        group=RedisStreams.NOTIFICATIONS_GROUP,
        consumer=RedisStreams.NOTIFICATIONS_CONSUMER,
        orchestrator=orchestrator,
    ),
}


async def main() -> None:
    orchestrator = NotificationOrchestrator(notifiers_mapping)
    consumer: Optional[Callable[[NotificationOrchestrator], Awaitable[Any]]] = (
        consumer_strategies.get("redis")
    )
    if consumer:
        await consumer(orchestrator)
    else:
        raise ValueError("Consumer strategy for 'redis' not found.")


if __name__ == "__main__":
    asyncio.run(main())

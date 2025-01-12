import asyncio

from notification_channels import EmailNotifier, SlackNotifier
from orchestrator import NotificationOrchestrator

from config import setup_logging
from domain.enums import RedisStreams, Topic
from seedwork.application.redis_consumer import start_redis_consumer

setup_logging()

notifiers_mapping = {
    Topic.SALES: SlackNotifier(),
    Topic.PRICING: EmailNotifier(),
}


async def main() -> None:
    orchestrator = NotificationOrchestrator(notifiers_mapping)
    await start_redis_consumer(
        stream_key=RedisStreams.NOTIFICATIONS,
        group=RedisStreams.NOTIFICATIONS_GROUP,
        consumer=RedisStreams.NOTIFICATIONS_CONSUMER,
        orchestrator=orchestrator,
    )


if __name__ == "__main__":
    asyncio.run(main())

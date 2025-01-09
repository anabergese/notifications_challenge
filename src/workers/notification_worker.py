import asyncio

from notification_channels import EmailNotifier, SlackNotifier
from notification_orchestrator import NotificationOrchestrator

from config import setup_logging
from domain.enums import RedisStreams, Topic

setup_logging()

notifiers_mapping = {
    Topic.SALES: SlackNotifier(),
    Topic.PRICING: EmailNotifier(),
}


async def main() -> None:
    service = NotificationOrchestrator(
        notifiers_mapping,
        RedisStreams.NOTIFICATIONS,
        RedisStreams.NOTIFICATIONS_GROUP,
        RedisStreams.NOTIFICATIONS_CONSUMER,
    )
    await service.start()


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import logging

from notification_channels import EmailNotifier, SlackNotifier
from notification_orchestrator import NotificationOrchestrator

from config import setup_logging
from domain.enums import Topic

setup_logging()

notifiers_mapping = {
    Topic.SALES: SlackNotifier(),
    Topic.PRICING: EmailNotifier(),
}


async def main() -> None:
    service = NotificationOrchestrator(notifiers_mapping)
    await service.start()


if __name__ == "__main__":
    logging.info("Starting Notification Service...")
    asyncio.run(main())

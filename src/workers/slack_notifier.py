import asyncio
import logging

from domain.events import DomainEvent

from .notifier import Notifier


class SlackNotifier(Notifier):
    """SlackNotifier is a subclass of Notifier that implements the notify method"""

    async def notify(self, event: DomainEvent) -> str:
        try:
            logging.info("Processing event...: %s", event)
            await asyncio.sleep(3)
            success_message = f"Event with topic {event.topic} sent to SLACK successfully: {event.description}"
            logging.info(success_message)
            return success_message
        except Exception as e:
            logging.error("Event cannot be sent to SLACK: %s", e)
            raise

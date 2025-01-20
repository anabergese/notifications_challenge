import asyncio
import logging
from abc import ABC, abstractmethod

from domain.events import DomainEvent


class Notifier(ABC):
    @abstractmethod
    async def notify(self, event: DomainEvent) -> str:
        pass


class EmailNotifier(Notifier):
    async def notify(self, event: DomainEvent) -> str:
        logging.info("Processing event...: %s", event)
        await asyncio.sleep(3)
        success_message = f"Event with topic {event.topic} sent to EMAIL successfully: {event.description}"
        logging.info(success_message)
        return success_message


class SlackNotifier(Notifier):
    async def notify(self, event: DomainEvent) -> str:
        logging.info("Processing event...: %s", event)
        await asyncio.sleep(3)
        success_message = f"Event with topic {event.topic} sent to SLACK successfully: {event.description}"
        logging.info(success_message)
        return success_message

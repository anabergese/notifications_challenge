import asyncio
import json
import logging
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    async def notify(self, task_json: str):
        pass


class EmailNotifier(Notifier):
    async def notify(self, task_json: str):
        task = json.loads(task_json)
        logging.info("Processing event...: %s", task)
        await asyncio.sleep(3)
        logging.info(
            "Event %s sent to Email successfully: %s",
            task["topic"],
            task["description"],
        )


class SlackNotifier(Notifier):
    async def notify(self, task_json: str):
        task = json.loads(task_json)
        logging.info("Processing event...: %s", task)
        await asyncio.sleep(3)
        logging.info(
            "Event %s sent to Slack successfully: %s",
            task["topic"],
            task["description"],
        )

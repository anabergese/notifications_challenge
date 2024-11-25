import asyncio
import json
from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    async def notify(self, task_json: str):
        pass


class EmailNotifier(Notifier):
    async def notify(self, task_json: str):
        task = json.loads(task_json)
        print(f"Processing task from EmailNotifier: {task}")
        await asyncio.sleep(3)
        print(f"Task {task['topic']} sent to email successfully: {task['description']}")


class SlackNotifier(Notifier):
    async def notify(self, task_json: str):
        task = json.loads(task_json)
        print(f"Processing task from SlackNotifier: {task}")
        await asyncio.sleep(3)
        print(f"Task {task['topic']} sent to Slack successfully: {task['description']}")

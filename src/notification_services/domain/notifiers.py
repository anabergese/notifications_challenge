import json
import time
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, task_json: str):
        pass

class EmailNotifier(Notifier):
    def notify(self, task_json: str):
        task = json.loads(task_json)
        print(f"Processing task from EmailNotifier: {task['id']}")
        time.sleep(3)
        print(f"Task {task['topic']} sent to email successfully: {task['description']}")

class SlackNotifier(Notifier):
    def notify(self, task_json: str):
        task = json.loads(task_json)
        print(f"Processing task from SlackNotifier: {task['id']}")
        time.sleep(3)
        print(f"Task {task['topic']} sent to Slack successfully: {task['description']}")

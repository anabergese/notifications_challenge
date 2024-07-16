import os
import json
import time
import redis
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def notify(self, task_json: str):
        pass

class EmailNotifier(Notifier):
    def notify(self, task_json: str):
        task = json.loads(task_json)
        print(f"Processing task from worker: {task['id']}")
        time.sleep(3)
        print(f"Task {task['topic']} sent to email successfully: {task['description']}")

class SlackNotifier(Notifier):
    def notify(self, task_json: str):
        task = json.loads(task_json)
        print(f"Processing task from worker: {task['id']}")
        time.sleep(3)
        print(f"Task {task['topic']} sent to Slack successfully: {task['description']}")

class Worker:
    def __init__(self, redis_conn, notifiers):
        self.redis_conn = redis_conn
        self.notifiers = notifiers

    def process_task(self, task_json: str):
        task_data = json.loads(task_json)
        topic = task_data.get('topic')

        notifier = self.notifiers.get(topic)
        if notifier:
            notifier.notify(task_json)
        else:
            self.redis_conn.lpush('task_queue', task_json)
            print(f"Task {task_data['id']} requeued as it does not have a matching topic")

    def run(self):
        while True:
            try:
                task = self.redis_conn.brpop('task_queue', timeout=0)
                if task:
                    _, task_json = task
                    self.process_task(task_json)
            except Exception as e:
                print(f"Error processing task: {e}")
                # Optionally re-queue the task for retry if an error occurs
                # self.redis_conn.lpush('task_queue', task_json)

def create_redis_connection():
    return redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=int(os.getenv('REDIS_PORT', 6379)), db=0)

def main():
    redis_conn = create_redis_connection()

    notifiers = {
        'pricing': EmailNotifier(),
        'sales': SlackNotifier(),
        # 'other_topic': SlackNotifier(),
        # Add more notifiers as needed
    }

    worker = Worker(redis_conn, notifiers)
    worker.run()

if __name__ == "__main__":
    main()

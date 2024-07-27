import json

from redis import Redis


class Worker:
    def __init__(self, redis_conn: Redis, notifiers: dict):
        self.redis_conn = redis_conn
        self.notifiers = notifiers

    def process_task(self, task_json: str):
        task_data = json.loads(task_json)
        topic = task_data.get("topic")
        notifier = self.notifiers.get(topic)
        if notifier:
            try:
                notifier.notify(task_json)
            except Exception as e:
                print(f"Error notifying for task {task_data['id']}: {e}")
                self.redis_conn.rpush(
                    "notifications_queue", task_json
                )  # Re-enqueue on error
        else:
            self.redis_conn.rpush("notifications_queue", task_json)
            print(
                f"Task {task_data['id']} requeued as it does not have a matching topic"
            )

    def run(self):
        while True:
            try:
                task = self.redis_conn.blpop("notifications_queue", timeout=0)
                if task:
                    _, task_json = task
                    self.process_task(task_json)
            except Exception as e:
                print(f"Error processing task: {e}")
                # Optionally re-queue the task for retry if an error occurs
                # self.redis_conn.lpush('notifications_queue', task_json)

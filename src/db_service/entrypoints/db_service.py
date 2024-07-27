import json

from redis import Redis


class DBService:
    def __init__(self, redis_conn: Redis):
        self.redis_conn = redis_conn

    def save_task(self, task_json: str):
        task_data = json.loads(task_json)
        print(f"Saving task {task_data['id']} to the data base.....3...2...1...DONE!")

    def run(self):
        while True:
            try:
                task = self.redis_conn.blpop("task_queue", timeout=0)
                if task:
                    _, task_json = task
                    self.save_task(task_json)
                    self.redis_conn.rpush("notifications_queue", task_json)
                    print(f"Task {task_json} requeued from DB")

            except Exception as e:
                print(f"Error processing task: {e}")

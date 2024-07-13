import os
import json
import time
import redis

# Initialize Redis connection
# redis_conn = redis.Redis(host='localhost', port=6379, db=0)
redis_conn = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=int(os.getenv('REDIS_PORT', 6379)), db=0)

def process_task(task_json):
    task = json.loads(task_json)
    print(f"Processing task from worker: {task['id']}")
    # Simulate task processing
    time.sleep(3)
    print(f"Task {task['topic']} processed successfully: {task['description']}")

def worker():
    while True:
        try:
            task = redis_conn.brpop('task_queue', timeout=0)
            if task:
                _, task_json = task
                task_data = json.loads(task_json)
                if task_data.get('topic') == 'pricing':
                    process_task(task_json)
                else:
                # Optionally re-queue the task for another worker to process
                    redis_conn.lpush('task_queue', task_json)
                    print(f"Task {task_data['id']} requeued as it does not have the topic 'pricing'")
        except Exception as e:
            print(f"Error processing task: {e}")
            # Optionally re-queue the task for retry if an error occurs
            # redis_conn.lpush('task_queue', task_json)

# Example usage
if __name__ == "__main__":
    worker()

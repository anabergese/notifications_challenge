import json
from redis import Redis
from rq import Worker, Connection

# # Conexión a Redis
# redis_conn = Redis(host="redis", port=6379)

# # Referenciar la cola de tareas
# task_queue = Queue("task_queue")
#  tarea que se coloca en la cola
def process_message(message):
    print(f"Processing message from worker: {message}")
    message_data = json.loads(message)
    print(f"Message ID: {message_data['id']}")
    print(f"Topic: {message_data['topic']}")
    print(f"Description: {message_data['description']}")
    
listen = ['task_queue']

redis_conn = Redis(host="redis", port=6379)

if __name__ == '__main__':
    with Connection(redis_conn):
        w = Worker(listen, connection=redis_conn)
        w.work()

from redis import Redis
from rq import Worker, Connection

# # Conexión a Redis
# redis_conn = Redis(host="redis", port=6379)

# # Referenciar la cola de tareas
# task_queue = Queue("task_queue")

listen = ['task_queue']

redis_conn = Redis(host="redis", port=6379)

if __name__ == '__main__':
    with Connection(redis_conn):
        w = Worker(listen, connection=redis_conn)
        w.work()

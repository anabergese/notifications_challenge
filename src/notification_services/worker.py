import json
from redis import Redis
from rq import Worker, Queue, Connection

# Conexión a Redis
redis_conn = Redis(host="redis", port=6379)

# Referenciar la cola de tareas
task_queue = Queue("task_queue")

def process_message(message_json):
    """
    Procesa el mensaje de la cola `task_queue`.
    """
    print("Entrando a process message functon")
    try:
        message_data = json.loads(message_json)
        # print(f"Processing message with ID: {message_data['id']}")
        print(f"Topic: {message_data['topic']}")
        print(f"Description: {message_data['description']}")
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el mensaje: {e}")

if __name__ == "__main__":
    with Connection(redis_conn):
        print("Generando connection con worker")
        # Iniciar el worker con nombre personalizado 'foo' y asociarlo a la cola `task_queue`
        worker_foo = Worker([task_queue], connection=redis_conn, name='foo')
        worker_foo.work()


# import json

# def process_message(message):
#     print(f"Processing message from worker: {message}")
#     message_data = json.loads(message)
#     print(f"Message ID: {message_data['id']}")
#     print(f"Topic: {message_data['topic']}")
#     print(f"Description: {message_data['description']}")


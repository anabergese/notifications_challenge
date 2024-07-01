import os
import redis
import json

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
queue_name = "notification_queue"

def process_message(message):
    # Aquí defines cómo quieres procesar el mensaje
    print(f"Processing message: {message}")
    # Ejemplo: Convertir el mensaje JSON a un diccionario de Python
    message_data = json.loads(message)
    # Lógica de procesamiento del mensaje
    print(f"Message ID: {message_data['id']}")
    print(f"Topic: {message_data['topic']}")
    print(f"Description: {message_data['description']}")

def main():
    db = redis.Redis(
        host=redis_host,
        port=redis_port,
        db=0,
        decode_responses=True,
    )
    print("Worker connected to Redis, waiting for messages...")

    while True:
        try:
            # Usar BRPOP para esperar y obtener el mensaje de la cola
            message = db.brpop(queue_name, timeout=0)
            if message:
                queue, message = message
                process_message(message)
        except redis.ConnectionError:
            print("Failed to connect to Redis, retrying...")
            continue

if __name__ == "__main__":
    main()

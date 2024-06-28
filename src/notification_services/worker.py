import random
from json import loads
import redis
import os

print("Starting worker...")  # Mensaje de depuración inicial

# Configuración de Redis
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_db_number = 0  # Puedes ajustar según tus necesidades
redis_password = None  # Ajusta si necesitas contraseña
redis_queue_name = "notification_queue"

def redis_db():
    print("Connecting to Redis...")  # Mensaje de depuración
    db = redis.Redis(
        host=redis_host,
        port=redis_port,
        db=redis_db_number,
        password=redis_password,
        decode_responses=True,
    )
    try:
        db.ping()
        print("Connected to Redis")  # Mensaje de éxito
    except redis.ConnectionError:
        print("Failed to connect to Redis")  # Mensaje de error
    return db

def redis_queue_push(db, message):
    db.lpush(redis_queue_name, message)
    print("Message pushed to Redis queue")  # Mensaje de depuración

def redis_queue_pop(db):
    print("Waiting to pop message from Redis queue...")  # Mensaje de depuración
    _, message_json = db.brpop(redis_queue_name)
    return message_json

def process_message(db, message_json: str):
    print("Processing message...")  # Mensaje de depuración
    message = loads(message_json)
    print(f"Message received: id={message['id']}, topic={message['topic']}, description={message['description']}")

    processed_ok = random.choices((True, False), weights=(5, 1), k=1)[0]
    if processed_ok:
        print("Processed successfully")
        print(f"Message ID: {message['id']}")
    else:
        print("Processing failed - requeuing...")
        redis_queue_push(db, message_json)

def main():
    print("Starting main function...")  # Mensaje de depuración
    db = redis_db()

    while True:
        print("Waiting for message...")  # Mensaje de depuración
        message_json = redis_queue_pop(db)
        process_message(db, message_json)

if __name__ == '__main__':
    main()
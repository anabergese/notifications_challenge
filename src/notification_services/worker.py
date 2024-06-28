import random
from json import loads
import redis
import os

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_db_number = 0  # Puedes ajustar según tus necesidades
redis_password = None  # Ajusta si necesitas contraseña
redis_queue_name = "notification_queue"

def redis_db():
    db = redis.Redis(
        host=redis_host,
        port=redis_port,
        db=redis_db_number,
        password=redis_password,
        decode_responses=True,
    )
    db.ping()
    return db

def redis_queue_push(db, message):
    db.lpush(redis_queue_name, message)

def redis_queue_pop(db):
    _, message_json = db.brpop(redis_queue_name)
    return message_json

def process_message(db, message_json: str):
    message = loads(message_json)
    print(f"Message received: id={message['id']}, topic={message['topic']}, description={message['description']}")

    processed_ok = random.choices((True, False), weights=(5, 1), k=1)[0]
    if processed_ok:
        print("Processed successfully")
    else:
        print("Processing failed - requeuing...")
        redis_queue_push(db, message_json)

def main():
    db = redis_db()

    while True:
        message_json = redis_queue_pop(db)
        process_message(db, message_json)

if __name__ == '__main__':
    main()

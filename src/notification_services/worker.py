import random
from json import loads
import redis
import os

print("Starting worker...")

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_db_number = 0
redis_password = None
redis_queue_name = "notification_queue"

def redis_db():
    print("Connecting to Redis...")
    db = redis.Redis(
        host=redis_host,
        port=redis_port,
        db=redis_db_number,
        password=redis_password,
        decode_responses=True,
    )
    try:
        db.ping()
        print("Connected to Redis")
    except redis.ConnectionError:
        print("Failed to connect to Redis")
    return db

def redis_queue_push(db, message):
    db.lpush(redis_queue_name, message)
    print("Message pushed to Redis queue")

def redis_queue_pop(db):
    print("Waiting to pop message from Redis queue...")
    _, message_json = db.brpop(redis_queue_name)
    return message_json

def process_message(db, message_json: str):
    print("Processing message...")
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
    print("Starting main function...")
    db = redis_db()

    while True:
        print("Waiting for message...")
        message_json = redis_queue_pop(db)
        process_message(db, message_json)

if __name__ == '__main__':
    main()

import json
import os

import redis

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
)


async def start_redis():
    return redis_client


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


# def publish_message(channel, message):
#     redis_client.publish(channel, message)


async def add_message_to_redis_channel(message, redis_conn):
    redis_conn.publish("db_service", json.dumps(message.dict()))

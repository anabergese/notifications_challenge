# import os

# import redis

# redis_client = redis.Redis(
#     host=os.getenv("REDIS_HOST", "localhost"),
#     port=int(os.getenv("REDIS_PORT", 6379)),
#     db=0,
# )


# async def psubscribe(channel):
#     pubsub = redis_client.pubsub()
#     pubsub.subscribe(channel)
#     return pubsub


import json

# def publish_message(channel, message):
#     redis_client.publish(channel, message)
import os

import redis

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
)


async def create_redis_connection():
    return redis_client


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


def publish_message(channel, message):
    redis_client.publish(channel, message)


async def get_add_message_to_redis_queue():
    async def add_message_to_redis_queue(message, redis_conn):
        redis_conn.publish("task_queue", json.dumps(message.dict()))

    return add_message_to_redis_queue


# dependencies
async def get_redis_connection():
    return await create_redis_connection()


async def get_add_message_to_queue():
    return await get_add_message_to_redis_queue()

import json
import os

import redis
from domain.enums import RedisChannels

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    db=0,
)


async def start_redis():
    return redis_client


async def publish_to_redis(message, redis_conn):
    redis_conn.publish(RedisChannels.DB_SERVICE.value, json.dumps(message.dict()))

import os

from redis.asyncio import Redis


def get_redis_client():
    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = int(os.getenv("REDIS_PORT", "6379"))
    return Redis(host=redis_host, port=redis_port, db=0)

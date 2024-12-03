import os

from redis.asyncio import Redis
from redis.backoff import ExponentialBackoff
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError
from redis.retry import Retry


def get_redis_client():
    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = int(os.getenv("REDIS_PORT", "6379"))

    retry_strategy = Retry(ExponentialBackoff(), retries=3)

    return Redis(
        host=redis_host,
        port=redis_port,
        db=0,
        retry=retry_strategy,
        retry_on_error=[
            BusyLoadingError,
            ConnectionError,
            TimeoutError,
        ],
    )

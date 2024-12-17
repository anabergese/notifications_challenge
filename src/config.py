import logging
import os

from redis.asyncio import Redis
from redis.backoff import ExponentialBackoff
from redis.exceptions import BusyLoadingError
from redis.exceptions import ConnectionError as RedisConnectionError
from redis.exceptions import TimeoutError as RedisTimeoutError
from redis.retry import Retry

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))


def get_redis_client():
    retry_strategy = Retry(ExponentialBackoff(), retries=3)
    return Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        retry=retry_strategy,
        retry_on_error=[
            BusyLoadingError,
            RedisConnectionError,
            RedisTimeoutError,
        ],
    )


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - - %(module)s - %(message)s",
    )

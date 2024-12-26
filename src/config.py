import logging
import os

from redis.asyncio import Redis
from redis.asyncio.retry import Retry
from redis.backoff import ExponentialBackoff
from redis.exceptions import BusyLoadingError
from redis.exceptions import ConnectionError as RedisConnectionError
from redis.exceptions import TimeoutError as RedisTimeoutError

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
REDIS_USERNAME = os.getenv("REDIS_USERNAME", "default")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")


def get_redis_client() -> Redis:
    retry = Retry(ExponentialBackoff(), retries=3)  # type: ignore
    return Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        retry=retry,
        decode_responses=True,
        username=REDIS_USERNAME,
        password=REDIS_PASSWORD,
        retry_on_error=[
            BusyLoadingError,
            RedisConnectionError,
            RedisTimeoutError,
        ],
    )


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - - %(module)s - %(message)s",
    )

from redis.asyncio import Redis
from redis.backoff import ExponentialBackoff
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError
from redis.retry import Retry

from config import REDIS_DB, REDIS_HOST, REDIS_PORT


def get_redis_client():
    retry_strategy = Retry(ExponentialBackoff(), retries=3)

    return Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=REDIS_DB,
        retry=retry_strategy,
        retry_on_error=[
            BusyLoadingError,
            ConnectionError,
            TimeoutError,
        ],
    )

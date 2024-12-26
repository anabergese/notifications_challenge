import os

import pytest
from redis.exceptions import BusyLoadingError
from redis.exceptions import ConnectionError as RedisConnectionError
from redis.exceptions import TimeoutError as RedisTimeoutError

from config import get_redis_client


@pytest.mark.asyncio
async def test_get_redis_client_timeout_error(mocker):
    """Test: RedisTimeoutError ocurre al intentar crear un cliente de Redis."""

    mock_redis = mocker.patch(
        "config.Redis", side_effect=RedisTimeoutError("Connection timed out")
    )

    with pytest.raises(RedisTimeoutError, match="Connection timed out"):
        client = get_redis_client()
        await client.ping()

    mock_redis.assert_called_once_with(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        db=0,
        decode_responses=True,
        retry=mocker.ANY,
        retry_on_error=[BusyLoadingError, RedisConnectionError, RedisTimeoutError],
        username=os.getenv("REDIS_USERNAME"),
        password=os.getenv("REDIS_PASSWORD"),
    )


@pytest.mark.asyncio
async def test_get_redis_client_busy_loading_error(mocker):
    """Test: BusyLoadingError ocurre al intentar crear un cliente de Redis."""

    mock_redis = mocker.patch(
        "config.Redis", side_effect=BusyLoadingError("Busy Loading Error")
    )

    with pytest.raises(BusyLoadingError, match="Busy Loading Error"):
        client = get_redis_client()
        await client.ping()

    mock_redis.assert_called_once_with(
        host=os.getenv("REDIS_HOST"),
        port=int(os.getenv("REDIS_PORT")),
        db=0,
        decode_responses=True,
        retry=mocker.ANY,
        retry_on_error=[BusyLoadingError, RedisConnectionError, RedisTimeoutError],
        username=os.getenv("REDIS_USERNAME"),
        password=os.getenv("REDIS_PASSWORD"),
    )

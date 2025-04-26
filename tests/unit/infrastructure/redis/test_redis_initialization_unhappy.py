# import os

# import pytest
# from redis.exceptions import BusyLoadingError
# from redis.exceptions import ConnectionError as RedisConnectionError
# from redis.exceptions import TimeoutError as RedisTimeoutError

# from infrastructure.redis.redis_initialization import get_redis_client


# @pytest.fixture
# def mock_env_vars(monkeypatch):
#     monkeypatch.setenv("REDIS_HOST", "test-host")
#     monkeypatch.setenv("REDIS_PORT", "6380")
#     monkeypatch.setenv("REDIS_DB", "1")
#     monkeypatch.setenv("REDIS_USERNAME", "test-user")
#     monkeypatch.setenv("REDIS_PASSWORD", "test-pass")


# @pytest.mark.asyncio
# async def test_get_redis_client_timeout_error(mocker):
#     """Test: RedisTimeoutError ocurre al intentar crear un cliente de Redis."""

#     mock_redis = mocker.patch(
#         "infrastructure.redis.redis_initialization.get_redis_client",
#         side_effect=RedisTimeoutError("Connection timed out"),
#     )

#     with pytest.raises(RedisTimeoutError, match="Connection timed out"):
#         client = get_redis_client()
#         await client.ping()

#     mock_redis.assert_called_once_with(
#         host=os.getenv("REDIS_HOST"),
#         port=int(os.getenv("REDIS_PORT")),
#         db=0,
#         decode_responses=True,
#         retry=mocker.ANY,
#         retry_on_error=[BusyLoadingError, RedisConnectionError, RedisTimeoutError],
#         username=os.getenv("REDIS_USERNAME"),
#         password=os.getenv("REDIS_PASSWORD"),
#     )


# @pytest.mark.asyncio
# async def test_get_redis_client_busy_loading_error(mocker):
#     """Test: BusyLoadingError ocurre al intentar crear un cliente de Redis."""

#     mock_redis = mocker.patch(
#         "infrastructure.redis.redis_initialization.get_redis_client",
#         side_effect=BusyLoadingError("Busy Loading Error"),
#     )

#     with pytest.raises(BusyLoadingError, match="Busy Loading Error"):
#         client = get_redis_client()
#         await client.ping()

#     mock_redis.assert_called_once_with(
#         host=os.getenv("REDIS_HOST"),
#         port=int(os.getenv("REDIS_PORT")),
#         db=0,
#         decode_responses=True,
#         retry=mocker.ANY,
#         retry_on_error=[BusyLoadingError, RedisConnectionError, RedisTimeoutError],
#         username=os.getenv("REDIS_USERNAME"),
#         password=os.getenv("REDIS_PASSWORD"),
#     )

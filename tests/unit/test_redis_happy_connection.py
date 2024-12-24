import pytest

from config import get_redis_client


@pytest.mark.asyncio
async def test_default_connection():
    client = get_redis_client()
    assert await client.ping() is True


@pytest.mark.asyncio
async def test_custom_configuration():
    redis_client = get_redis_client()
    try:
        assert redis_client.connection_pool.connection_kwargs["host"] == "redis"
        assert redis_client.connection_pool.connection_kwargs["port"] == 6379
        assert redis_client.connection_pool.connection_kwargs["db"] == 0
    finally:
        await redis_client.close()
        redis_client.connection_pool.disconnect()

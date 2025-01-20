import os

import pytest

from infrastructure.redis.redis_initialization import get_redis_client


@pytest.mark.asyncio
async def test_default_connection():
    client = get_redis_client()
    assert await client.ping() is True

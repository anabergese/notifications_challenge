from typing import Union

from domain.enums import RedisStreams
from infrastructure.redis.redis_initialization import get_redis_client


async def initialize_redis_stream(
    stream_key: RedisStreams = RedisStreams.NOTIFICATIONS,
    consumer_group: RedisStreams = RedisStreams.NOTIFICATIONS_GROUP,
    last_id_delivered: Union[int, bytes, str, memoryview] = "$",
    auto_create: bool = True,
):
    """
    Creates the stream and consumer group in Redis if they do not exist.
    """
    try:
        redis = get_redis_client()
        await redis.xgroup_create(
            stream_key, consumer_group, last_id_delivered, auto_create
        )
    except Exception as e:
        if "BUSYGROUP" in str(e):
            print(f"Grupo '{consumer_group}' ya existe en el stream '{stream_key}'.")
        else:
            raise

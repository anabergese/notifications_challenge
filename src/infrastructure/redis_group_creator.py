from typing import Union

from config import get_redis_client
from domain.enums import RedisStreams

redis = get_redis_client()


async def initialize_redis_stream(
    stream_key: RedisStreams,
    consumer_group: RedisStreams,
    last_id_delivered: Union[int, bytes, str, memoryview] = "$",
    auto_create: bool = True,
):
    """
    Creates the stream and consumer group in Redis if they do not exist.
    """
    try:
        await redis.xgroup_create(
            stream_key, consumer_group, last_id_delivered, auto_create
        )
    except Exception as e:
        if "BUSYGROUP" in str(e):
            print(f"Grupo '{consumer_group}' ya existe en el stream '{stream_key}'.")
        else:
            raise

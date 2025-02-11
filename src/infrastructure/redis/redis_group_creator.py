import logging
from typing import Union

from redis.exceptions import ResponseError

from domain.publisher_enums import RedisStreams
from infrastructure.redis.redis_initialization import get_redis_client


async def create_consumer_group(
    stream_key: RedisStreams = RedisStreams.NOTIFICATIONS,
    consumer_group: RedisStreams = RedisStreams.NOTIFICATIONS_GROUP,
    last_id_delivered: Union[int, bytes, str, memoryview] = "$",
    auto_create: bool = True,
):
    try:
        redis = get_redis_client()
        await redis.xgroup_create(
            stream_key, consumer_group, last_id_delivered, auto_create
        )
    except ResponseError as e:
        if "BUSYGROUP" in str(e):
            logging.info(
                "Group '%s' already exists in the stream '%s'.",
                consumer_group,
                stream_key,
            )
        else:
            logging.error(
                "Error creating group '%s' for stream '%s}': %s",
                consumer_group,
                stream_key,
                e,
            )
            raise

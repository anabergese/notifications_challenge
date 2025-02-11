import logging

from redis.exceptions import ResponseError

from application.messagebus import MessageBus
from domain.publisher_enums import RedisStreams
from infrastructure.redis.redis_initialization import get_redis_client

from .process_notification import map_to_message_bus


async def start_redis_consumer(
    message_bus: MessageBus,
    stream_key: RedisStreams = RedisStreams.NOTIFICATIONS,
    group: RedisStreams = RedisStreams.NOTIFICATIONS_GROUP,
    consumer: RedisStreams = RedisStreams.NOTIFICATIONS_CONSUMER,
    count: int = 1,
    block: int = 5000,
    redis_client=None,
):
    logging.info("Starting Redis Consumer on stream: %s", stream_key)

    if redis_client is None:
        redis_client = get_redis_client()

    last_id = ">"

    while True:
        try:
            notifications = await redis_client.xreadgroup(
                group,
                consumer,
                {stream_key: last_id},
                count=count,
                block=block,
            )
            if notifications:
                await map_to_message_bus(
                    redis_client, message_bus, stream_key, group, notifications
                )
            else:
                logging.info("No new notifications in stream: %s", stream_key)
        except ResponseError as e:
            logging.error(
                "Error reading from Redis stream '%s' with group '%s' and consumer '%s', details: %s",
                stream_key.value,
                group.value,
                consumer.value,
                str(e),
            )
            raise

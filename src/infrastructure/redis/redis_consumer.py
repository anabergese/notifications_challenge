import logging

import redis
from redis.exceptions import RedisError

from application.messagebus import MessageBus
from domain.events import NotificationReceived
from domain.publisher_enums import RedisStreams
from infrastructure.redis.redis_initialization import get_redis_client


async def start_redis_consumer(
    message_bus: MessageBus,
    stream_key: RedisStreams = RedisStreams.NOTIFICATIONS,
    group: RedisStreams = RedisStreams.NOTIFICATIONS_GROUP,
    consumer: RedisStreams = RedisStreams.NOTIFICATIONS_CONSUMER,
):
    logging.info("Starting Redis Consumer on stream: %s", stream_key)
    redis = get_redis_client()
    from_id, count, block = ">", 10, 5000

    while True:
        try:
            messages = await redis.xreadgroup(
                group,
                consumer,
                {stream_key: from_id},
                count=count,
                block=block,
            )
            if messages:
                for stream, entries in messages:
                    for message_id, message_data in entries:
                        event = NotificationReceived(
                            topic=message_data["topic"],
                            description=message_data["description"],
                            version=message_data.get("version", "1.0"),
                        )
                        await message_bus.handle(event)
                        await redis.xack(stream_key.value, group.value, message_id)
            else:
                logging.info("No new messages in stream: %s", stream_key)
        except (RedisError, TypeError) as e:
            logging.error(
                "Error reading from Redis stream '%s' with group '%s' and consumer '%s': %s",
                stream_key.value,
                group.value,
                consumer.value,
                str(e),
            )

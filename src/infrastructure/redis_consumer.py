import logging

from domain.enums import RedisStreams
from domain.events import NotificationReceived
from infrastructure.redis.redis_initialization import get_redis_client
from application.messagebus import MessageBus


async def start_redis_consumer(
    stream_key: RedisStreams,
    group: RedisStreams,
    consumer: RedisStreams,
    message_bus: MessageBus,
):
    logging.info("Starting Redis Consumer on stream: %s", stream_key)
    redis_client = get_redis_client()
    from_id, count, block = ">", 10, 5000

    while True:
        try:
            messages = await redis_client.xreadgroup(
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
                        # await redis_client.xack(
                        #     stream_key.value, group.value, message_id
                        # )
            else:
                logging.info("No new messages in stream: %s", stream_key)
        except Exception as e:
            logging.error(
                "Error reading from Redis stream '%s' with group '%s' and consumer '%s': %s",
                stream_key.value,
                group.value,
                consumer.value,
                str(e),
            )

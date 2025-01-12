import logging

from config import get_redis_client
from domain.enums import RedisStreams
from workers.orchestrator import NotificationOrchestrator


async def start_redis_consumer(
    stream_key: RedisStreams,
    group: RedisStreams,
    consumer: RedisStreams,
    orchestrator: NotificationOrchestrator,
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
                        await orchestrator.process_message(message_data)
                        await redis_client.xack(stream_key, group, message_id)
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

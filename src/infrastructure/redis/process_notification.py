import logging
from typing import Any

from application.messagebus import MessageBus
from domain.events import NotificationReceived
from domain.publisher_enums import RedisStreams


async def map_to_message_bus(
    redis_client: Any,
    message_bus: MessageBus,
    stream_key: RedisStreams,
    group: RedisStreams,
    notifications: list,
):
    for stream, entries in notifications:
        for message_id, message_data in entries:
            try:
                event = NotificationReceived(
                    topic=message_data["topic"],
                    description=message_data["description"],
                    version=message_data.get("version", "1.0"),
                )
                await message_bus.handle(event)
                await redis_client.xack(stream_key.value, group.value, message_id)
            except Exception as e:
                logging.error(str(e))
                raise

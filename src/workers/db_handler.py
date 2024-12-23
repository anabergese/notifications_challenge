import asyncio
import json
import logging

from domain.enums import RedisChannels
from domain.events import NotificationCreated  # Asegúrate de importar la clase
from seedwork.application import redis_consumer, redis_publisher


async def db_handler() -> None:
    psub = await redis_consumer.subscribe_channel(RedisChannels.DB_SERVICE)
    async for message in psub.listen():
        if message["type"] == "message":
            data = message["data"]
            logging.info("Tipo de dato recibido: %s", type(data))
            logging.info("Data received: %s", data)

            try:
                data_dict = json.loads(data)
                logging.info("Deserialized data: %s", data)

                event = NotificationCreated(**data_dict)
                logging.info("Reconstructed event: %s", event)

                await redis_publisher.publish(
                    RedisChannels.NOTIFICATION_SERVICES, event
                )

            except json.JSONDecodeError as e:
                logging.error("Failed to decode JSON: %s", e)
            except TypeError as e:
                logging.error("Failed to reconstruct event: %s", e)

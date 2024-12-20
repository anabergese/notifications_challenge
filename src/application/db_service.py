import asyncio
import logging

from config import get_redis_client
from domain.enums import RedisChannels

redis_client = get_redis_client()


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel)
    return pubsub


async def db_service():
    psub = await psubscribe(RedisChannels.DB_SERVICE)
    async for message in psub.listen():  # Usa el listener asíncrono
        if message["type"] == "message":  # Filtrar solo mensajes
            data = message["data"]
            logging.info("Event received: %s", data)

            # Aquí procesar el mensaje en la base de datos
            # Por ejemplo:
            # await save_to_db(data)

            # Re-publicar el mensaje a NOTIFICATION_SERVICES
            await redis_client.publish(RedisChannels.NOTIFICATION_SERVICES, data)

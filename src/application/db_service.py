import asyncio
import json
import logging

from domain.enums import RedisChannels
from seedwork.application import redis_consumer, redis_publisher


async def db_service():
    psub = await redis_consumer.subscribe_channel(RedisChannels.DB_SERVICE)
    async for message in psub.listen():  # Usa el listener asíncrono
        if message["type"] == "message":  # Filtrar solo mensajes
            data = message["data"]
            if isinstance(data, bytes):
                data = data.decode("utf-8")  # Convertir a cadena

            # Deserializar JSON a un diccionario
            data_dict = json.loads(data)

            logging.info("Event received: %s", data_dict)
            # Aquí procesar el mensaje en la base de datos
            # Por ejemplo:
            # await save_to_db(data)

            # Re-publicar el mensaje a NOTIFICATION_SERVICES
            await redis_publisher.publish(
                RedisChannels.NOTIFICATION_SERVICES, data_dict
            )

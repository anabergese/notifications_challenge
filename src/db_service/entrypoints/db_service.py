import asyncio

from domain.enums import RedisChannels
from infrastructure.redis_client import get_redis_client

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
            print(f"Mensaje recibido por DB_SERVICE: {data}")

            # Aquí procesar el mensaje en la base de datos
            # Por ejemplo:
            # await save_to_db(data)

            # Re-publicar el mensaje a NOTIFICATION_SERVICES
            await redis_client.publish(RedisChannels.NOTIFICATION_SERVICES, data)

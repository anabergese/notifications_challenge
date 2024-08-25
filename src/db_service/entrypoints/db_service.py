import asyncio

from config import get_redis_client
from domain.enums import RedisChannels

redis_client = get_redis_client()


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


async def db_service():
    psub = await psubscribe(RedisChannels.DB_SERVICE)
    while True:
        message = psub.get_message(ignore_subscribe_messages=True)
        await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
        if message:
            # Imprime el contenido del mensaje
            print(f"Mensaje recibido: {message['data']}")
            # Falta crear new row en DB aquí
            # Antes o despues de crear la new row en DB necesito pasar a class Notification?
            redis_client.publish(RedisChannels.NOTIFICATION_SERVICES, message["data"])

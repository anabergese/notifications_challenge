import asyncio

from config import get_redis_client

redis_client = get_redis_client()


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


async def db_service():
    psub = await psubscribe("db_service")
    while True:
        message = psub.get_message(ignore_subscribe_messages=True)
        await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
        if message:
            # Imprime el contenido del mensaje
            print(f"Mensaje recibido: {message['data']}")

            redis_client.publish("notification_services", message["data"])

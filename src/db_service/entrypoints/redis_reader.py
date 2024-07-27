# file to delete
import asyncio
import os

import redis

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
)


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


async def reader():
    psub = await psubscribe("db_service")
    while True:
        message = psub.get_message(ignore_subscribe_messages=True)
        await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
        if message:
            # Imprime el contenido del mensaje
            print(f"Mensaje recibido: {message['data']}")

            redis_client.publish("notifications_service", message["data"])


if __name__ == "__main__":
    asyncio.run(reader())

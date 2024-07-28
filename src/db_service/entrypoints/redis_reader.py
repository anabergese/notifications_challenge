# file to delete
import asyncio
import os

import redis


def get_redis_client():
    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = int(os.getenv("REDIS_PORT", 6379))
    return redis.Redis(host=redis_host, port=redis_port, db=0)


redis_client = get_redis_client()


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

import asyncio
import os

import aioredis

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
psub = redis.pubsub()
pub = aioredis.Redis.from_url(
    f"redis://{REDIS_HOST}:{REDIS_PORT}", decode_responses=True
)


async def reader():
    async with psub as p:
        await p.subscribe("db_channel")
        while True:
            message = await p.get_message(ignore_subscribe_messages=True)
            await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
            if message:
                # Imprime el contenido del mensaje
                print(f"Mensaje recibido: {message['data']}")


if __name__ == "__main__":
    asyncio.run(reader())

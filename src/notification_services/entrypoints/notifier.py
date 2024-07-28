import asyncio

from config import get_redis_client

redis_client = get_redis_client()


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


async def notification_services(channel):
    psub = await psubscribe(channel)
    while True:
        message = psub.get_message(ignore_subscribe_messages=True)
        await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
        if message:
            print(f"notificación enviada a slack: {message['data']}")

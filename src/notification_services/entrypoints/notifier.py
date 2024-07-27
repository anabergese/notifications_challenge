import asyncio

from config import get_redis_client


class Notifier:
    def __init__(self):
        self.redis_client = get_redis_client()

    async def psubscribe(self, channel):
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        return pubsub

    async def connect_service(self, channel):
        psub = await self.psubscribe(channel)
        while True:
            message = psub.get_message(ignore_subscribe_messages=True)
            await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
            if message:
                print(f"Mensaje recibido y sent to slack/emal: {message['data']}")

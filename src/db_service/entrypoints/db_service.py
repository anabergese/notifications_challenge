import asyncio

from config import get_redis_client


class DBService:
    def __init__(self):
        self.redis_client = get_redis_client()

    async def psubscribe(self, channel):
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        return pubsub

    async def save_message(self, input_channel, output_channel):
        psub = await self.psubscribe(input_channel)
        while True:
            message = psub.get_message(ignore_subscribe_messages=True)
            await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
            if message:
                print(f"Mensaje recibido: {message['data']}")

                self.redis_client.publish(output_channel, message["data"])

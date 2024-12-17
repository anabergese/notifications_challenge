from config import get_redis_client
from domain import enums

redis_client = get_redis_client()


async def subscribe_channel(channel: enums.RedisChannels):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel)
    return pubsub

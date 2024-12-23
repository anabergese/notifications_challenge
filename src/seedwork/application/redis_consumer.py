from config import get_redis_client
from domain import enums

r = get_redis_client()


async def subscribe_channel(channel: enums.RedisChannels):  # type: ignore
    pubsub = r.pubsub()
    await pubsub.subscribe(channel)
    return pubsub

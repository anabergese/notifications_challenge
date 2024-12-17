from config import get_redis_client

redis_client = get_redis_client()


async def subscribe_channel(channel):
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel)
    return pubsub

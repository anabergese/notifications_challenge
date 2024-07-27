from .redis_config import add_message_to_redis_channel, start_redis


async def get_redis_connection():
    return await start_redis()


async def get_publish_to_channel():
    return add_message_to_redis_channel

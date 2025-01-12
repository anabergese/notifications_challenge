from config import get_redis_client
from domain.enums import RedisStreams

redis = get_redis_client()


async def initialize_redis_stream(
    stream_key: RedisStreams.NOTIFICATIONS,
    consumer_group: RedisStreams.NOTIFICATIONS_GROUP,
):
    """
    Creates the stream and consumer group in Redis if they do not exist.

    Arguments:
        stream_key: stream name.
        consumer_group: consumer group name.
    """
    try:
        # Crear el grupo de consumidores si no existe
        await redis.xgroup_create(stream_key, consumer_group, mkstream=True)
    except Exception as e:
        if "BUSYGROUP" in str(e):
            print(f"Grupo '{consumer_group}' ya existe en el stream '{stream_key}'.")
        else:
            raise

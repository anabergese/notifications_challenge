from config import get_redis_client
from domain import enums

redis = get_redis_client()


async def initialize_redis_stream(
    stream_key: enums.RedisStreams.NOTIFICATIONS,
    consumer_group: enums.RedisStreams.NOTIFICATIONS.NOTIFICATIONS_GROUP,
):
    """
    Crea el Stream y el Grupo de Consumidores en Redis si no existen.

    Args:
        stream_key: Nombre del stream.
        consumer_group: Nombre del grupo de consumidores.
    """
    try:
        # Crear el grupo de consumidores si no existe
        await redis.xgroup_create(stream_key, consumer_group, mkstream=True)
    except Exception as e:
        if "BUSYGROUP" in str(e):
            print(f"Grupo '{consumer_group}' ya existe en el stream '{stream_key}'.")
        else:
            raise

import asyncio

from config import setup_logging
from domain.enums import RedisStreams
from entrypoints.bootstrap import bootstrap
from infrastructure.redis_consumer import start_redis_consumer

setup_logging()


async def main() -> None:
    message_bus = await bootstrap()

    await start_redis_consumer(
        stream_key=RedisStreams.NOTIFICATIONS,
        group=RedisStreams.NOTIFICATIONS_GROUP,
        consumer=RedisStreams.NOTIFICATIONS_CONSUMER,
        message_bus=message_bus,
    )


if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from entrypoints.bootstrap import bootstrap
from entrypoints.config import setup_logging
from infrastructure.redis.redis_consumer import start_redis_consumer


async def main() -> None:
    setup_logging()
    message_bus = await bootstrap()
    await start_redis_consumer(message_bus=message_bus)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from entrypoints.bootstrap import bootstrap
from entrypoints.config import setup_logging
from entrypoints.dependencies import (
    get_notifiers_mapping,
    get_orchestrator,
    get_publisher,
)
from infrastructure.redis.redis_consumer import start_redis_consumer


async def main() -> None:
    setup_logging()
    publisher = get_publisher()
    orchestrator = get_orchestrator(get_notifiers_mapping())
    message_bus = await bootstrap(publish=publisher, orchestrator=orchestrator)
    await start_redis_consumer(message_bus=message_bus)


if __name__ == "__main__":
    asyncio.run(main())

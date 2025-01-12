import asyncio

from notification_channels import EmailNotifier, SlackNotifier
from orchestrator import NotificationOrchestrator

from config import setup_logging
from domain.enums import RedisStreams, Topic
from seedwork.application.redis_consumer import start_redis_consumer

setup_logging()

notifiers_mapping = {
    Topic.SALES: SlackNotifier(),
    Topic.PRICING: EmailNotifier(),
}

# Diccionario de estrategias con funciones (sin ejecutarlas)
consumer_strategies = {
    "redis": lambda orchestrator: start_redis_consumer(
        stream_key=RedisStreams.NOTIFICATIONS,
        group=RedisStreams.NOTIFICATIONS_GROUP,
        consumer=RedisStreams.NOTIFICATIONS_CONSUMER,
        orchestrator=orchestrator,
    ),
}


async def main() -> None:
    orchestrator = NotificationOrchestrator(notifiers_mapping)
    consumer = consumer_strategies.get("redis")
    await consumer(orchestrator)


if __name__ == "__main__":
    asyncio.run(main())

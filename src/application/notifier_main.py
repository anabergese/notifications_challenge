import asyncio

from notifier import notification_services

from domain.enums import RedisChannels
from logging_config import setup_logging

setup_logging()

if __name__ == "__main__":
    asyncio.run(notification_services(RedisChannels.NOTIFICATION_SERVICES))

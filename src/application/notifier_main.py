import asyncio

from notifier import notification_services

from config import setup_logging
from domain.enums import RedisChannels

setup_logging()

if __name__ == "__main__":
    asyncio.run(notification_services(RedisChannels.NOTIFICATION_SERVICES))

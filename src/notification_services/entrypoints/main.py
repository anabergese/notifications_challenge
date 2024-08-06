import asyncio

from domain.enums import RedisChannels
from notifier import notification_services

if __name__ == "__main__":
    asyncio.run(notification_services(RedisChannels.NOTIFICATION_SERVICES))

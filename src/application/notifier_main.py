import asyncio

from notifier import notification_services

from domain.enums import RedisChannels

if __name__ == "__main__":
    asyncio.run(notification_services(RedisChannels.NOTIFICATION_SERVICES))

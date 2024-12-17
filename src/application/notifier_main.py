import asyncio

from notifier import notification_services

from config import setup_logging

setup_logging()

if __name__ == "__main__":
    asyncio.run(notification_services())

import asyncio

from notifier import Notifier


async def main():
    notification_services = Notifier()
    await notification_services.connect_service("notification_services")


if __name__ == "__main__":
    asyncio.run(main())

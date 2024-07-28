import asyncio

from notifier import notification_services


async def main():
    await notification_services("notification_services")


if __name__ == "__main__":
    asyncio.run(main())

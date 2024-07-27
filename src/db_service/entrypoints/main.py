import asyncio

from db_service import DBService


async def main():
    db_service = DBService()
    await db_service.save_message("db_service", "notification_services")


if __name__ == "__main__":
    asyncio.run(main())

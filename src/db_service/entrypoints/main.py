# file to delete
import asyncio

from db_service import db_service


async def main():
    await db_service()


if __name__ == "__main__":
    asyncio.run(main())

import asyncio

from entrypoints.db_service import db_service

if __name__ == "__main__":
    asyncio.run(db_service())

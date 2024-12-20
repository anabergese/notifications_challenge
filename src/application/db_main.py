import asyncio

from db_service import db_service

from config import setup_logging

setup_logging()

if __name__ == "__main__":
    asyncio.run(db_service())

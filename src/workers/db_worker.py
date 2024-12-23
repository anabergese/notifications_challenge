import asyncio

from db_handler import db_handler

from config import setup_logging

setup_logging()

if __name__ == "__main__":
    asyncio.run(db_handler())

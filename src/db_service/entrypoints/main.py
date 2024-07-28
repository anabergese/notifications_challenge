# file to delete
import asyncio

from redis_reader import reader

if __name__ == "__main__":
    asyncio.run(reader())

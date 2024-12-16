import asyncio
import logging

from config import get_redis_client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_redis_connection():
    try:
        redis_client = get_redis_client()
        logger.info("Connecting to Redis...")
        redis_client.pingsssss()  # Pingssss no es un valid metodo, el test deberia fallar
        logger.info("Successfully connected to Redis!")
    except Exception as e:
        logger.error("Error connecting to Redis: %s", e)
    finally:
        redis_client.close()
        redis_client.connection_pool.disconnect()

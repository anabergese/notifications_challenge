import logging
import os

# from entrypoints.config import Config
import redis
from domain.models import Message
from fastapi import HTTPException
from redis import Redis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_redis_connection():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=0,
    )


def add_message_to_redis_queue(message: Message, redis_conn):
    try:
        message_json = message.model_dump_json()
        redis_conn.lpush("task_queue", message_json)
        logger.info("Message added to queue: %s", message_json)
    except Exception as e:
        logger.error("Failed to add message to queue: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


def get_add_message_to_redis_queue():
    return add_message_to_redis_queue

import json
import logging

import redis
from config import get_redis_host_and_port

logger = logging.getLogger(__name__)

r = redis.Redis(**get_redis_host_and_port())


def publish(channel: str, event: dict):
    logging.info("Log from redis_publisher.py: channel=%s, event=%s", channel, event)
    r.publish(channel, json.dumps((event)))

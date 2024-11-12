import json
import logging
from dataclasses import asdict

import redis
from config import config
from domain.events import Event

logger = logging.getLogger(__name__)

r = redis.Redis(**config.get_redis_host_and_port())


def publish(channel: str, event: Event):
    logging.info("publishing: channel=%s, event=%s", channel, event)
    r.publish(channel, json.dumps(asdict(event)))

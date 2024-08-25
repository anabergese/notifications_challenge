import json

from domain.enums import RedisChannels

from .channels import NotificationChannel


class RedisNotificationChannel(NotificationChannel):
    def __init__(self, redis_client):
        self.redis_client = redis_client

    async def publish(self, message):
        self.redis_client.publish(
            RedisChannels.DB_SERVICE.value, json.dumps(message.dict())
        )

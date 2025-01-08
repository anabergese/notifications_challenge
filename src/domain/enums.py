from enum import Enum


class Topic(str, Enum):
    SALES = "sales"
    PRICING = "pricing"


class RedisStreams(str, Enum):
    NOTIFICATIONS = "notifications"
    NOTIFICATIONS_GROUP = "notifications_group"
    NOTIFICATIONS_CONSUMER = "notifications_consumer"

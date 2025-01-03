from enum import Enum


class Topic(str, Enum):
    SALES = "sales"
    PRICING = "pricing"


class RedisChannels(str, Enum):
    DB_SERVICE = "db_service"
    NOTIFICATION_SERVICES = "notification_services"

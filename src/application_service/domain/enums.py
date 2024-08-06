from enum import Enum


class Topic(str, Enum):
    SALES = "sales"
    PRICING = "pricing"


class RedisChannels(Enum):
    DB_SERVICE = "db_service"
    NOTIFICATION_SERVICES = "notification_services"

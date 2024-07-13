import redis

class Config:
    REDIS_HOST = 'redis'
    REDIS_PORT = 6379
    REDIS_DB = 0

def get_redis_connection():
    return redis.Redis(
        host=Config.REDIS_HOST,
        port=Config.REDIS_PORT,
        db=Config.REDIS_DB
    )

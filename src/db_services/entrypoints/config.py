import os
import redis
from redis import Redis

def create_redis_connection():
    return redis.Redis(
        host=os.getenv('REDIS_HOST', 'localhost'), 
        port=int(os.getenv('REDIS_PORT', 6379)), 
        db=0
    )
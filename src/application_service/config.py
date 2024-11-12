import os


def get_redis_host_and_port():
    host = os.environ.get("REDIS_HOST", "localhost")
    port = 6379 if host == "localhost" else 6379
    return dict(host=host, port=port)


# import os

# import redis


# def get_redis_client():
#     redis_host = os.getenv("REDIS_HOST", "localhost")
#     redis_port = int(os.getenv("REDIS_PORT", "6379"))
#     return redis.Redis(host=redis_host, port=redis_port, db=0)

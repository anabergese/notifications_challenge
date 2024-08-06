from fastapi import HTTPException, Request

from .redis import publish_to_redis, start_redis


async def get_channel_connection():
    return await start_redis()


async def get_publish_to_channel():
    return publish_to_redis


async def get_channel(request: Request):
    if not hasattr(request.app.state, "channel"):
        raise HTTPException(
            status_code=500, detail="Channel connection is not available."
        )
    return request.app.state.channel

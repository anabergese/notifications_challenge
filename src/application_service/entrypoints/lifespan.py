# lifespan.py
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .redis import (
    start_redis,  # Import the function that initializes the Redis connection
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Initialize the Redis connection at startup
        channel = await start_redis()
        app.state.channel = channel
        yield
    except Exception as exc:
        logger.error("Error establishing channel connection: %s", exc)
        raise RuntimeError("Failed to establish channel connection.") from exc
    finally:
        # Properly close the Redis connection on shutdown
        if hasattr(app.state, "channel"):
            app.state.channel.close()

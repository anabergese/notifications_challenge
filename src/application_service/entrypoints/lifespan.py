import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .dependencies import get_channel_connection

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        channel = await get_channel_connection()
        app.state.channel = channel
        yield
    except Exception as exc:
        logger.error("Error establishing channel connection: %s", exc)
        raise RuntimeError("Failed to establish channel connection.") from exc
    finally:
        if hasattr(app.state, "channel"):
            await app.state.channel.close()

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from config import setup_logging
from domain.enums import RedisStreams
from seedwork.application import stream_initialization

from .bootstrap import bootstrap
from .exception_handlers.handlers import add_error_handlers
from .routes.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Initializing Streams...")
    await stream_initialization.initialize_redis_stream(
        RedisStreams.NOTIFICATIONS,
        RedisStreams.NOTIFICATIONS_GROUP,
    )
    print("Streams initialized successfully.")
    yield


app = FastAPI(
    title="Notification System",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
    tags=["Notification System"],
    lifespan=lifespan,
)

setup_logging()

message_bus = bootstrap()

add_error_handlers(app)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

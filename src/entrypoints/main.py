import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from infrastructure.redis.redis_group_creator import initialize_redis_stream

from .config import setup_logging
from .exception_handlers.handlers import add_error_handlers
from .routes.routes import router


@asynccontextmanager
async def lifespan(_: FastAPI):
    logging.info("Initializing FastAPI.")
    await initialize_redis_stream()
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

add_error_handlers(app)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

import logging

import uvicorn
from fastapi import FastAPI

from domain.events import NotificationCreated
from logging_config import setup_logging
from service_layer.handlers import handle_notification_created
from service_layer.messagebus import register_handler

from .routes.routes import router

app = FastAPI(
    title="Notification System",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
    tags=["Notification System"],
)

setup_logging()

# Registrar handlers en el MessageBus
register_handler(NotificationCreated, handle_notification_created)


app.include_router(router)

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=80)
    except RuntimeError as runtime_error:
        logging.critical("Application startup failed: %s", runtime_error)

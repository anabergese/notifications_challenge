import logging

import uvicorn
from domain.events import NotificationCreated
from entrypoints.routes.routes import router
from fastapi import FastAPI
from service_layer.handlers import handle_notification_created
from service_layer.messagebus import register_handler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Notification System",
    description="API for handling customer requests and sending notifications to various channels.",
    version="1.0.0",
    tags=["Notification System"],
)

# Registrar handlers en el MessageBus
register_handler(NotificationCreated, handle_notification_created)


app.include_router(router)

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0", port=80)
    except RuntimeError as runtime_error:
        logger.critical("Application startup failed: %s", runtime_error)

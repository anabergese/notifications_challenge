import logging
from contextlib import asynccontextmanager
from datetime import datetime

from bootstrap import bootstrap
from domain.system_events import ServiceConnectionEstablished
from fastapi import FastAPI

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Inicializar el MessageBus en el startup
        message_bus = bootstrap()
        app.state.message_bus = message_bus

        # Publicar el evento ServiceConnectionEstablished
        event = ServiceConnectionEstablished(
            timestamp=datetime.now(), service_name="NotificationSystem"
        )
        message_bus.publish(event)

        yield

    except Exception as exc:
        logger.error("Error during application startup: %s", exc)
        raise RuntimeError("Application startup failed.") from exc
    finally:
        # Realizar acciones de limpieza si es necesario
        if hasattr(app.state, "message_bus"):
            # Puedes realizar acciones de cierre o limpieza aquí si es necesario
            pass

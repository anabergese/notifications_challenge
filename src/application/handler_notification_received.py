import asyncio
import logging

from domain.events import NotificationReceived
from workers.orchestrator import NotificationOrchestrator


async def handle_notification_received(
    event: NotificationReceived, orchestrator: NotificationOrchestrator
):
    logging.info("Tipo de dato recibido por handler not received: %s", type(event))
    message_data = {
        "topic": event.topic,
        "description": event.description,
        "version": event.version,
    }
    await orchestrator.process_message(message_data)

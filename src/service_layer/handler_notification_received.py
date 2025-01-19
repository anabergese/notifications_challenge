import asyncio

from domain.events import NotificationReceived
from workers.orchestrator import NotificationOrchestrator


async def handle_notification_received(
    event: NotificationReceived, orchestrator: NotificationOrchestrator
):
    message_data = {
        "topic": event.topic.value,
        "description": event.description,
        "version": event.version,
    }
    await orchestrator.process_message(message_data)

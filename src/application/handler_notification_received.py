from domain.events import NotificationReceived
from workers.orchestrator import NotificationOrchestrator


async def handle_notification_received(
    event: NotificationReceived, orchestrator: NotificationOrchestrator
):
    await orchestrator.process_message(event)

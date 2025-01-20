import logging

from domain.events import NotificationReceived

from .notification_channels import Notifier


class NotificationOrchestrator:
    def __init__(
        self,
        notifiers: dict[str, Notifier],
    ):
        self.notifiers = notifiers

    async def process_message(self, event: NotificationReceived):
        try:
            logging.info("Received: %s, and data type: %s", event, type(event))
            topic = event.topic
            notifier = self.notifiers.get(topic)
            if notifier:
                logging.info("Processing notification for topic: %s", topic)
                await notifier.notify(event)
            else:
                logging.warning("No notifier found for topic: %s", topic)
        except Exception as e:
            logging.error("Error processing message: %s", str(e))

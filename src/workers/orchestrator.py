import json
import logging

from notification_channels import Notifier


class NotificationOrchestrator:
    def __init__(
        self,
        notifiers: dict[str, Notifier],
    ):
        self.notifiers = notifiers

    async def process_message(self, message_data):
        try:
            logging.info("Tipo de dato recibido por stream: %s", type(message_data))
            logging.info("El dato recibido por stream: %s", message_data)
            topic = message_data.get("topic", "")
            notifier = self.notifiers.get(topic)
            if notifier:
                logging.info("Processing notification for topic: %s", topic)
                await notifier.notify(json.dumps(message_data))
            else:
                logging.warning("No notifier found for topic: %s", topic)
        except Exception as e:
            logging.error("Error processing message: %s", str(e))

import logging
from typing import List

from domain.events import NotificationReceived
from domain.topic_enums import Topic

from .notifiers.notifier import Notifier


class NotificationOrchestrator:
    """NotificationOrchestrator is responsible for orchestrating the notification process.
    It receives notifications and delegates the processing to the appropriate notifiers.
    Attributes:
        notifiers (dict[Topic, List[Notifier]]): A mapping of topics to their respective notifiers.
    Methods:
        process_message(event: NotificationReceived):
            Processes the received notification event and notifies the appropriate notifiers.
    Raises:
        Exception: If an error occurs during the notification process.
    """

    def __init__(
        self,
        notifiers: dict[Topic, List[Notifier]],
    ):
        self.notifiers = notifiers

    async def process_message(self, event: NotificationReceived):
        try:
            logging.info("Received: %s, and data type: %s", event, type(event))
            topic = event.topic
            notifiers = self.notifiers.get(topic, [])
            if notifiers:
                logging.info("Processing notification for topic: %s", topic)
                for notifier in notifiers:
                    await notifier.notify(event)
            else:
                logging.warning("No notifier found for topic: %s", topic)
        except Exception as e:
            logging.error("Error processing message: %s", str(e))
            raise

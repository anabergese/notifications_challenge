import json
import logging

from notification_channels import Notifier

from config import get_redis_client
from domain import enums


class NotificationOrchestrator:
    def __init__(
        self,
        notifiers: dict[str, Notifier],
        stream_key: enums.RedisStreams.NOTIFICATIONS,
        group: enums.RedisStreams.NOTIFICATIONS.NOTIFICATIONS_GROUP,
        consumer_name: enums.RedisStreams.NOTIFICATIONS.NOTIFICATIONS_CONSUMER,
    ):
        self.notifiers = notifiers
        self.stream_key = stream_key
        self.group = group
        self.consumer_name = consumer_name
        self.redis = get_redis_client()

    async def start(self) -> None:
        """
        Empieza a leer mensajes del Redis Stream como parte de un grupo de consumidores.
        """
        logging.info(
            "Starting Notification Orchestrator on stream: %s", self.stream_key
        )

        from_id = ">"  # Leer nuevos mensajes
        count = 10  # Leer hasta 10 mensajes por iteración
        block = 5000  # Bloquea por hasta 5 segundos esperando mensajes

        while True:
            try:
                # Leer mensajes del grupo
                messages = await self.redis.xreadgroup(
                    self.group,
                    self.consumer_name,
                    {self.stream_key: from_id},
                    count=count,
                    block=block,
                )
                if messages:
                    for stream, entries in messages:
                        for message_id, message_data in entries:
                            await self._process_message(message_data)
                            # Acknowledge the message
                            await self.redis.xack(
                                self.stream_key, self.group, message_id
                            )
                else:
                    logging.info("No new messages in stream: %s", self.stream_key)
            except Exception as e:
                logging.error("Error processing stream: %s", str(e))

    async def _process_message(self, message_data: dict[bytes, bytes]) -> None:
        """
        Procesa un mensaje del stream.
        """
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

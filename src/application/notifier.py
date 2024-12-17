import asyncio
import json
import logging

from notifiers import Notifier

from domain.enums import RedisChannels
from seedwork.application import redis_consumer


class NotificationService:
    def __init__(self, notifiers: dict[str, Notifier]):
        """
        Inicializa el servicio de notificaciones con un diccionario de notifiers.
        :param notifiers: Diccionario que mapea un tópico a una instancia de Notifier.
        """
        self.notifiers = notifiers

    async def start(self):
        """
        Inicia la escucha en el canal de Redis para manejar las notificaciones.
        """
        logging.info(
            "Subscribing to Redis channel: %s", RedisChannels.NOTIFICATION_SERVICES
        )
        psub = await redis_consumer.subscribe_channel(
            RedisChannels.NOTIFICATION_SERVICES
        )

        async for message in psub.listen():
            if message["type"] == "message":
                await self._process_message(message)

    async def _process_message(self, message):
        """
        Procesa un mensaje recibido del canal Redis.
        :param message: Mensaje en formato Redis.
        """
        try:
            data = json.loads(message["data"])  # Decodifica el mensaje
            topic = data.get("topic")

            # Recupera el notifier adecuado según el tópico
            notifier = self.notifiers.get(topic)
            if notifier:
                logging.info("Processing notification for topic: %s", topic)
                await notifier.notify(json.dumps(data))
            else:
                logging.warning("No notifier found for topic: %s", topic)
        except (json.JSONDecodeError, KeyError) as e:
            logging.error("Error processing message: %s", str(e))

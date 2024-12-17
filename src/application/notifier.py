import asyncio
import json
import logging

from notifiers import EmailNotifier, SlackNotifier

from domain.enums import RedisChannels, Topic
from seedwork.application import redis_consumer

email_notifier = EmailNotifier()
slack_notifier = SlackNotifier()


async def notification_services():
    psub = await redis_consumer.subscribe_channel(RedisChannels.NOTIFICATION_SERVICES)

    async for message in psub.listen():  # Use async for to handle messages
        if message["type"] == "message":  # Filter only "message" events
            data = json.loads(message["data"])  # Decode the message
            topic = data.get("topic")
            if topic == Topic.SALES:
                await slack_notifier.notify(json.dumps(data))  # Ensure notify is async
            elif topic == Topic.PRICING:
                await email_notifier.notify(json.dumps(data))  # Ensure notify is async
            else:
                logging.info("Unknown topic: %s, type: %s", topic, type(topic))

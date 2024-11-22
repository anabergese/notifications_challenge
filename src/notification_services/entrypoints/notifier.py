import asyncio
import json

from config import get_redis_client
from domain.enums import Topic
from domain.notifiers import EmailNotifier, SlackNotifier

redis_client = get_redis_client()

email_notifier = EmailNotifier()
slack_notifier = SlackNotifier()


async def psubscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


async def notification_services(channel):
    psub = await psubscribe(channel)
    while True:
        message = psub.get_message(ignore_subscribe_messages=True)
        await asyncio.sleep(0)  # Permite que otros eventos de asyncio se procesen
        if message:
            data = json.loads(message["data"])
            topic = data.get("topic")
            if topic == "Topic.SALES":
                slack_notifier.notify(message["data"])
            elif topic == "Topic.PRICING":
                email_notifier.notify(message["data"])
            else:
                print(f"Unknown topic: {topic}")

from .channels import NotificationChannel


class NotificationService:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    async def send_notification(self, notification):
        await self.channel.publish(notification)

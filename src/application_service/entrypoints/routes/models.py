from domain.enums import Topic
from domain.models import Notification
from pydantic import BaseModel, Field


class NotificationRequest(BaseModel):
    topic: Topic = Field(title="Topic", description="Topic of the message")
    description: str = Field(
        title="Description", description="Description of the message"
    )

    def create_notification(self) -> Notification:
        return Notification(topic=self.topic, description=self.description)

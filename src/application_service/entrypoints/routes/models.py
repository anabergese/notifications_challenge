from domain.enums import Topic
from pydantic import BaseModel, Field


class NotificationRequest(BaseModel):
    topic: Topic = Field(title="Topic", description="Topic of the message")
    description: str = Field(
        title="Description", description="Description of the message"
    )

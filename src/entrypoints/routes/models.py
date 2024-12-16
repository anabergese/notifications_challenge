from pydantic import BaseModel, Field

from domain.enums import Topic


class NotificationRequest(BaseModel):
    topic: Topic
    description: str = Field(min_length=10, max_length=200)

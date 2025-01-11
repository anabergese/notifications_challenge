from pydantic import BaseModel, Field

from domain.enums import Topic
from domain.events import NotificationCreated


class NotificationRequest(BaseModel):
    topic: Topic
    description: str = Field(min_length=10, max_length=200)

    def map_to(self) -> NotificationCreated:
        return NotificationCreated(topic=self.topic, description=self.description)


class NotificationCreatedResponse(BaseModel):
    message: str
    topic: str


class ErrorResponse(BaseModel):
    detail: str

from pydantic import BaseModel

from domain.enums import Topic


class NotificationRequest(BaseModel):
    topic: Topic
    description: str

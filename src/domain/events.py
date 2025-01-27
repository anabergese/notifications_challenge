from pydantic import Field
from pydantic.dataclasses import dataclass

from .topic_enums import Topic


@dataclass(frozen=True)
class Event:
    pass


@dataclass(frozen=True)
class DomainEvent(Event):
    topic: Topic
    description: str = Field(min_length=10, max_length=200)
    version: str = "1.0"


@dataclass(frozen=True)
class NotificationCreated(DomainEvent):
    pass


@dataclass(frozen=True)
class NotificationReceived(DomainEvent):
    pass

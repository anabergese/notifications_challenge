from dataclasses import dataclass
from datetime import datetime

from pydantic import Field
from pydantic.dataclasses import dataclass

from .enums import Topic


@dataclass(frozen=True)
class Event:
    timestamp: datetime


@dataclass(frozen=True)
class DomainEvent(Event):
    pass


@dataclass(frozen=True)
class NotificationCreated(DomainEvent):
    topic: Topic
    description: str = Field(min_length=10, max_length=200)
    version: str = "1.0"

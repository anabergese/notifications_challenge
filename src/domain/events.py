from dataclasses import dataclass
from datetime import datetime

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
    description: str
    version: str = "1.0"

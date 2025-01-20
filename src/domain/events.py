from pydantic import Field
from pydantic.dataclasses import dataclass

from .enums import Topic


@dataclass(frozen=True)
class Event:
    pass


@dataclass(frozen=True)
class DomainEvent(Event):
    pass


@dataclass(frozen=True)
class NotificationCreated(DomainEvent):
    topic: Topic
    description: str
    version: str = "1.0"


@dataclass(frozen=True)
class NotificationReceived(DomainEvent):
    topic: Topic
    description: str
    version: str = "1.0"

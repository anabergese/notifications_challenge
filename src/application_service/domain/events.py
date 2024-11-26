from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Event:
    timestamp: datetime


@dataclass(frozen=True)
class DomainEvent(Event):
    topic: str
    description: str
    version: str = "1.0"


@dataclass(frozen=True)
class NotificationCreated(DomainEvent):
    topic: str
    description: str

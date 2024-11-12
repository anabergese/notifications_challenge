from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional


@dataclass(frozen=True)
class Event:
    timestamp: datetime
    event_data: Any = None


class ServiceConnectionEstablished(Event):
    service_name: str


class ServiceStopped(Event):
    service_name: str


class ServiceConnectionFailed(Event):
    service_name: str


class NotificationFailed(Event):
    pass

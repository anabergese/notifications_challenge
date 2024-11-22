from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class Event:
    timestamp: datetime
    event_data: Any = None


@dataclass(frozen=True)
class DomainEvent:
    timestamp: datetime
    event_data: Any = None

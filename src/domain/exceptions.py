from abc import ABC
from dataclasses import dataclass, field


@dataclass(frozen=True)
class DomainError(Exception, ABC):
    message: str


@dataclass(frozen=True)
class NotificationSendError(DomainError):
    message: str = field(
        default="Notification could not be sent, retries had been applied"
    )

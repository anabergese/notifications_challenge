from abc import ABC, abstractmethod

from domain.events import DomainEvent


class Notifier(ABC):
    """This class defines the interface for sending notifications.
    Subclasses should implement the `notify` method to send notifications
    using different protocols (e.g., email, SMS, etc.).
    Attributes:
        event (DomainEvent): The event to be notified about.
    Methods:
        notify(event: DomainEvent) -> str:
            Sends a notification about the event.
            Returns a string indicating the result of the notification.
    Raises:
        NotImplementedError: If the `notify` method is not implemented in a subclass.
    """

    @abstractmethod
    async def notify(self, event: DomainEvent) -> str:
        raise NotImplementedError

from abc import ABC, abstractmethod

from domain.events import DomainEvent


class Notifier(ABC):
    @abstractmethod
    async def notify(self, event: DomainEvent) -> str:
        raise NotImplementedError

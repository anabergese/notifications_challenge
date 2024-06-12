from abc import ABC, abstractmethod

class NotifierPort(ABC):
    @abstractmethod
    def notify(self, description: str):
        pass
    @abstractmethod
    def validate_topic(self, topic: str) -> bool:
        pass
from abc import ABC, abstractmethod
from src.application_service.entrypoints.models import RequestModel
from src.application_service.domain.models import RequestEvent
class EventProvider(ABC):
    @abstractmethod
    def create_event(self, request: RequestModel) -> RequestEvent:
        pass

class BotEventProvider(EventProvider):
    def create_event(self, request: RequestModel) -> RequestEvent:
        return RequestEvent(
            topic=request.topic,
            description=request.description,
            source="CustomerBot",
            status="Received",
            id=1
        )
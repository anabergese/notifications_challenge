from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from src.application_service.entrypoints.models import RequestModel

class RequestEvent(BaseModel):
    id: int = Field(default=None)
    topic: str
    description: str
    source: str
    status: str

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
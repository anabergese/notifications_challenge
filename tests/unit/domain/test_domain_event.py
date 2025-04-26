import dataclasses

import pytest
from pydantic import ValidationError

from src.domain.events import DomainEvent, Event
from src.domain.topic_enums import Topic


class TestDomainEvent:
    def test_inherits_from_event_class(self, domain_event):
        assert isinstance(domain_event, Event)

    def test_created_with_valid_inputs(self, domain_event):
        assert domain_event.topic == Topic.PRICING
        assert domain_event.description == "I want to know how much cost AI chats."
        assert domain_event.version == "1.0"

    def test_is_immutable(self, domain_event):
        with pytest.raises(dataclasses.FrozenInstanceError):
            domain_event.topic = "Topic.MARKETING"
        with pytest.raises(dataclasses.FrozenInstanceError):
            domain_event.description = "New description"
        with pytest.raises(dataclasses.FrozenInstanceError):
            domain_event.version = "2.0"

    def test_raises_value_error_for_invalid_description(self, invalid_description):
        with pytest.raises(ValueError):
            DomainEvent(topic=Topic.SALES, description=invalid_description)

    def test_raises_pydantic_validation_error_for_invalid_topic(self, invalid_topic):
        with pytest.raises(ValidationError):
            DomainEvent(
                topic=invalid_topic,
                description="This is a valid description",
            )

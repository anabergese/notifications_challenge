import dataclasses

import pytest
from pydantic import ValidationError

from src.domain.events import DomainEvent, Event
from src.domain.topic_enums import Topic


class TestDomainEvent:
    def test_domain_event_inherits_from_event_class(self, domain_event):
        assert isinstance(domain_event, Event)

    def test_domain_event_created_with_valid_inputs(self, domain_event):
        assert domain_event.topic == Topic.SALES
        assert domain_event.description == "Valid description with proper length"
        assert domain_event.version == "1.0"

    def test_domain_event_is_immutable(self, domain_event):
        with pytest.raises(dataclasses.FrozenInstanceError):
            domain_event.topic = "Topic.MARKETING"
        with pytest.raises(dataclasses.FrozenInstanceError):
            domain_event.description = "New description"
        with pytest.raises(dataclasses.FrozenInstanceError):
            domain_event.version = "2.0"

    def test_domain_event_raises_value_error_for_too_short_description(self):
        with pytest.raises(ValueError):
            DomainEvent(topic=Topic.SALES, description="short")

    def test_domain_event_raises_value_error_for_too_long_description(self):
        with pytest.raises(ValueError):
            DomainEvent(topic=Topic.SALES, description="x" * 201)

    def test_domain_event_raises_pydantic_validation_error_for_invalid_topic(self):
        with pytest.raises(ValidationError):
            DomainEvent(
                topic="INEXISTENT TOPIC",
                description="Valid description with proper length",
            )

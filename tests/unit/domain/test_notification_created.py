import dataclasses

import pytest
from pydantic import ValidationError

from src.domain.events import DomainEvent, NotificationCreated
from src.domain.topic_enums import Topic


class TestNotificationCreated:
    def test_inherits_from_domain_event_class(self, notification_created):
        assert isinstance(notification_created, DomainEvent)

    def test_with_valid_inputs(self, notification_created):
        assert notification_created.topic == Topic.PRICING
        assert (
            notification_created.description == "I want to know how much cost AI chats."
        )
        assert notification_created.version == "1.0"

    def test_is_immutable(self, notification_created):
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_created.topic = "Topic.MARKETING"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_created.description = "New description"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_created.version = "2.0"

    def test_raises_value_error_for_invalid_description(self, invalid_description):
        with pytest.raises(ValueError):
            NotificationCreated(topic=Topic.SALES, description=invalid_description)

    def test_raises_pydantic_validation_error_for_invalid_topic(self, invalid_topic):
        with pytest.raises(ValidationError):
            NotificationCreated(
                topic=invalid_topic,
                description="Valid description with proper length",
            )

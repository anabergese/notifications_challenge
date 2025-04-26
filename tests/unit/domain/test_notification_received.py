import dataclasses

import pytest
from pydantic import ValidationError

from src.domain.events import DomainEvent, NotificationReceived
from src.domain.topic_enums import Topic


class TestNotificationReceived:
    def test_inherits_from_domain_event_class(self, notification_received):
        assert isinstance(notification_received, DomainEvent)

    def test_with_valid_inputs(self, notification_received):
        assert notification_received.topic == Topic.PRICING
        assert (
            notification_received.description
            == "I want to know how much cost AI chats."
        )
        assert notification_received.version == "1.0"

    def test_is_immutable(self, notification_received):
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_received.topic = "Topic.MARKETING"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_received.description = "New description"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_received.version = "2.0"

    def test_raises_value_error_for_invalid_description(self, invalid_description):
        with pytest.raises(ValueError):
            NotificationReceived(topic=Topic.SALES, description=invalid_description)

    def test_raises_pydantic_validation_error_for_invalid_topic(self, invalid_topic):
        with pytest.raises(ValidationError):
            NotificationReceived(
                topic=invalid_topic,
                description="Valid description with proper length",
            )

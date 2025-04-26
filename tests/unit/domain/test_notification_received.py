import dataclasses

import pytest
from pydantic import ValidationError

from src.domain.events import DomainEvent, NotificationReceived
from src.domain.topic_enums import Topic


class TestNotificationReceived:
    def test_notification_received_inherits_from_domain_event_class(
        self, notification_received
    ):
        assert isinstance(notification_received, DomainEvent)

    def test_notification_received_with_valid_inputs(self, notification_received):
        assert notification_received.topic == Topic.SALES
        assert (
            notification_received.description == "Valid description with proper length"
        )
        assert notification_received.version == "1.0"

    def test_notification_received_is_immutable(self, notification_received):
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_received.topic = "Topic.MARKETING"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_received.description = "New description"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_received.version = "2.0"

    def test_notification_created_raises_value_error_for_too_short_description(self):
        with pytest.raises(ValueError):
            NotificationReceived(topic=Topic.SALES, description="short")

    def test_notification_created_raises_value_error_for_too_long_description(self):
        with pytest.raises(ValueError):
            NotificationReceived(topic=Topic.SALES, description="x" * 201)

    def test_notification_created_raises_pydantic_validation_error_for_invalid_topic(
        self,
    ):
        with pytest.raises(ValidationError):
            NotificationReceived(
                topic="INEXISTENT TOPIC",
                description="Valid description with proper length",
            )

import dataclasses

import pytest
from pydantic import ValidationError

from src.domain.events import DomainEvent, NotificationCreated
from src.domain.topic_enums import Topic


class TestNotificationCreated:
    def test_notification_created_inherits_from_domain_event_class(
        self, notification_created
    ):
        assert isinstance(notification_created, DomainEvent)

    def test_notification_created_with_valid_inputs(self, notification_created):
        assert notification_created.topic == Topic.SALES
        assert (
            notification_created.description == "Valid description with proper length"
        )
        assert notification_created.version == "1.0"

    def test_notification_created_is_immutable(self, notification_created):
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_created.topic = "Topic.MARKETING"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_created.description = "New description"
        with pytest.raises(dataclasses.FrozenInstanceError):
            notification_created.version = "2.0"

    def test_notification_created_raises_value_error_for_too_short_description(self):
        with pytest.raises(ValueError):
            NotificationCreated(topic=Topic.SALES, description="short")

    def test_notification_created_raises_value_error_for_too_long_description(self):
        with pytest.raises(ValueError):
            NotificationCreated(topic=Topic.SALES, description="x" * 201)

    def test_notification_created_raises_pydantic_validation_error_for_invalid_topic(
        self,
    ):
        with pytest.raises(ValidationError):
            NotificationCreated(
                topic="INEXISTENT TOPIC",
                description="Valid description with proper length",
            )

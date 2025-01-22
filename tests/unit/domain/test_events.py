import dataclasses

import pytest

from domain.enums import Topic
from domain.events import DomainEvent, Event, NotificationCreated, NotificationReceived


class TestDomainEvent:
    def test_domain_event_validation(self):
        with pytest.raises(ValueError):
            DomainEvent(topic=Topic.SALES, description="short")

        with pytest.raises(ValueError):
            DomainEvent(topic=Topic.SALES, description="x" * 201)

        event = DomainEvent(
            topic=Topic.SALES, description="Valid description with proper length"
        )
        assert event.topic == Topic.SALES
        assert event.description == "Valid description with proper length"
        assert event.version == "1.0"

    def test_event_immutability(self):
        event = DomainEvent(
            topic=Topic.SALES, description="Testing immutability of the event"
        )
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.topic = "Topic.MARKETING"
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.description = "New description"
        with pytest.raises(dataclasses.FrozenInstanceError):
            event.version = "2.0"


class TestNotificationReceivedEvent:
    def test_notification_received_event_validation(self):
        event = NotificationReceived(
            topic=Topic.SALES,
            description="Notification was received by the recipient",
        )
        assert isinstance(event, DomainEvent)
        assert isinstance(event, Event)
        assert event.topic == Topic.SALES
        assert event.version == "1.0"


class TestNotificationCreated:
    def test_notification_created_with_valid_inputs(self, valid_inputs):
        payload = valid_inputs
        event = NotificationCreated(**payload)
        assert event.topic == payload["topic"]
        assert event.description == payload["description"]
        assert event.version == "1.0"

    def test_notification_created_fails_with_invalid_topic(self, invalid_topic_inputs):
        payload = invalid_topic_inputs
        with pytest.raises(ValueError) as exc_info:
            NotificationCreated(**payload)
        errors = str(exc_info.value)
        assert "topic" in errors

    def test_notification_created_fails_with_invalid_description(
        self, invalid_description_inputs
    ):
        payload = invalid_description_inputs
        with pytest.raises(ValueError) as exc_info:
            NotificationCreated(**payload)
        errors = str(exc_info.value)
        assert "description" in errors

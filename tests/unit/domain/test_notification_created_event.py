import pytest

from domain.events import NotificationCreated


def test_notification_created_initialization_with_valid_payload(
    valid_payload_notification,
):
    payload = valid_payload_notification
    event = NotificationCreated(**payload)
    assert event.topic == payload["topic"]
    assert event.description == payload["description"]
    assert event.timestamp == payload["timestamp"]


def test_notification_created_initialization_invalid_short_description(
    invalid_payload_short_description,
):
    payload = invalid_payload_short_description
    with pytest.raises(ValueError):
        NotificationCreated(**payload)


def test_notification_created_initialization_missing_topic(
    invalid_payload_missing_topic,
):
    payload = invalid_payload_missing_topic
    with pytest.raises(ValueError) as exc_info:
        NotificationCreated(**payload)
    errors = str(exc_info.value)
    assert "topic" in errors


def test_notification_created_initialization_with_varied_invalid_payloads(
    invalid_payload_varied,
):
    payload = invalid_payload_varied
    with pytest.raises(ValueError):
        NotificationCreated(**payload)

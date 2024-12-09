import dataclasses

import pytest

from domain.events import NotificationCreated


def test_notification_created_with_valid_inputs(
    valid_inputs,
):
    payload = valid_inputs
    event = NotificationCreated(**payload)
    assert event.topic == payload["topic"]
    assert event.description == payload["description"]
    assert event.timestamp == payload["timestamp"]
    assert event.version == "1.0"


def test_notification_created_is_immutable(valid_inputs):
    payload = valid_inputs
    event = NotificationCreated(**payload)
    with pytest.raises(dataclasses.FrozenInstanceError):
        event.description = "New description"


def test_notification_created_fails_with_invalid_topic(
    invalid_topic_inputs,
):
    """
    Test invalid 'topic' field inputs for NotificationCreated.
    """
    payload = invalid_topic_inputs
    with pytest.raises(ValueError) as exc_info:
        NotificationCreated(**payload)
    errors = str(exc_info.value)
    assert "topic" in errors


def test_notification_created_fails_with_invalid_description(
    invalid_description_inputs,
):
    """
    Test invalid 'description' field inputs for NotificationCreated.
    """
    payload = invalid_description_inputs
    with pytest.raises(ValueError) as exc_info:
        NotificationCreated(**payload)
    errors = str(exc_info.value)
    assert "description" in errors


def test_notification_created_fails_with_invalid_timestamp(
    invalid_timestamp_inputs,
):
    """
    Test invalid 'timestamp' field inputs for NotificationCreated.
    """
    payload = invalid_timestamp_inputs
    with pytest.raises(ValueError) as exc_info:
        NotificationCreated(**payload)
    errors = str(exc_info.value)
    assert "timestamp" in errors

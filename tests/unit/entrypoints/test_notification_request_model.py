import pytest

from domain.enums import Topic
from entrypoints.routes.models import NotificationRequest


def test_notification_request_valid_inputs(valid_inputs):
    request = NotificationRequest(**valid_inputs)
    assert request.topic == Topic.PRICING
    assert request.description == "New pricing update available."


def test_notification_request_fails_with_invalid_topics(invalid_topic_inputs):
    with pytest.raises(ValueError) as exc_info:
        NotificationRequest(**invalid_topic_inputs)
    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("topic",)
    assert errors[0]["type"] == "enum"


def test_notification_request_fails_with_invalid_descriptions(
    invalid_description_inputs,
):
    with pytest.raises(ValueError) as exc_info:
        NotificationRequest(**invalid_description_inputs)
    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("description",)

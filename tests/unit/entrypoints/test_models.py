import pytest
from pydantic import ValidationError

from domain.enums import Topic
from entrypoints.routes.models import NotificationRequest


def test_notification_request_valid_pricing(valid_payload_pricing):
    request = NotificationRequest(**valid_payload_pricing)
    assert request.topic == Topic.PRICING
    assert request.description == "New pricing update."


def test_notification_request_valid_sales(valid_payload_sales):
    request = NotificationRequest(**valid_payload_sales)
    assert request.topic == Topic.SALES
    assert request.description == "New pricing update."


def test_notification_request_invalid_payloads(invalid_payload):
    with pytest.raises(ValidationError):
        NotificationRequest(**invalid_payload)


def test_notification_request_missing_topic(invalid_payload_missing_topic):
    with pytest.raises(ValidationError) as exc_info:
        NotificationRequest(**invalid_payload_missing_topic)
    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("topic",)
    assert errors[0]["type"] == "missing"


def test_notification_request_missing_description(invalid_payload_missing_description):
    with pytest.raises(ValidationError) as exc_info:
        NotificationRequest(**invalid_payload_missing_description)
    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == ("description",)
    assert errors[0]["type"] == "missing"

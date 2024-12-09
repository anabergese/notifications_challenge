import pytest

from domain.enums import Topic
from domain.events import NotificationCreated


def test_notify_returns_500_because_failures_into_create_notification(
    valid_payload_pricing, mocked_service_failures, client
):
    response = client.post("/notify", json=valid_payload_pricing)
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}
    mocked_service_failures.assert_called_once_with(
        topic=Topic.PRICING, description=valid_payload_pricing["description"]
    )


def test_notify_returns_200_ok_despite_handle_error(
    valid_payload_pricing, mocked_handle_failures, client
):
    response = client.post("/notify", json=valid_payload_pricing)
    assert response.status_code == 200
    assert response.json() == {"message": "Notification created for topic: pricing"}

    mocked_handle_failures.assert_called_once_with(
        NotificationCreated(
            topic=Topic.PRICING,
            description=valid_payload_pricing["description"],
            timestamp=mocked_handle_failures.call_args[0][0].timestamp,
        )
    )


def test_handle_method_receives_notificationcreated_instance_despite_handle_error(
    valid_payload_pricing, mocked_handle_failures, client
):
    client.post("/notify", json=valid_payload_pricing)

    mocked_handle_failures.assert_called_once()
    called_event = mocked_handle_failures.call_args[0][0]
    assert isinstance(called_event, NotificationCreated)
    assert called_event.topic == Topic.PRICING
    assert called_event.description == valid_payload_pricing["description"]
    assert called_event.timestamp is not None


def test_logging_error_includes_event_when_handle_fails(
    valid_payload_pricing, mocked_handle_failures, client, caplog
):
    with caplog.at_level("ERROR"):
        response = client.post("/notify", json=valid_payload_pricing)
    assert response.status_code == 200
    mocked_handle_failures.assert_called_once()

    assert "Error handling event:" in caplog.text
    assert "NotificationCreated" in caplog.text
    assert "topic=<Topic.PRICING: 'pricing'>" in caplog.text
    assert "description='New pricing update.'" in caplog.text

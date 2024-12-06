import pytest
from fastapi.testclient import TestClient

from domain.enums import Topic
from src.entrypoints.main import app

client = TestClient(app)


def test_create_notification_with_service_failure(valid_payload_pricing, mocker):
    mock_create_notification = mocker.patch(
        "service_layer.service.NotificationService.create_notification",
        side_effect=Exception("Service failure"),
    )

    response = client.post("/notify", json=valid_payload_pricing)
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}

    mock_create_notification.assert_called_once_with(
        topic=Topic.PRICING, description=valid_payload_pricing["description"]
    )


def test_create_notification_with_timeout_error(valid_payload_pricing, mocker):
    mock_create_notification = mocker.patch(
        "service_layer.service.NotificationService.create_notification",
        side_effect=TimeoutError("Too much time passed."),
    )

    response = client.post("/notify", json=valid_payload_pricing)
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}

    mock_create_notification.assert_called_once_with(
        topic=Topic.PRICING, description=valid_payload_pricing["description"]
    )

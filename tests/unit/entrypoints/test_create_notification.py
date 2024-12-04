import pytest
from fastapi.testclient import TestClient

from src.entrypoints.main import app

client = TestClient(app)

from unittest.mock import AsyncMock, patch


def test_create_notification_with_service_failure():
    invalid_payload = {"topic": "pricing", "description": "This should fail."}

    # Simula que el método lanza una excepción genérica
    with patch(
        "service_layer.service.NotificationService.create_notification",
        new_callable=AsyncMock,
    ) as mock_create_notification:
        mock_create_notification.side_effect = Exception("Service failure")

        response = client.post("/notify", json=invalid_payload)
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal Server Error"}


def test_create_notification_with_value_error():
    invalid_payload = {"topic": "pricing", "description": "This should fail."}

    # Simula que el método lanza un TimeoutError
    with patch(
        "service_layer.service.NotificationService.create_notification",
        new_callable=AsyncMock,
    ) as mock_create_notification:
        mock_create_notification.side_effect = TimeoutError("Too much time passed.")

        response = client.post("/notify", json=invalid_payload)
        assert response.status_code == 500
        assert response.json() == {"detail": "Internal Server Error"}

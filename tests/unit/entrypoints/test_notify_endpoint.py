import pytest
from fastapi.testclient import TestClient

from src.entrypoints.main import app

client = TestClient(app)


def test_create_notification_with_valid_topic():
    valid_payload = {"topic": "pricing", "description": "New pricing update."}
    response = client.post("/notify", json=valid_payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Notification created for topic: pricing"}


def test_create_notification_with_invalid_topic():
    invalid_payload = {"topic": "invalid_topic", "description": "This should fail."}
    response = client.post("/notify", json=invalid_payload)
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid topic."}

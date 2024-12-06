import pytest


def test_create_notification_with_valid_topic_pricing(valid_payload_pricing, client):
    response = client.post("/notify", json=valid_payload_pricing)
    assert response.status_code == 200
    assert response.json() == {"message": "Notification created for topic: pricing"}


def test_create_notification_with_valid_topic_sales(valid_payload_sales, client):
    response = client.post("/notify", json=valid_payload_sales)
    assert response.status_code == 200
    assert response.json() == {"message": "Notification created for topic: sales"}


def test_create_notification_with_invalid_topics(invalid_payload, client):
    response = client.post("/notify", json=invalid_payload)
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid topic."}


def test_create_notification_with_missing_topic(invalid_payload_missing_topic, client):
    response = client.post("/notify", json=invalid_payload_missing_topic)
    assert response.status_code == 422
    assert response.json() == {"detail": "Topic is required."}


def test_create_notification_with_missing_description(
    invalid_payload_missing_description, client
):
    response = client.post("/notify", json=invalid_payload_missing_description)
    assert response.status_code == 422
    assert response.json() == {"detail": "Description is required."}

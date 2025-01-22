import pytest


class TestCreateNotificationSuccess:
    def test_with_valid_topic_pricing_returns_201(self, valid_payload_pricing, client):
        response = client.post("/notify", json=valid_payload_pricing)
        assert response.status_code == 201
        assert response.json() == {
            "message": "Notification created successfully.",
            "topic": "pricing",
        }

    def test_with_valid_topic_sales_returns_201(self, valid_payload_sales, client):
        response = client.post("/notify", json=valid_payload_sales)
        assert response.status_code == 201
        assert response.json() == {
            "message": "Notification created successfully.",
            "topic": "sales",
        }


class TestCreateNotificationFailure:
    def test_returns_422_invalid_topic(self, invalid_payload_topics, client):
        response = client.post("/notify", json=invalid_payload_topics)
        assert response.status_code == 422
        assert response.json() == {"detail": "Invalid topic."}

    def test_returns_422_invalid_description(
        self, invalid_payload_descriptions, client
    ):
        response = client.post("/notify", json=invalid_payload_descriptions)
        assert response.status_code == 422
        assert response.json() == {"detail": "Invalid description."}

    def test_returns_422_topic_is_required(self, invalid_payload_missing_topic, client):
        response = client.post("/notify", json=invalid_payload_missing_topic)
        assert response.status_code == 422
        assert response.json() == {"detail": "Topic is required."}

    def test_returns_422_description_is_required(
        self, invalid_payload_missing_description, client
    ):
        response = client.post("/notify", json=invalid_payload_missing_description)
        assert response.status_code == 422
        assert response.json() == {"detail": "Description is required."}

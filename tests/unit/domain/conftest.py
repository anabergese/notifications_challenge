from datetime import datetime

import pytest


@pytest.fixture
def valid_payload_notification():
    return {
        "topic": "pricing",
        "description": "New pricing update available.",
        "timestamp": datetime.now(),
    }


@pytest.fixture
def invalid_payload_short_description():
    return {
        "topic": "pricing",
        "description": "123",  # Too short
        "timestamp": datetime.now(),
    }


@pytest.fixture
def invalid_payload_missing_topic():
    return {
        "description": "This should fail.",
        "timestamp": datetime.now(),
    }


@pytest.fixture(
    params=[
        {"topic": "", "description": "Empty string as topic"},
        {"topic": 123, "description": "Integer as topic"},
        {"topic": None, "description": "None as topic"},
        {"topic": "pricing", "description": 123},  # Invalid description type
        {"topic": "pricing", "description": "123"},  # Too short description
        {"topic": "pricing", "description": "a" * 1000},  # Too long description
    ]
)
def invalid_payload_varied(request):
    payload = request.param
    payload["timestamp"] = datetime.now()
    return payload

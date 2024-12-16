from datetime import datetime

import pytest


@pytest.fixture
def valid_inputs():
    return {
        "topic": "pricing",
        "description": "New pricing update available.",
        "timestamp": datetime.now(),
    }


@pytest.fixture(
    params=[
        # Invalid formats
        {"topic": "", "description": "Empty string as topic"},
        {"topic": " ", "description": "Whitespace as topic"},
        {"topic": True, "description": "Boolean as topic"},
        {"topic": {"key": "value"}, "description": "Object as topic"},
        {"topic": ["sales", "pricing"], "description": "List as topic"},
        {"topic": None, "description": "None as topic"},
        # Extreme values
        {"topic": "a" * 1000, "description": "Very long string as topic"},
        {"topic": "123pricing", "description": "String with invalid prefix"},
        # Special characters
        {"topic": "@#$%^&*", "description": "Special characters as topic"},
        {"topic": "sales\npricing", "description": "String with newlines"},
        # Numbers
        {"topic": 0, "description": "Zero as topic"},
        {"topic": -1, "description": "Negative number as topic"},
        {"topic": 1.5, "description": "Float as topic"},
        {"topic": 2e10, "description": "Scientific notation as topic"},
        # Injection strings
        {"topic": "SELECT * FROM users", "description": "SQL injection as topic"},
        {"topic": "<script>alert('hack')</script>", "description": "HTML/JS injection"},
        # Case sensitivity
        {"topic": "PRICING", "description": "Uppercase valid topic"},
        {"topic": "Sales", "description": "Mixed-case valid topic"},
        {"topic": "pricing ", "description": "Valid topic with trailing space"},
    ]
)
def invalid_topic_inputs(request):
    """Provide invalid input data for the 'topic' field."""
    payload = request.param
    payload["timestamp"] = datetime.now()
    return payload


@pytest.fixture(
    params=[
        {"topic": "sales"},
        {"topic": "pricing", "description": 123},
        {"topic": "pricing", "description": ""},
        {"topic": "pricing", "description": " "},
        {"topic": "pricing", "description": "a" * 10000},
        {"topic": "pricing", "description": True},
        {"topic": "pricing", "description": {"key": "value"}},
        {"topic": "pricing", "description": ["sales", "pricing"]},
        {"topic": "pricing", "description": None},
        {"topic": "pricing", "description": 0},
        {"topic": "pricing", "description": -1},
        {"topic": "pricing", "description": 1.5},
    ]
)
def invalid_description_inputs(request):
    """Provide invalid input data for the 'description' field."""
    payload = request.param
    payload["timestamp"] = datetime.now()
    return payload


@pytest.fixture(
    params=[
        {
            "topic": "pricing",
            "description": "Valid description",
            "timestamp": None,
        },
        {
            "topic": "pricing",
            "description": "Valid description",
            "timestamp": "not a datetime",
        },
        {
            "topic": "pricing",
            "description": "Valid description",
            "timestamp": True,
        },
        {
            "topic": "pricing",
            "description": "Valid description",
            "timestamp": {"time": "now"},
        },
    ]
)
def invalid_timestamp_inputs(request):
    """Provide invalid input data for the 'timestamp' field."""
    payload = request.param
    return payload

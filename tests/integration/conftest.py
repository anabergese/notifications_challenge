import pytest


@pytest.fixture
def valid_payload_pricing():
    return {"topic": "pricing", "description": "New pricing update."}


@pytest.fixture
def valid_payload_sales():
    return {"topic": "sales", "description": "New pricing update."}


@pytest.fixture
def invalid_payload_missing_topic():
    return {"description": "This should fail."}


@pytest.fixture
def invalid_payload_missing_description():
    return {"topic": "sales"}


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
def invalid_payload(request):
    return {
        "topic": request.param["topic"],
        "description": request.param["description"],
    }

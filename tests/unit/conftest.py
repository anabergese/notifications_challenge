import pytest

from src.domain.events import DomainEvent, NotificationCreated, NotificationReceived


@pytest.fixture
def valid_inputs():
    return {
        "topic": "pricing",
        "description": "I want to know how much cost AI chats.",
    }


@pytest.fixture
def domain_event(valid_inputs):
    return DomainEvent(
        topic=valid_inputs["topic"],
        description=valid_inputs["description"],
    )


@pytest.fixture
def notification_created(valid_inputs):
    return NotificationCreated(
        topic=valid_inputs["topic"],
        description=valid_inputs["description"],
    )


@pytest.fixture
def notification_received(valid_inputs):
    return NotificationReceived(
        topic=valid_inputs["topic"],
        description=valid_inputs["description"],
    )


@pytest.fixture(
    params=[
        # Invalid formats
        "",
        " ",
        True,
        {"key": "value"},
        ["sales", "pricing"],
        None,
        # Extreme values
        "a" * 1000,
        "123pricing",
        # Special characters
        "@#$%^&*",
        "sales\npricing",
        # Numbers
        0,
        -1,
        1.5,
        2e10,
        # Injection strings
        "SELECT * FROM users",
        "<script>alert('hack')</script>",
        # Case sensitivity
        "PRICING",
        "Sales",
        "pricing ",
    ]
)
def invalid_topic(request):
    """Provide invalid input data for the 'topic' field."""
    return request.param


@pytest.fixture(
    params=[
        123,
        "",
        " ",
        "a" * 201,
        True,
        {"key": "value"},
        ["sales", "pricing"],
        None,
        0,
        -1,
        1.5,
    ]
)
def invalid_description(request):
    """Provide invalid input data for the 'description' field."""
    return request.param

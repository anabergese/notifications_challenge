import pytest

from src.domain.events import DomainEvent, NotificationCreated, NotificationReceived
from src.domain.topic_enums import Topic


@pytest.fixture(scope="module")
def domain_event():
    """Fixture to create a valid mock DomainEvent object."""

    return DomainEvent(
        topic=Topic.SALES,
        description="Valid description with proper length",
        version="1.0",
    )


@pytest.fixture(scope="module")
def notification_created():
    """Fixture to create a valid mock NotificationCreated object."""

    return NotificationCreated(
        topic=Topic.SALES,
        description="Valid description with proper length",
        version="1.0",
    )


@pytest.fixture(scope="module")
def notification_received():
    """Fixture to create a valid mock NotificationReceived object."""

    return NotificationReceived(
        topic=Topic.SALES,
        description="Valid description with proper length",
        version="1.0",
    )

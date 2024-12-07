from datetime import datetime

import pytest

from domain.enums import Topic
from domain.events import NotificationCreated


def test_notification_created_initialization():
    timestamp = datetime.now()
    topic = "pricingss"
    description = "New pricing update available."

    with pytest.raises(ValueError):  # Se espera un ValueError al validar el tipo
        NotificationCreated(topic=topic, description=description, timestamp=timestamp)

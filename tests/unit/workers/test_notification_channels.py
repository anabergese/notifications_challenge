import pytest

from domain.events import DomainEvent
from workers.notification_channels import EmailNotifier, NewNotifier, SlackNotifier


class TestNotificationChannels:
    @pytest.fixture
    def sample_event(self):
        return DomainEvent(topic="pricing", description="test description")

    @pytest.mark.asyncio
    async def test_email_notifier_notify(self, sample_event):
        notifier = EmailNotifier()
        result = await notifier.notify(sample_event)
        expected = (
            "Event with topic pricing sent to EMAIL successfully: test description"
        )
        assert result == expected

    @pytest.mark.asyncio
    async def test_slack_notifier_notify(self, sample_event):
        notifier = SlackNotifier()
        result = await notifier.notify(sample_event)
        expected = (
            "Event with topic pricing sent to SLACK successfully: test description"
        )
        assert result == expected

    @pytest.mark.asyncio
    async def test_new_notifier_notify(self, sample_event):
        notifier = NewNotifier()
        result = await notifier.notify(sample_event)
        expected = "Event with topic pricing sent to NEW CHANNEL successfully: test description"
        assert result == expected

    # test pasa por lo que me da la pauta de que debo agregar manejo de errores/validaciones para el metodo nofity de los notifiers?
    @pytest.mark.asyncio
    async def test_notifiers_with_special_characters(self):
        class MockEvent:
            def __init__(self, topic, description):
                self.topic = topic
                self.description = description

        special_event = MockEvent(topic="test!@#$%", description="desc<>&")
        notifiers = [EmailNotifier(), SlackNotifier(), NewNotifier()]

        expected_results = {
            EmailNotifier: "Event with topic test!@#$% sent to EMAIL successfully: desc<>&",
            SlackNotifier: "Event with topic test!@#$% sent to SLACK successfully: desc<>&",
            NewNotifier: "Event with topic test!@#$% sent to NEW CHANNEL successfully: desc<>&",
        }

        for notifier in notifiers:
            result = await notifier.notify(special_event)
            expected = expected_results[notifier.__class__]
            assert result == expected

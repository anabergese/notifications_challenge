from enum import Enum

import pytest

from src.domain.publisher_enums import RedisStreams


class TestRedisStreamsEnum:
    def test_are_correct_strings(self):
        assert isinstance(RedisStreams.NOTIFICATIONS.value, str)
        assert isinstance(RedisStreams.NOTIFICATIONS_GROUP.value, str)
        assert isinstance(RedisStreams.NOTIFICATIONS_CONSUMER.value, str)

    def test_has_three_allowed_values(self):
        assert len(RedisStreams) == 3

    def test_inherit_from_enum_class(self):
        assert isinstance(RedisStreams.NOTIFICATIONS, Enum)
        assert isinstance(RedisStreams.NOTIFICATIONS_GROUP, Enum)
        assert isinstance(RedisStreams.NOTIFICATIONS_CONSUMER, Enum)

    def test_enum_comparison_works_as_expected(self):
        assert RedisStreams.NOTIFICATIONS == RedisStreams.NOTIFICATIONS
        assert RedisStreams.NOTIFICATIONS != RedisStreams.NOTIFICATIONS_GROUP

    def test_raises_value_error_for_invalid_string(self):
        with pytest.raises(ValueError):
            RedisStreams("notifications_invalid")

    def test_raises_value_error_for_integer_value(self):
        with pytest.raises(ValueError):
            RedisStreams(123)

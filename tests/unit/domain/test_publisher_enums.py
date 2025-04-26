from enum import Enum

import pytest

from src.domain.publisher_enums import RedisStreams


class TestRedisStreamsEnum:
    def test_redis_streams_are_correct_strings(self):
        assert RedisStreams.NOTIFICATIONS.value == "notifications"
        assert RedisStreams.NOTIFICATIONS_GROUP.value == "notifications_group"
        assert RedisStreams.NOTIFICATIONS_CONSUMER.value == "notifications_consumer"
        assert isinstance(RedisStreams.NOTIFICATIONS.value, str)

    def test_redis_streams_enum_has_three_allowed_components(self):
        assert len(RedisStreams) == 3

    def test_redis_streams_inherit_from_enum_class(self):
        assert isinstance(RedisStreams.NOTIFICATIONS, Enum)

    def test_enum_comparison_works_as_expected(self):
        assert RedisStreams.NOTIFICATIONS == RedisStreams.NOTIFICATIONS
        assert RedisStreams.NOTIFICATIONS != RedisStreams.NOTIFICATIONS_GROUP

    def test_redis_streams_raises_value_error_for_invalid_string(self):
        with pytest.raises(ValueError):
            RedisStreams("notifications_invalid")

    def test_redis_streams_raises_value_error_for_integer_value(self):
        with pytest.raises(ValueError):
            RedisStreams(123)

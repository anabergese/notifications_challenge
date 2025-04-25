from enum import Enum

from src.domain.publisher_enums import RedisStreams


def test_redis_streams_available_values_are_strings():
    assert RedisStreams.NOTIFICATIONS.value == "notifications"
    assert RedisStreams.NOTIFICATIONS_GROUP.value == "notifications_group"
    assert RedisStreams.NOTIFICATIONS_CONSUMER.value == "notifications_consumer"
    assert isinstance(RedisStreams.NOTIFICATIONS.value, str)


def test_redis_message_broker_allowed_components_are_three():
    assert len(RedisStreams) == 3


def test_redis_streams_inherit_from_enum():
    assert isinstance(RedisStreams.NOTIFICATIONS, Enum)


def test_enum_comparison():
    assert RedisStreams.NOTIFICATIONS == RedisStreams.NOTIFICATIONS
    assert RedisStreams.NOTIFICATIONS != RedisStreams.NOTIFICATIONS_GROUP

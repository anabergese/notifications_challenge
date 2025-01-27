from src.domain.publisher_enums import RedisStreams
from src.domain.topic_enums import Topic


def test_topic_values():
    assert Topic.SALES.value == "sales"
    assert Topic.PRICING.value == "pricing"
    assert len(Topic) == 3


def test_topic_type():
    assert isinstance(Topic.SALES, Topic)
    assert isinstance(Topic.SALES.value, str)


def test_redis_streams_values():
    assert RedisStreams.NOTIFICATIONS.value == "notifications"
    assert RedisStreams.NOTIFICATIONS_GROUP.value == "notifications_group"
    assert RedisStreams.NOTIFICATIONS_CONSUMER.value == "notifications_consumer"
    assert len(RedisStreams) == 3


def test_redis_streams_type():
    assert isinstance(RedisStreams.NOTIFICATIONS, RedisStreams)
    assert isinstance(RedisStreams.NOTIFICATIONS.value, str)


def test_enum_comparison():
    assert Topic.SALES == Topic.SALES
    assert Topic.SALES != Topic.PRICING
    assert Topic.SALES != RedisStreams.NOTIFICATIONS

from enum import Enum

from src.domain.topic_enums import Topic


def test_available_topic_values_are_strings():
    assert Topic.SALES.value == "sales"
    assert Topic.PRICING.value == "pricing"
    assert isinstance(Topic.SALES.value, str)


def test_topic_allowed_values_are_two():
    assert len(Topic) == 2


def test_topic_inherit_from_enum():
    assert isinstance(Topic.SALES, Topic)
    assert isinstance(Topic.SALES, Enum)


def test_enum_comparison():
    assert Topic.SALES == Topic.SALES
    assert Topic.SALES != Topic.PRICING

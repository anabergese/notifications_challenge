from enum import Enum

import pytest

from src.domain.topic_enums import Topic


def test_topic_values_are_correct_strings():
    assert Topic.SALES.value == "sales"
    assert Topic.PRICING.value == "pricing"
    assert isinstance(Topic.SALES.value, str)


def test_topic_enum_has_two_allowed_values():
    assert len(Topic) == 2


def test_topic_inherit_from_enum_class():
    assert isinstance(Topic.SALES, Topic)
    assert isinstance(Topic.SALES, Enum)


def test_topic_enum_comparison_works_as_expected():
    assert Topic.SALES == Topic.SALES
    assert Topic.SALES != Topic.PRICING


def test_topic_raises_value_error_for_invalid_string():
    with pytest.raises(ValueError):
        Topic("buying")


def test_topic_raises_value_error_for_integer_value():
    with pytest.raises(ValueError):
        Topic(123)

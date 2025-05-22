import pytest

from backend.utils.pricing import calculate_shipping_price


def test_valid_weight_tier_one():
    result = calculate_shipping_price(7)
    assert result == {
        "client_price_per_kg": 18.0,
        "total_client_price": 126.0,
        "our_profit_per_kg": 7.5,
        "total_profit": 52.5,
    }


def test_valid_weight_tier_two():
    result = calculate_shipping_price(12)
    assert result == {
        "client_price_per_kg": 17.75,
        "total_client_price": 213.0,
        "our_profit_per_kg": 7.25,
        "total_profit": 87.0,
    }


def test_invalid_low_weight():
    with pytest.raises(ValueError):
        calculate_shipping_price(4.9)


def test_invalid_high_weight():
    with pytest.raises(ValueError):
        calculate_shipping_price(51)


def test_non_numeric_weight():
    with pytest.raises(ValueError):
        calculate_shipping_price("abc")


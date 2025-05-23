import pytest

from backend.utils.pricing import calculate_shipping_price


@pytest.mark.parametrize(
    "weight,expected",
    [
        (5, {"client_price_per_kg": 18.0, "total_client_price": 90.0, "our_profit_per_kg": 7.5, "total_profit": 37.5}),
        (7, {"client_price_per_kg": 18.0, "total_client_price": 126.0, "our_profit_per_kg": 7.5, "total_profit": 52.5}),
        (10, {"client_price_per_kg": 18.0, "total_client_price": 180.0, "our_profit_per_kg": 7.5, "total_profit": 75.0}),
        (10.01, {"client_price_per_kg": 17.75, "total_client_price": 177.68, "our_profit_per_kg": 7.25, "total_profit": 72.57}),
        (12, {"client_price_per_kg": 17.75, "total_client_price": 213.0, "our_profit_per_kg": 7.25, "total_profit": 87.0}),
        (15, {"client_price_per_kg": 17.75, "total_client_price": 266.25, "our_profit_per_kg": 7.25, "total_profit": 108.75}),
        (15.01, {"client_price_per_kg": 17.5, "total_client_price": 262.68, "our_profit_per_kg": 7.0, "total_profit": 105.07}),
        (22, {"client_price_per_kg": 17.5, "total_client_price": 385.0, "our_profit_per_kg": 7.0, "total_profit": 154.0}),
        (22.01, {"client_price_per_kg": 17.25, "total_client_price": 379.67, "our_profit_per_kg": 6.75, "total_profit": 148.57}),
        (30, {"client_price_per_kg": 17.25, "total_client_price": 517.5, "our_profit_per_kg": 6.75, "total_profit": 202.5}),
        (30.01, {"client_price_per_kg": 17.0, "total_client_price": 510.17, "our_profit_per_kg": 6.5, "total_profit": 195.06}),
        (40, {"client_price_per_kg": 17.0, "total_client_price": 680.0, "our_profit_per_kg": 6.5, "total_profit": 260.0}),
        (40.01, {"client_price_per_kg": 16.75, "total_client_price": 670.17, "our_profit_per_kg": 6.25, "total_profit": 250.06}),
        (50, {"client_price_per_kg": 16.75, "total_client_price": 837.5, "our_profit_per_kg": 6.25, "total_profit": 312.5}),
    ],
)
def test_valid_weights(weight, expected):
    assert calculate_shipping_price(weight) == expected


@pytest.mark.parametrize("weight", [4.9, 51, "abc"])
def test_invalid_weights(weight):
    with pytest.raises(ValueError):
        calculate_shipping_price(weight)


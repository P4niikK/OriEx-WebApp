"""Utility functions for calculating shipping prices."""

from typing import Any, Dict


def calculate_shipping_price(weight_kg: Any) -> Dict[str, float]:
    """Calculate shipping price info based on the given weight in kilograms.

    Parameters
    ----------
    weight_kg : Any
        Weight of the package in kilograms. Can be any type that can be
        converted to ``float``.

    Returns
    -------
    Dict[str, float]
        Dictionary with keys ``client_price_per_kg``, ``total_client_price``,
        ``our_profit_per_kg`` and ``total_profit``.

    Raises
    ------
    ValueError
        If ``weight_kg`` is not numeric or is outside the supported range.
    """

    try:
        weight = float(weight_kg)
    except (TypeError, ValueError):
        raise ValueError("El peso debe ser num\u00e9rico")

    if weight < 5:
        raise ValueError("Peso m\u00ednimo 5kg")
    if weight > 50:
        raise ValueError("Para m\u00e1s de 50kg, por favor solicitar cotizaci\u00f3n especial")

    tiers = [
        (5.00, 10.00, 18.00, 7.50),
        (10.01, 15.00, 17.75, 7.25),
        (15.01, 22.00, 17.50, 7.00),
        (22.01, 30.00, 17.25, 6.75),
        (30.01, 40.00, 17.00, 6.50),
        (40.01, 50.00, 16.75, 6.25),
    ]

    for lower, upper, client_price, profit in tiers:
        if lower <= weight <= upper:
            return {
                "client_price_per_kg": client_price,
                "total_client_price": round(client_price * weight, 2),
                "our_profit_per_kg": profit,
                "total_profit": round(profit * weight, 2),
            }

    # This point should not be reached because of the validations above
    raise ValueError("Rango de peso no soportado")


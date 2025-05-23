from flask import Blueprint, request, jsonify
from backend.utils.pricing import calculate_shipping_price

bp = Blueprint('shipping', __name__)


@bp.route('/api/calculate_shipping', methods=['POST'])
def calculate_shipping():
    """Endpoint to calculate shipping price from weight."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json() or {}
    if 'weight_kg' not in data:
        return jsonify({"error": "weight_kg es requerido"}), 400

    weight = data['weight_kg']
    try:
        price_data = calculate_shipping_price(weight)
        weight = float(weight)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify({
        "weight_kg": weight,
        "client_price_per_kg_usd": price_data["client_price_per_kg"],
        "total_client_price_usd": price_data["total_client_price"],
        "message": "C\u00e1lculo exitoso",
    })

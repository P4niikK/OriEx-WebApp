from flask import Blueprint, request, jsonify
from backend.utils.pricing import calculate_shipping_price

bp = Blueprint('shipping', __name__)

# Example shipments used when a real database is not available.
EXAMPLE_SHIPMENTS = {
    "ABC123": {
        "tracking_id": "ABC123",
        "status": "En tr\u00e1nsito China",
        "origin": "Shenzhen, China",
        "destination": "Buenos Aires, Argentina",
        "estimated_delivery_date": "2030-01-01",
        "history": ["Recibido en almac\u00e9n", "En tr\u00e1nsito China"],
    }
}


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


@bp.route('/api/track_shipment/<string:tracking_id>', methods=['GET'])
def track_shipment(tracking_id):
    """Basic shipment tracking endpoint.

    Tries to fetch a shipment from the database if SQLAlchemy is configured.
    Falls back to example data defined in ``EXAMPLE_SHIPMENTS``.
    """
    # Attempt database lookup if models are available.
    try:
        from backend.models.models import Shipment

        shipment = Shipment.query.filter_by(tracking_id=tracking_id).first()
        if shipment:
            return jsonify(
                {
                    "tracking_id": shipment.tracking_id,
                    "status": shipment.status,
                    "origin": shipment.origin_address_china,
                    "destination": shipment.destination_address_argentina,
                    "estimated_delivery_date": shipment.estimated_delivery_date.isoformat()
                    if shipment.estimated_delivery_date
                    else None,
                }
            )
    except Exception:
        # Database might not be configured; ignore errors and use example data
        pass

    shipment = EXAMPLE_SHIPMENTS.get(tracking_id)
    if shipment:
        return jsonify(shipment)

    return jsonify({"error": "Shipment not found"}), 404

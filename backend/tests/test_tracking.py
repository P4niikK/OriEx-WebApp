from backend.app import create_app


def test_track_shipment_example():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/track_shipment/ABC123')
    assert response.status_code == 200
    data = response.get_json()
    assert data['tracking_id'] == 'ABC123'
    assert 'status' in data


def test_track_shipment_not_found():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/track_shipment/UNKNOWN')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data

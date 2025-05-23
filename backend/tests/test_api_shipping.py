from backend.app import create_app


def test_calculate_shipping_endpoint_valid():
    app = create_app()
    client = app.test_client()
    response = client.post('/api/calculate_shipping', json={'weight_kg': 5})
    assert response.status_code == 200
    data = response.get_json()
    assert data['weight_kg'] == 5.0
    assert data['client_price_per_kg_usd'] == 18.0
    assert data['total_client_price_usd'] == 90.0
    assert data['message'] == 'C\u00e1lculo exitoso'


def test_calculate_shipping_endpoint_invalid():
    app = create_app()
    client = app.test_client()
    response = client.post('/api/calculate_shipping', json={'weight_kg': 4})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_calculate_shipping_endpoint_missing_weight():
    app = create_app()
    client = app.test_client()
    response = client.post('/api/calculate_shipping', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_calculate_shipping_second_tier():
    app = create_app()
    client = app.test_client()
    response = client.post('/api/calculate_shipping', json={'weight_kg': 12})
    assert response.status_code == 200
    data = response.get_json()
    assert data['weight_kg'] == 12.0
    assert data['client_price_per_kg_usd'] == 17.75
    assert data['total_client_price_usd'] == 213.0
    assert data['message'] == 'C\u00e1lculo exitoso'


def test_calculate_shipping_above_max():
    app = create_app()
    client = app.test_client()
    response = client.post('/api/calculate_shipping', json={'weight_kg': 51})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_calculate_shipping_non_numeric():
    app = create_app()
    client = app.test_client()
    response = client.post('/api/calculate_shipping', json={'weight_kg': 'abc'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

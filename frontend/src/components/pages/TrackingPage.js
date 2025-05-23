import React, { useState } from 'react';
import { Link } from 'react-router-dom';

function TrackingPage() {
  const [trackingId, setTrackingId] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleTrack = async () => {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      // When the backend is ready, this call will fetch real data
      const response = await fetch(`/api/track_shipment/${trackingId}`);
      const data = await response.json();
      if (!response.ok) {
        setError(data.error || 'Número de rastreo no encontrado o inválido.');
      } else {
        setResult(data);
      }
    } catch (err) {
      setError('Error de red');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Rastreo de Envíos</h1>
      <div style={{ marginBottom: '1rem' }}>
        <label>
          Ingresa tu Número de Rastreo (Tracking ID):
          <input
            type="text"
            value={trackingId}
            onChange={(e) => setTrackingId(e.target.value)}
            style={{ marginLeft: '0.5rem' }}
          />
        </label>
        <button onClick={handleTrack} disabled={loading || !trackingId} style={{ marginLeft: '0.5rem' }}>
          {loading ? 'Buscando...' : 'Rastrear'}
        </button>
      </div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {result && (
        <div style={{ border: '1px solid #ccc', padding: '1rem' }}>
          <p>
            <strong>Tracking ID:</strong> {result.tracking_id}
          </p>
          <p>
            <strong>Estado:</strong> {result.status}
          </p>
          <p>
            <strong>Origen:</strong> {result.origin}
          </p>
          <p>
            <strong>Destino:</strong> {result.destination}
          </p>
          {result.estimated_delivery_date && (
            <p>
              <strong>Entrega Estimada:</strong> {result.estimated_delivery_date}
            </p>
          )}
          {result.history && (
            <div>
              <h3>Historial</h3>
              <ul>
                {result.history.map((h, idx) => (
                  <li key={idx}>{h}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
      <div style={{ marginTop: '1rem' }}>
        <Link to="/">Volver al inicio</Link>
      </div>
    </div>
  );
}

export default TrackingPage;

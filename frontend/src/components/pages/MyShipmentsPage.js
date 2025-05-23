import React, { useEffect, useState, useContext } from 'react';
import { AuthContext } from '../auth/AuthContext';

function MyShipmentsPage() {
  const { token } = useContext(AuthContext);
  const [shipments, setShipments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchShipments = async () => {
      try {
        const res = await fetch('/api/shipments/me', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        const data = await res.json();
        if (!res.ok) {
          setError(data.error || 'Error');
        } else {
          setShipments(data);
        }
      } catch (err) {
        setError('Error de red');
      } finally {
        setLoading(false);
      }
    };

    if (token) {
      fetchShipments();
    }
  }, [token]);

  if (loading) return <div>Cargando...</div>;
  if (error) return <div style={{ color: 'red' }}>{error}</div>;

  return (
    <div>
      <h1>Mis Envíos</h1>
      <table>
        <thead>
          <tr>
            <th>Tracking ID</th>
            <th>Fecha de Creación</th>
            <th>Peso (kg)</th>
            <th>Costo Total (USD)</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          {shipments.map((s) => (
            <tr key={s.tracking_id}>
              <td>{s.tracking_id}</td>
              <td>{s.created_at ? new Date(s.created_at).toLocaleDateString() : ''}</td>
              <td>{s.weight_kg}</td>
              <td>{s.total_client_price_usd}</td>
              <td>{s.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default MyShipmentsPage;

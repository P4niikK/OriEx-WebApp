import React, { useState } from 'react';
import styles from './ShippingCalculator.module.css';

function ShippingCalculator() {
  const [weight, setWeight] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCalculate = async () => {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const response = await fetch('/api/calculate_shipping', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ weight_kg: parseFloat(weight) }),
      });
      const data = await response.json();
      if (!response.ok) {
        setError(data.error || 'Error desconocido');
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
    <div className={styles.container}>
      <div className={styles.inputGroup}>
        <label>
          Peso del Paquete (kg):
          <input
            type="number"
            value={weight}
            onChange={(e) => setWeight(e.target.value)}
            min="0"
            step="0.01"
          />
        </label>
      </div>
      <button onClick={handleCalculate} disabled={loading}>
        {loading ? 'Calculando...' : 'Calcular Costo'}
      </button>
      {error && <div className={styles.error}>{error}</div>}
      {result && (
        <div className={styles.result}>
          <div>Peso Ingresado: {result.weight_kg} kg</div>
          <div>Costo Estimado Total (USD): {result.total_client_price_usd}</div>
        </div>
      )}
    </div>
  );
}

export default ShippingCalculator;

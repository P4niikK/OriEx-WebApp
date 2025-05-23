import React from 'react';
import ShippingCalculator from '../shipping/ShippingCalculator';

function ShippingCalculatorPage() {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>Calculadora de Envíos</h1>
      <ShippingCalculator />
    </div>
  );
}

export default ShippingCalculatorPage;

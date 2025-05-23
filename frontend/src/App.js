import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './components/pages/HomePage';
import ShippingCalculatorPage from './components/pages/ShippingCalculatorPage';
import TrackingPage from './components/pages/TrackingPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/shipping-calculator" element={<ShippingCalculatorPage />} />
        <Route path="/tracking" element={<TrackingPage />} />
      </Routes>
    </Router>
  );
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './components/pages/HomePage';
import ShippingCalculatorPage from './components/pages/ShippingCalculatorPage';
import TrackingPage from './components/pages/TrackingPage';
import LoginPage from './components/pages/LoginPage';
import RegisterPage from './components/pages/RegisterPage';
import ProtectedRoute from './components/auth/ProtectedRoute';
import DashboardLayout from './components/dashboard/DashboardLayout';
import MyShipmentsPage from './components/pages/MyShipmentsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route element={<ProtectedRoute />}>
          <Route path="/dashboard" element={<DashboardLayout />}>
            <Route index element={<MyShipmentsPage />} />
            <Route path="shipments" element={<MyShipmentsPage />} />
          </Route>
          <Route path="/shipping-calculator" element={<ShippingCalculatorPage />} />
          <Route path="/tracking" element={<TrackingPage />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;

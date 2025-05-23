import React, { useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { AuthContext } from './AuthContext';

function ProtectedRoute({ redirectTo = '/login' }) {
  const { token } = useContext(AuthContext);

  if (!token) {
    return <Navigate to={redirectTo} replace />;
  }

  return <Outlet />;
}

export default ProtectedRoute;

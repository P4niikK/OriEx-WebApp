import React, { useContext } from 'react';
import { Link, Outlet, useNavigate } from 'react-router-dom';
import { AuthContext } from '../auth/AuthContext';

function DashboardLayout() {
  const { logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div style={{ display: 'flex', minHeight: '100vh' }}>
      <nav style={{ width: '200px', background: '#f0f0f0', padding: '1rem' }}>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li>
            <Link to="/dashboard/shipments">Mis Envíos</Link>
          </li>
          <li>
            <Link to="/shipping-calculator">Solicitar Nuevo Envío</Link>
          </li>
          <li>
            <Link to="/dashboard/profile">Mi Perfil</Link>
          </li>
          <li>
            <button onClick={handleLogout}>Cerrar Sesión</button>
          </li>
        </ul>
      </nav>
      <main style={{ flexGrow: 1, padding: '1rem' }}>
        <Outlet />
      </main>
    </div>
  );
}

export default DashboardLayout;

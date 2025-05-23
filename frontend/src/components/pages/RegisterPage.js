import React, { useState } from 'react';

function RegisterPage() {
  const [form, setForm] = useState({ email: '', password: '', full_name: '' });
  const [error, setError] = useState(null);
  const [message, setMessage] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setMessage(null);
    try {
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form),
      });
      const data = await res.json();
      if (!res.ok) {
        setError(data.error || 'Error');
      } else {
        setMessage('Registro exitoso');
      }
    } catch (err) {
      setError('Error de red');
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Registro</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input name="email" value={form.email} onChange={handleChange} />
        </div>
        <div>
          <label>Nombre Completo:</label>
          <input name="full_name" value={form.full_name} onChange={handleChange} />
        </div>
        <div>
          <label>Contraseña:</label>
          <input type="password" name="password" value={form.password} onChange={handleChange} />
        </div>
        <button type="submit">Registrarse</button>
      </form>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {message && <div style={{ color: 'green' }}>{message}</div>}
    </div>
  );
}

export default RegisterPage;

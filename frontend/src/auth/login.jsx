with open("Login.jsx", "r") as f:
    login_code = f.read()

# Inject feature flags and conditional rendering into Login.jsx
updated_login_code = '''
import React, { useState } from 'react';
import axios from 'axios';
import { FEATURE_FLAGS } from './config/constants';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/auth/login', {
        username,
        password
      });
      localStorage.setItem('token', response.data.access_token);
      window.location.href = '/dashboard';
    } catch (err) {
      setError('Invalid credentials');
    }
  };

  return (
    <div>
      <h2>Login</h2>

      {FEATURE_FLAGS.ENABLE_BRANDING && (
        <div style={{ marginBottom: '1em' }}>
          <strong>Welcome to SecurePortal!</strong>
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {FEATURE_FLAGS.ENABLE_LOGIN_HELP && (
        <div style={{ marginTop: '1em' }}>
          <p>Need help? Contact support or reset your password.</p>
        </div>
      )}

      {FEATURE_FLAGS.ENABLE_MFA_PROMPT && (
        <div style={{ marginTop: '1em', color: 'blue' }}>
          <p>Multi-factor authentication is enabled. You will be prompted after login.</p>
        </div>
      )}
    </div>
  );
}

export default Login;
'''

with open("Login.jsx", "w") as f:
    f.write(updated_login_code)

print("Login.jsx has been updated with conditional rendering using feature flags.")



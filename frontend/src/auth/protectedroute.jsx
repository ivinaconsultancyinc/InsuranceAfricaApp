protectedroute_code = '''
import React from 'react';
import { Navigate } from 'react-router-dom';

function ProtectedRoute({ children }) {
  const token = localStorage.getItem('token');
  return token ? children : <Navigate to="/login" />;
}

export default ProtectedRoute;
'''

with open("Login.jsx", "w") as f:
    f.write(login_jsx_code)

with open("ProtectedRoute.jsx", "w") as f:
    f.write(protected_route_code)

print("Login.jsx and ProtectedRoute.jsx have been implemented for the frontend auth folder.")

App.jsx (place this file in main frontend folder)

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Login';
import Dashboard from './Dashboard';
import ProtectedRoute from './ProtectedRoute';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;



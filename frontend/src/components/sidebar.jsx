sidebar_code = '''
import React from 'react';
import { NavLink } from 'react-router-dom';

function Sidebar() {
  const linkStyle = {
    display: 'block',
    padding: '10px 20px',
    textDecoration: 'none',
    color: '#333'
  };

  const activeStyle = {
    fontWeight: 'bold',
    color: '#007bff'
  };

  return (
    <div style={{ width: '200px', background: '#f4f4f4', height: '100vh', paddingTop: '20px' }}>
      <NavLink to="/dashboard" style={linkStyle} activeStyle={activeStyle}>Dashboard</NavLink>
      <NavLink to="/claims" style={linkStyle} activeStyle={activeStyle}>Claims</NavLink>
      <NavLink to="/customers" style={linkStyle} activeStyle={activeStyle}>Customers</NavLink>
      <NavLink to="/audit-logs" style={linkStyle} activeStyle={activeStyle}>Audit Logs</NavLink>
    </div>
  );
}

export default Sidebar;
'''

with open("Sidebar.jsx", "w") as f:
    f.write(sidebar_code)

print("Sidebar.jsx has been created with navigation links and styling.")

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Login from './Login';
import Dashboard from './Dashboard';
import ProtectedRoute from './ProtectedRoute';
import Dashboard from './dashboard/Dashboard';
import './styles.css';
import AccountsPayable from './pages/AccountsPayable';

import ResetPassword from './ResetPassword';
import Client from './components/Client';
import StatisticalReport from './components/StatisticalReport';
import User from './components/User';
import Product from './components/Product';
import Receivable from './components/Receivable';
import Reinsurance from './components/Reinsurance';
import Ledger from './components/Ledger';
import Policy from './components/Policy';
import Premium from './components/Premium';
import Customer from './components/Customer';
import Document from './components/Document';
import GL from './components/GL';
import AuditAccess from './components/AuditAccess';
import ClaimsLoans from './components/ClaimsLoans';
import Commissions from './components/Commissions';
import Agent from './components/Agent';
import Product from './components/Product';
import Receivable from './components/Receivable';


const Sidebar = () => (
  <div className="sidebar">
    <ul>
      <li><Link to="/client">Client</Link></li>
      <li><Link to="/statistical-report">Statistical Report</Link></li>
      <li><Link to="/user">User</Link></li>
      <li><Link to="/product">Product</Link></li>
      <li><Link to="/receivable">Receivable</Link></li>
      <li><Link to="/reinsurance">Reinsurance</Link></li>
      <li><Link to="/ledger">Ledger</Link></li>
      <li><Link to="/policy">Policy</Link></li>
      <li><Link to="/premium">Premium</Link></li>
      <li><Link to="/customer">Customer</Link></li>
      <li><Link to="/document">Document</Link></li>
      <li><Link to="/gl">GL</Link></li>
      <li><Link to="/auditaccess">Audit Access</Link></li>
      <li><Link to="/claimsloans">Claims & Loans</Link></li>
      <li><Link to="/commissions">Commissions</Link></li>
      <li><Link to="/agent">Agent</Link></li>
    </ul>
  </div>
);

function App() {
  return (
    <Router>
      <Sidebar />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        } />
        <Route path="/reset-password" element={<ResetPassword />} />
        <Route path="/client" element={<Client />} />
        <Route path="/statistical-report" element={<StatisticalReport />} />
        <Route path="/user" element={<User />} />
        <Route path="/product" element={<Product />} />
        <Route path="/receivable" element={<Receivable />} />
        <Route path="/reinsurance" element={<Reinsurance />} />
        <Route path="/ledger" element={<Ledger />} />
        <Route path="/policy" element={<Policy />} />
        <Route path="/premium" element={<Premium />} />
        <Route path="/customer" element={<Customer />} />
        <Route path="/document" element={<Document />} />
        <Route path="/gl" element={<GL />} />
        <Route path="/auditaccess" element={<AuditAccess />} />
        <Route path="/claimsloans" element={<ClaimsLoans />} />
        <Route path="/commissions" element={<Commissions />} />
        <Route path="/agent" element={<Agent />} />
        <Route path="/product" element={<ProtectedRoute><Product /></ProtectedRoute>} />
        <Route path="/receivable" element={<ProtectedRoute><Receivable /></ProtectedRoute>} />
      </Routes>
    </Router>
  );
}

export default App;


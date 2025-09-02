import React from 'react';
import { FEATURE_FLAGS } from './config/constants';

function Dashboard() {
  return (
    <div>
      <h1>Welcome to the Dashboard</h1>

      {FEATURE_FLAGS.ENABLE_DASHBOARD_ANALYTICS && (
        <section>
          <h2>Analytics</h2>
          <p>Here are your dashboard analytics...</p>
        </section>
      )}

      {FEATURE_FLAGS.ENABLE_AUDIT_LOGS && (
        <section>
          <h2>Audit Logs</h2>
          <p>Displaying audit logs...</p>
        </section>
      )}

      {FEATURE_FLAGS.ENABLE_STATISTICAL_REPORTING && (
        <section>
          <h2>Statistical Reports</h2>
          <p>Here are your statistical reports...</p>
        </section>
      )}

      {FEATURE_FLAGS.ENABLE_CURRENCY_CONVERSION && (
        <section>
          <h2>Currency Converter</h2>
          <p>Currency conversion tools available...</p>
        </section>
      )}
    </div>
  );
}

export default Dashboard;


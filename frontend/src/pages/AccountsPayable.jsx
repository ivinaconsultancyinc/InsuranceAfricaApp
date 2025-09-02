import React, { useEffect, useState } from 'react';
import axios from 'axios';

function AccountsPayable() {
  const [invoices, setInvoices] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/accounts-payable')
      .then(response => setInvoices(response.data))
      .catch(error => console.error('Error fetching accounts payable:', error));
  }, []);

  return (
    <div>
      <h2>Accounts Payable</h2>
      <ul>
        {invoices.map(invoice => (
          <li key={invoice.id}>
            <strong>Invoice #: {invoice.invoice_number}</strong><br />
            Vendor ID: {invoice.vendor_id}<br />
            Date: {invoice.invoice_date}<br />
            Due: {invoice.due_date}<br />
            Amount: ${invoice.amount} {invoice.currency}<br />
            Status: {invoice.status}<br />
            Approved By: {invoice.approved_by}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AccountsPayable;




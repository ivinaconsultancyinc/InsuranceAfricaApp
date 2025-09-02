import React, { useEffect, useState } from 'react';

const Receivable = () => {
  const [receivables, setReceivables] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('/api/receivables')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setReceivables(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <h2>Receivable List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Customer ID</th>
            <th>Invoice Number</th>
            <th>Amount Due</th>
            <th>Currency</th>
            <th>Due Date</th>
            <th>Payment Date</th>
            <th>Status</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {receivables.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.customer_id}</td>
              <td>{item.invoice_number}</td>
              <td>{item.amount_due}</td>
              <td>{item.currency}</td>
              <td>{item.due_date}</td>
              <td>{item.payment_date || '—'}</td>
              <td>{item.status}</td>
              <td>{item.created_at}</td>
              <td>{item.updated_at || '—'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Receivable;


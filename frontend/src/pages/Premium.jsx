import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Premium = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    policy_id: "", customer_id: "", amount: "", currency: "", due_date: "", payment_date: "", status: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/premium`);
      setRecords(response.data);
    } catch (error) {
      console.error('Error fetching records:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`/api/premium`, formData);
      fetchRecords();
      setFormData({
        policy_id: "", customer_id: "", amount: "", currency: "", due_date: "", payment_date: "", status: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create Premium</h2>
      <form onSubmit={handleSubmit}>
        <input name="policy_id" value={formData.policy_id} onChange={handleChange} placeholder="policy_id" /> <input name="customer_id" value={formData.customer_id} onChange={handleChange} placeholder="customer_id" /> <input name="amount" value={formData.amount} onChange={handleChange} placeholder="amount" /> <input name="currency" value={formData.currency} onChange={handleChange} placeholder="currency" /> <input name="due_date" value={formData.due_date} onChange={handleChange} placeholder="due_date" /> <input name="payment_date" value={formData.payment_date} onChange={handleChange} placeholder="payment_date" /> <input name="status" value={formData.status} onChange={handleChange} placeholder="status" />
        <button type="submit">Add</button>
      </form>

      <h2>Premium List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>policy_id</th> <th>customer_id</th> <th>amount</th> <th>currency</th> <th>due_date</th> <th>payment_date</th> <th>status</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.policy_id}</td> <td>{record.customer_id}</td> <td>{record.amount}</td> <td>{record.currency}</td> <td>{record.due_date}</td> <td>{record.payment_date}</td> <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Premium;


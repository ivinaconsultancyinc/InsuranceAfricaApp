import React, { useState, useEffect } from 'react';
import axios from 'axios';

const GL = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    account_id: "", amount: "", currency: "", debit_credit: "", description: "", reference: "", transaction_date: "", created_by: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/gl`);
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
      await axios.post(`/api/gl`, formData);
      fetchRecords();
      setFormData({
        account_id: "", amount: "", currency: "", debit_credit: "", description: "", reference: "", transaction_date: "", created_by: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create GL</h2>
      <form onSubmit={handleSubmit}>
        <input name="account_id" value={formData.account_id} onChange={handleChange} placeholder="account_id" /> <input name="amount" value={formData.amount} onChange={handleChange} placeholder="amount" /> <input name="currency" value={formData.currency} onChange={handleChange} placeholder="currency" /> <input name="debit_credit" value={formData.debit_credit} onChange={handleChange} placeholder="debit_credit" /> <input name="description" value={formData.description} onChange={handleChange} placeholder="description" /> <input name="reference" value={formData.reference} onChange={handleChange} placeholder="reference" /> <input name="transaction_date" value={formData.transaction_date} onChange={handleChange} placeholder="transaction_date" /> <input name="created_by" value={formData.created_by} onChange={handleChange} placeholder="created_by" />
        <button type="submit">Add</button>
      </form>

      <h2>GL List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>account_id</th> <th>amount</th> <th>currency</th> <th>debit_credit</th> <th>description</th> <th>reference</th> <th>transaction_date</th> <th>created_by</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.account_id}</td> <td>{record.amount}</td> <td>{record.currency}</td> <td>{record.debit_credit}</td> <td>{record.description}</td> <td>{record.reference}</td> <td>{record.transaction_date}</td> <td>{record.created_by}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default GL;


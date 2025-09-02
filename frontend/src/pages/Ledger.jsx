import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Ledger = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    account_id: "", account_name: "", account_type: "", currency: "", balance: "", status: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/ledger`);
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
      await axios.post(`/api/ledger`, formData);
      fetchRecords();
      setFormData({
        account_id: "", account_name: "", account_type: "", currency: "", balance: "", status: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create Ledger</h2>
      <form onSubmit={handleSubmit}>
        <input name="account_id" value={formData.account_id} onChange={handleChange} placeholder="account_id" /> <input name="account_name" value={formData.account_name} onChange={handleChange} placeholder="account_name" /> <input name="account_type" value={formData.account_type} onChange={handleChange} placeholder="account_type" /> <input name="currency" value={formData.currency} onChange={handleChange} placeholder="currency" /> <input name="balance" value={formData.balance} onChange={handleChange} placeholder="balance" /> <input name="status" value={formData.status} onChange={handleChange} placeholder="status" />
        <button type="submit">Add</button>
      </form>

      <h2>Ledger List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>account_id</th> <th>account_name</th> <th>account_type</th> <th>currency</th> <th>balance</th> <th>status</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.account_id}</td> <td>{record.account_name}</td> <td>{record.account_type}</td> <td>{record.currency}</td> <td>{record.balance}</td> <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Ledger;

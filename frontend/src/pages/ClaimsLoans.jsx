import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ClaimsLoans = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    policy_id: "", claim_type: "", claim_amount: "", claim_date: "", status: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/claimsloans`);
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
      await axios.post(`/api/claimsloans`, formData);
      fetchRecords();
      setFormData({
        policy_id: "", claim_type: "", claim_amount: "", claim_date: "", status: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create ClaimsLoans</h2>
      <form onSubmit={handleSubmit}>
        <input name="policy_id" value={formData.policy_id} onChange={handleChange} placeholder="policy_id" /> <input name="claim_type" value={formData.claim_type} onChange={handleChange} placeholder="claim_type" /> <input name="claim_amount" value={formData.claim_amount} onChange={handleChange} placeholder="claim_amount" /> <input name="claim_date" value={formData.claim_date} onChange={handleChange} placeholder="claim_date" /> <input name="status" value={formData.status} onChange={handleChange} placeholder="status" />
        <button type="submit">Add</button>
      </form>

      <h2>ClaimsLoans List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>policy_id</th> <th>claim_type</th> <th>claim_amount</th> <th>claim_date</th> <th>status</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.policy_id}</td> <td>{record.claim_type}</td> <td>{record.claim_amount}</td> <td>{record.claim_date}</td> <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ClaimsLoans;

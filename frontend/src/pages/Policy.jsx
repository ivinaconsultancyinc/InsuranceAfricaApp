import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Policy = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    policy_number: "", client_id: "", product_type: "", start_date: "", end_date: "", premium_amount: "", status: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/policy`);
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
      await axios.post(`/api/policy`, formData);
      fetchRecords();
      setFormData({
        policy_number: "", client_id: "", product_type: "", start_date: "", end_date: "", premium_amount: "", status: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create Policy</h2>
      <form onSubmit={handleSubmit}>
        <input name="policy_number" value={formData.policy_number} onChange={handleChange} placeholder="policy_number" /> <input name="client_id" value={formData.client_id} onChange={handleChange} placeholder="client_id" /> <input name="product_type" value={formData.product_type} onChange={handleChange} placeholder="product_type" /> <input name="start_date" value={formData.start_date} onChange={handleChange} placeholder="start_date" /> <input name="end_date" value={formData.end_date} onChange={handleChange} placeholder="end_date" /> <input name="premium_amount" value={formData.premium_amount} onChange={handleChange} placeholder="premium_amount" /> <input name="status" value={formData.status} onChange={handleChange} placeholder="status" />
        <button type="submit">Add</button>
      </form>

      <h2>Policy List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>policy_number</th> <th>client_id</th> <th>product_type</th> <th>start_date</th> <th>end_date</th> <th>premium_amount</th> <th>status</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.policy_number}</td> <td>{record.client_id}</td> <td>{record.product_type}</td> <td>{record.start_date}</td> <td>{record.end_date}</td> <td>{record.premium_amount}</td> <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Policy;


import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Client = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    full_name: "", email: "", phone: "", address: "", status: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/client`);
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
      await axios.post(`/api/client`, formData);
      fetchRecords();
      setFormData({
        full_name: "", email: "", phone: "", address: "", status: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create Client</h2>
      <form onSubmit={handleSubmit}>
        <input name="full_name" value={formData.full_name} onChange={handleChange} placeholder="full_name" /> <input name="email" value={formData.email} onChange={handleChange} placeholder="email" /> <input name="phone" value={formData.phone} onChange={handleChange} placeholder="phone" /> <input name="address" value={formData.address} onChange={handleChange} placeholder="address" /> <input name="status" value={formData.status} onChange={handleChange} placeholder="status" />
        <button type="submit">Add</button>
      </form>

      <h2>Client List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>full_name</th> <th>email</th> <th>phone</th> <th>address</th> <th>status</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.full_name}</td> <td>{record.email}</td> <td>{record.phone}</td> <td>{record.address}</td> <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Client;



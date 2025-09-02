import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Agent = () => {
  const [agents, setAgents] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    address: ''
  });

  useEffect(() => {
    fetchAgents();
  }, []);

  const fetchAgents = async () => {
    try {
      const response = await axios.get('/api/agents');
      setAgents(response.data);
    } catch (error) {
      console.error('Error fetching agents:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/api/agents', formData);
      fetchAgents();
      setFormData({ name: '', email: '', phone: '', address: '' });
    } catch (error) {
      console.error('Error creating agent:', error);
    }
  };

  return (
    <div>
      <h2>Create Agent</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
        <input name="email" value={formData.email} onChange={handleChange} placeholder="Email" required />
        <input name="phone" value={formData.phone} onChange={handleChange} placeholder="Phone" />
        <input name="address" value={formData.address} onChange={handleChange} placeholder="Address" />
        <button type="submit">Add Agent</button>
      </form>

      <h2>Agent List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {agents.map(agent => (
            <tr key={agent.id}>
              <td>{agent.id}</td>
              <td>{agent.name}</td>
              <td>{agent.email}</td>
              <td>{agent.phone}</td>
              <td>{agent.address}</td>
              <td>{agent.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Agent;


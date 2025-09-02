import React, { useState, useEffect } from 'react';
import axios from 'axios';

const User = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    username: "", email: "", full_name: "", hashed_password: "", role: "", is_active: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/user`);
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
      await axios.post(`/api/user`, formData);
      fetchRecords();
      setFormData({
        username: "", email: "", full_name: "", hashed_password: "", role: "", is_active: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create User</h2>
      <form onSubmit={handleSubmit}>
        <input name="username" value={formData.username} onChange={handleChange} placeholder="username" /> <input name="email" value={formData.email} onChange={handleChange} placeholder="email" /> <input name="full_name" value={formData.full_name} onChange={handleChange} placeholder="full_name" /> <input name="hashed_password" value={formData.hashed_password} onChange={handleChange} placeholder="hashed_password" /> <input name="role" value={formData.role} onChange={handleChange} placeholder="role" /> <input name="is_active" value={formData.is_active} onChange={handleChange} placeholder="is_active" />
        <button type="submit">Add</button>
      </form>

      <h2>User List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>username</th> <th>email</th> <th>full_name</th> <th>hashed_password</th> <th>role</th> <th>is_active</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.username}</td> <td>{record.email}</td> <td>{record.full_name}</td> <td>{record.hashed_password}</td> <td>{record.role}</td> <td>{record.is_active}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default User;


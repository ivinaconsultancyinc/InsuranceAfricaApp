import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Document = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    title: "", description: "", file_path: "", uploaded_by: "", upload_date: "", status: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/document`);
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
      await axios.post(`/api/document`, formData);
      fetchRecords();
      setFormData({
        title: "", description: "", file_path: "", uploaded_by: "", upload_date: "", status: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create Document</h2>
      <form onSubmit={handleSubmit}>
        <input name="title" value={formData.title} onChange={handleChange} placeholder="title" /> <input name="description" value={formData.description} onChange={handleChange} placeholder="description" /> <input name="file_path" value={formData.file_path} onChange={handleChange} placeholder="file_path" /> <input name="uploaded_by" value={formData.uploaded_by} onChange={handleChange} placeholder="uploaded_by" /> <input name="upload_date" value={formData.upload_date} onChange={handleChange} placeholder="upload_date" /> <input name="status" value={formData.status} onChange={handleChange} placeholder="status" />
        <button type="submit">Add</button>
      </form>

      <h2>Document List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>title</th> <th>description</th> <th>file_path</th> <th>uploaded_by</th> <th>upload_date</th> <th>status</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.title}</td> <td>{record.description}</td> <td>{record.file_path}</td> <td>{record.uploaded_by}</td> <td>{record.upload_date}</td> <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Document;


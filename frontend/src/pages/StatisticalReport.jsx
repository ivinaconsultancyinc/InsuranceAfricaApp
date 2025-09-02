import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StatisticalReport = () => {
  const [records, setRecords] = useState([]);
  const [formData, setFormData] = useState({
    title: "", report_type: "", generated_on: "", generated_by: "", status: "", notes: ""
  });

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await axios.get(`/api/statisticalreport`);
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
      await axios.post(`/api/statisticalreport`, formData);
      fetchRecords();
      setFormData({
        title: "", report_type: "", generated_on: "", generated_by: "", status: "", notes: ""
      });
    } catch (error) {
      console.error('Error creating record:', error);
    }
  };

  return (
    <div>
      <h2>Create StatisticalReport</h2>
      <form onSubmit={handleSubmit}>
        <input name="title" value={formData.title} onChange={handleChange} placeholder="title" /> <input name="report_type" value={formData.report_type} onChange={handleChange} placeholder="report_type" /> <input name="generated_on" value={formData.generated_on} onChange={handleChange} placeholder="generated_on" /> <input name="generated_by" value={formData.generated_by} onChange={handleChange} placeholder="generated_by" /> <input name="status" value={formData.status} onChange={handleChange} placeholder="status" /> <input name="notes" value={formData.notes} onChange={handleChange} placeholder="notes" />
        <button type="submit">Add</button>
      </form>

      <h2>StatisticalReport List</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>title</th> <th>report_type</th> <th>generated_on</th> <th>generated_by</th> <th>status</th> <th>notes</th>
          </tr>
        </thead>
        <tbody>
          {records.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.title}</td> <td>{record.report_type}</td> <td>{record.generated_on}</td> <td>{record.generated_by}</td> <td>{record.status}</td> <td>{record.notes}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StatisticalReport;




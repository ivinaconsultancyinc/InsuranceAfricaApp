import json

# Define the structure of Claims.jsx based on Clients.jsx
claims_component = '''
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Claims() {
  const [claims, setClaims] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/claims-loans')
      .then(response => setClaims(response.data))
      .catch(error => console.error('Error fetching claims:', error));
  }, []);

  return (
    <div>
      <h2>Claims</h2>
      <ul>
        {claims.map(claim => (
          <li key={claim.claim_id}>
            <strong>Policy #: {claim.policy_number}</strong><br />
            Type: {claim.claim_type}<br />
            Amount: ${claim.claim_amount}<br />
            Status: {claim.claim_status}<br />
            Date Filed: {claim.date_filed}
          </li>
        ))}
      </ul>
    </div>
  );
}

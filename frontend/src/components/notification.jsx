notification_code = '''
import React from 'react';

function Notification({ message, type }) {
  const styles = {
    padding: '10px',
    margin: '10px 0',
    color: type === 'error' ? 'red' : 'green',
    border: `1px solid ${type === 'error' ? 'red' : 'green'}`,
    borderRadius: '5px'
  };

  return message ? <div style={styles}>{message}</div> : null;
}

export default Notification;
'''


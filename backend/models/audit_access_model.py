from sqlalchemy import Column, Integer, String, DateTime, Time
from datetime import datetime
from database import Base

# Updated AuditLog model to support login and data access logging
class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String)
    entity_id = Column(String)
    action = Column(String)  # e.g., LOGIN, DATA_ACCESS
    performed_by = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(String)

# Updated UserAccess model to support time-based access restrictions
class UserAccess(Base):
    __tablename__ = 'user_access'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    role = Column(String)
    permissions = Column(String)  # comma-separated list
    last_login = Column(DateTime)
    allowed_start_time = Column(Time)  # Time-based access start
    allowed_end_time = Column(Time)    # Time-based access end

# Save the updated model to audit_access_model.py
updated_model_code = '''
from sqlalchemy import Column, Integer, String, DateTime, Time
from datetime import datetime
from database import Base

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String)
    entity_id = Column(String)
    action = Column(String)
    performed_by = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(String)

class UserAccess(Base):
    __tablename__ = 'user_access'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    role = Column(String)
    permissions = Column(String)  # comma-separated list
    last_login = Column(DateTime)
    allowed_start_time = Column(Time)  # Time-based access start
    allowed_end_time = Column(Time)    # Time-based access end
'''

with open("audit_access_model.py", "w") as f:
    f.write(updated_model_code)



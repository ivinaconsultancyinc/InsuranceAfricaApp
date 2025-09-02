from sqlalchemy import Column, Integer, String, Date
from database import Base  # assuming shared Base

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    report_type = Column(String)
    generated_on = Column(Date)
    generated_by = Column(String)
    status = Column(String)
    notes = Column(String)

from sqlalchemy import Column, Integer, String, Float, Date
from ..database import Base

class ReinsuranceTreaty(Base):
    __tablename__ = "reinsurance_treaties"

    id = Column(Integer, primary_key=True, index=True)
    treaty_name = Column(String, unique=True, index=True)
    insurer = Column(String)
    coverage_type = Column(String)
    coverage_limit = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, default="active")
"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import Column, VARCHAR, Integer
from src.database.base import Base
# any_imports



class AutoModelOne(Base):
    __tablename__ = 'ones'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True)
    # relations

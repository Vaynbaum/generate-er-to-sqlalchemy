"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import Column, VARCHAR, INTEGER
from src.database.base import Base
# any_imports



class AutoModelSubject(Base):
    __tablename__ = 'subjects'
    id = Column(INTEGER, primary_key=True)
    title = Column(VARCHAR, unique=True)
    # relations
"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import VARCHAR, Column, Integer
from src.database.base import Base
# any_imports



class AutoModelGroup(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    title = Column(VARCHAR, unique=True)
    # relations

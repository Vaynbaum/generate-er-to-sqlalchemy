"_qRT9DB5e9rWe48j42IU"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import VARCHAR, Integer, Column
from src.database.base import Base
# any_imports



class AutoModelRole(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True)
    # relations

"_qRT9DB5e9rWe48j42IU"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import ForeignKey, VARCHAR, Integer, Column
from sqlalchemy.orm import relationship, backref

from src.database.base import Base
# any_imports
from src.database.models.user_gemodels.teacher import Teacher



class AutoModelRecord(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    owner_id = Column(Integer, ForeignKey(Teacher.id))
    # relations
    owner = relationship(Teacher, backref=backref("records", cascade="all, delete-orphan"))

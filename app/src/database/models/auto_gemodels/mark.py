"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import ForeignKey, Column, DateTime, Integer
from sqlalchemy.orm import relationship, backref

from src.database.base import Base
# any_imports
from src.database.models.user_gemodels.subject import Subject



class AutoModelMark(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey(Subject.id))
    date = Column(DateTime)
    mark = Column(Integer)
    # relations
    subject = relationship(Subject, backref=backref("marks", cascade="all, delete-orphan"))

"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import Column, ForeignKey, DATETIME, INTEGER
from sqlalchemy.orm import relationship, backref

from src.database.base import Base
# any_imports
from src.database.models.user_gemodels.subject import Subject



class AutoModelMark(Base):
    __tablename__ = 'marks'
    id = Column(INTEGER, primary_key=True)
    subject_id = Column(INTEGER, ForeignKey(Subject.id))
    date = Column(DATETIME)
    mark = Column(INTEGER)
    # relations
    subject = relationship(Subject, backref=backref("marks", cascade="all, delete-orphan"))

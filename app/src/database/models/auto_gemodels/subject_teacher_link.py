"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import Column, ForeignKey, INTEGER
from sqlalchemy.orm import relationship, backref

from src.database.base import Base
# any_imports
from src.database.models.user_gemodels.subject import Subject
from src.database.models.user_gemodels.teacher import Teacher



class AutoModelSubjectTeacherLink(Base):
    __tablename__ = 'subject_teacher_links'
    subject_id = Column(INTEGER, ForeignKey(Subject.id), primary_key=True)
    teacher_id = Column(INTEGER, ForeignKey(Teacher.id), primary_key=True)
    # relations
    subject = relationship(Subject, backref=backref("subject_teacher_links", cascade="all, delete-orphan"))
    teacher = relationship(Teacher, backref=backref("subject_teacher_links", cascade="all, delete-orphan"))

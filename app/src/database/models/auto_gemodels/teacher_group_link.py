"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import Column, ForeignKey, INTEGER
from sqlalchemy.orm import relationship, backref

from src.database.base import Base
# any_imports
from src.database.models.user_gemodels.teacher import Teacher
from src.database.models.user_gemodels.group import Group



class AutoModelTeacherGroupLink(Base):
    __tablename__ = 'teacher_group_links'
    teacher_id = Column(INTEGER, ForeignKey(Teacher.id), primary_key=True)
    group_id = Column(INTEGER, ForeignKey(Group.id), primary_key=True)
    # relations
    teacher = relationship(Teacher, backref=backref("teacher_group_links", cascade="all, delete-orphan"))
    group = relationship(Group, backref=backref("teacher_group_links", cascade="all, delete-orphan"))

"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import Column, VARCHAR, ForeignKey, Integer
from sqlalchemy.orm import relationship, backref

from src.database.base import Base
# any_imports
from src.database.models.user_gemodels.teacher import Teacher



class AutoModelInfoTeacher(Base):
    __tablename__ = 'info_teachers'
    teacher_id = Column(Integer, ForeignKey(Teacher.id), primary_key=True)
    patronymic = Column(VARCHAR(255))
    # relations
    teacher = relationship(Teacher, backref=backref("info_teachers", cascade="all, delete-orphan"))

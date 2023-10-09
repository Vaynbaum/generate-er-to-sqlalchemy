"e56a1550-8fbb-45ad-956c-1786394a9013"
# Auto generated model. Don't add a custom description here 

from sqlalchemy import Column, ForeignKey, VARCHAR, INTEGER
from sqlalchemy.orm import relationship, backref

from src.database.base import Base
# any_imports
from src.database.models.user_gemodels.one import One
from src.database.models.user_gemodels.role import Role


class AutoModelTeacher(Base):
    __tablename__ = 'teachers'
    id = Column(INTEGER, primary_key=True)
    firstname = Column(VARCHAR(255))
    lastname = Column(VARCHAR(255))
    role_id = Column(INTEGER)
    one_id = Column(INTEGER, ForeignKey(One.id))
    # relations
    one = relationship(One, backref=backref("teachers", cascade="all, delete-orphan"))
    role = relationship(Role, backref=backref("teachers", cascade="all, delete-orphan"))
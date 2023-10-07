from sqlalchemy import {imports}
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class {class_name}(Base):
    __tablename__ = '{table_name}'
{fields}
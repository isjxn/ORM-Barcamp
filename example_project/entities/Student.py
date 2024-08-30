from entities.Base import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
  __tablename__ = "students"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
from entities.association_table import association_table
from entities.Base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Student(Base):
  __tablename__ = "students"
  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  courses = relationship("Course", back_populates="students", secondary=association_table)
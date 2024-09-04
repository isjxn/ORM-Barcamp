from entities.Base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from entities.association_table import association_table

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="courses", secondary=association_table)
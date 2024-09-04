from sqlalchemy import Table, Column, ForeignKey
from entities.Base import Base

association_table = Table(
    "association_table",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)
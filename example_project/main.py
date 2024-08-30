
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.Base import Base
from entities.Student import Student

# Intialize the database
engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a new student to the database
new_student = Student(name='John Doe', age=21)
session.add(new_student)
session.commit()

# Query the database
students = session.query(Student).all()
for student in students:
  print(student.name, student.age)

# Delete all students from the database
session.query(Student).delete()
session.commit()

# Close the session
session.close()

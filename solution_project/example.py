
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.Base import Base
from entities.Student import Student

# Intialize the database
engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


# -- {Example CRUD operations} --

# -- Create --
new_student = Student(name='John Doe', age=21)
session.add(new_student)
session.commit()

new_student = Student(name='Max Mustermann', age=30)
session.add(new_student)
session.commit()

# -- Read --
# Read a single student (the first one in this case)
student = session.query(Student).first()
print("Read a single student:")
print(student.name, student.age)

# Read all students
print("\nRead all students:")
students = session.query(Student).all()
for student in students:
  print(student.name, student.age)

# Read a student by their name
student = session.query(Student).filter_by(name='John Doe').first()
print("\nRead a student by their name:")
print(student.name, student.age)

# Read a student who is older than 25
student = session.query(Student).filter(Student.age > 25).first()
print("\nRead a student who is older than 25:")
print(student.name, student.age)

# -- Update --
# Update a students age
student = session.query(Student).filter_by(name='John Doe').first()
student.age = 25
session.commit()

print("\nUpdated student age:")
print(student.name, student.age)

# -- Delete --
# Delete a student (named John Doe)
student = session.query(Student).filter_by(name='John Doe').first()
session.delete(student)
session.commit()

# Delete all students
session.query(Student).delete()
session.commit()

# -- {End of Example CRUD operations} --

# Close the session
session.close()
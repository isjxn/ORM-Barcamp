from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.Base import Base
from entities.Student import Student
from entities.Course import Course

# Intialize the database
engine = create_engine("sqlite:///example.db")
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Exercise 1
new_student = Student(name='Linus Torvalds', age=54)
session.add(new_student)
session.commit()

student = session.query(Student).filter_by(name='Linus Torvalds').first()
print("The student's name is " + student.name + " and they are " + str(student.age) + " years old.")

# Exercise 2
student = session.query(Student).filter_by(name='Linus Torvalds').first()
student.name = "Steve Jobs"
session.commit()

student = session.query(Student).filter_by(name='Steve Jobs').first()
print("The updated student's name is " + student.name + " and they are " + str(student.age) + " years old.")

# Exercise 3
student = session.query(Student).filter_by(name='Steve Jobs').first()
session.delete(student)
session.commit()

all_students = session.query(Student).all()
for student in all_students:
    print("Name: " + student.name + ", Age: " + str(student.age))

# Exercise 4
compsci_course = Course(name="Computer Science 101")
history_course = Course(name="History 201")
session.add(compsci_course)
session.add(history_course)

all_courses = session.query(Course).all()
for course in all_courses:
    print("Course ID: " + str(course.id) + ", Course Name: " + course.name)

# Exercise 5
linus_torvalds = session.query(Student).filter_by(name='Linus Torvalds').first()
compsci_course = session.query(Course).filter_by(name='Computer Science 101').first()
linus_torvalds.courses.append(compsci_course)

steve_jobs = session.query(Student).filter_by(name='Steve Jobs').first()
history_course = session.query(Course).filter_by(name='History 201').first()
steve_jobs.courses.append(history_course)

students_in_courses = session.query(Student).filter(Student.courses.any()).all()
for student in students_in_courses:
    for course in student.courses:
        print(student.name + " is enrolled in " + course.name + ".")

# Exercise 6
compsci_course = session.query(Course).filter_by(name="Computer Science 101").first()

for student in compsci_course.students:
    print("Student enrolled in Computer Science 101: " + student.name)

all_students = session.query(Student).all()
for student in all_students:
    print(student.name + " is enrolled in " + str(len(student.courses)) + " courses.")

students_with_no_courses = session.query(Student).filter(Student.courses == None).all()
for student in students_with_no_courses:
    print("Student not enrolled in any courses: " + student.name)

# Close the session
session.close()
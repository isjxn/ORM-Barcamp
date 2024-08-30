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

# Exercise 1

# Exercise 2

# Exercise 3

# Exercise 4
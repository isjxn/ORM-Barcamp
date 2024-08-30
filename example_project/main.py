from sqlalchemy import create_engine
engine = create_engine("sqlite:///example.db")
connection = engine.connect()
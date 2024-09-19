from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///music_app.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///albums.db"  # You can change this to your preferred database

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

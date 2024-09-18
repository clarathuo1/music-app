from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///music_app.db')
Session = sessionmaker(bind=engine)
session = Session()

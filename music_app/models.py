from sqlalchemy import (
    Column, Table, ForeignKey, Integer, String, DateTime, func, ARRAY
)

from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

artist_album= Table(
    'artist_album',
    Base.metadata,
    Column('artist_id', Integer, ForeignKey('artists.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)

class Artist(Base):
    __tablename__ = 'artists'
    
    id = Column(Integer, primary_key=True)
    stage_name = Column(String)
    real_name = Column(String)
    updated_on = Column(DateTime, onupdate=func.now())
    
    albums = relationship('Album', backref=backref('artist'))
    genres = relationship('Genre', secondary=artist_album, back_populates='artists')
       
    

class Album(Base):
    __tablename__ = 'albums'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    released_on = Column(DateTime, server_default=func.now())
    updated_on = Column(DateTime, onupdate=func.now())
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    albums = relationship('Album', backref=backref('genre'))
    artists = relationship('Artist', secondary=artist_album, back_populates='genres')
    
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import engine, Session

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    albums = relationship('Album', back_populates='genre')

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    albums = relationship('Album', back_populates='artist')

class Album(Base):
    __tablename__ = 'albums'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist_id = Column(Integer, ForeignKey('artists.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

    artist = relationship('Artist', back_populates='albums')
    genre = relationship('Genre', back_populates='albums')

# Create tables
Base.metadata.create_all(engine)

# ORM Methods
def add_artist(name):
    session = Session()
    artist = Artist(name=name)
    session.add(artist)
    session.commit()
    session.close()

def add_album(title, artist_name, genre_name):
    session = Session()
    artist = session.query(Artist).filter_by(name=artist_name).first()
    genre = session.query(Genre).filter_by(name=genre_name).first()
    
    if not artist:
        artist = Artist(name=artist_name)
        session.add(artist)
    
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)

    album = Album(title=title, artist=artist, genre=genre)
    session.add(album)
    session.commit()
    session.close()

def get_albums_by_artist(artist_name):
    session = Session()
    albums = session.query(Album).join(Artist).filter(Artist.name == artist_name).all()
    session.close()
    return albums

def get_albums_by_genre(genre_name):
    session = Session()
    albums = session.query(Album).join(Genre).filter(Genre.name == genre_name).all()
    session.close()
    return albums

def delete_album(album_id):
    session = Session()
    album = session.query(Album).filter_by(id=album_id).first()
    if album:
        session.delete(album)
        session.commit()
    session.close()

def list_artists():
    session = Session()
    artists = session.query(Artist).all()
    session.close()
    return artists

def list_albums():
    session = Session()
    albums = session.query(Album).all()
    session.close()
    return albums

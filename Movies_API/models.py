from sqlalchemy import Column, Integer, String, Float , ForeignKey
from database import Base

class Director(Base):
    __tablename__ = "director"

    id    = Column(Integer, primary_key=True)
    name  = Column(String(100))
    email = Column(String(255))
    country = Column(String(500))
    age =Column(Integer)



class Movie(Base):
    __tablename__ = "movie"

    id    = Column(Integer, primary_key=True)
    title  = Column(String(100))
    genre = Column(String(100))
    release_year=Column(Integer)
    rating= Column(Float)
    director_id  = Column(Integer, ForeignKey("director.id"))
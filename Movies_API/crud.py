# Client

# ↓

# Router

# ↓

# CRUD.py

# ↓

# SQLAlchemy Model

# ↓

# Database



from sqlalchemy.orm import Session
from schemas import MovieRequest,DirectorCreate 
from models import Director , Movie

# db → Database session
# movie → User ka data

# db ke andar kya hota hai?
# Yaad hai database.py me humne banaya tha:
# SessionLocal = sessionmaker(...)
# Aur
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# get_db() har request ke liye ek database session banata hai.

# db.add() dictionary accept nahi karta.
# Isme id hi nahi hai.

# Kyun?

# Kyunki id PostgreSQL khud generate karega.
def create_movie(db:Session,movie:MovieRequest):
  #Movie ek class hai jo tmne bnayi hai models me 
#   class Student:  python basic
#     pass

# s = Student()  s is a object but here movie_data is object 
# # Student() → Object create ho raha hai (constructor call)
# s → Us object ka reference (variable)  
  movie_data = Movie(  
    title = movie.title,
    genre = movie.genre,
    release_year = movie.release_year,
    rating = movie.rating
)
  db.add(movie_data)
  db.commit()
  db.refresh(movie_data)
  return movie_data

# db.add(db_movie)

# Is line ke turant baad (aur commit() se pehle), kya movie PostgreSQL database me save ho chuki hoti hai?

# A) ✅ Haan
# B) ❌ Nahi, sirf session me hai
# C) Sirf RAM me hai, session me bhi nahi

# Ab tumne Pydantic (MovieRequest) se SQLAlchemy (Movie) object bana diya.
# db.add() kuch return nahi karta.

# Ye sirf object ko session me add karta hai.
# Kyuki add() sirf session me add karta hai.

# Actual PostgreSQL me save commit() karta hai.


def get_all_movies(db: Session):
    movies = db.query(Movie).all()
    return movies
def get_movie_by_id(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    return movie
def get_movie_by_id(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    return movie

def update_movie(db: Session, movie_id: int, movie: MovieRequest):

    movie_data = db.query(Movie).filter(Movie.id == movie_id).first()

    if movie_data:

        movie_data.title = movie.title
        movie_data.genre = movie.genre
        movie_data.release_year = movie.release_year
        movie_data.rating = movie.rating

        db.commit()
        db.refresh(movie_data)

    return movie_data



def create_director(db: Session, director: DirectorCreate):

    db_director = Director(
        name=director.name,
        email=director.email,
        country=director.country,
        age=director.age
    )

    db.add(db_director)
    db.commit()
    db.refresh(db_director)

    return db_director


def get_all_directors(db: Session):
    return db.query(Director).all()


def get_director_by_id(db: Session, director_id: int):
    return db.query(Director).filter(Director.id == director_id).first()


def update_director(db: Session, director_id: int, director: DirectorCreate):

    db_director = db.query(Director).filter(Director.id == director_id).first()

    if db_director:
        db_director.name = director.name
        db_director.email = director.email
        db_director.country = director.country
        db_director.age = director.age

        db.commit()
        db.refresh(db_director)

    return db_director


def delete_director(db: Session, director_id: int):

    db_director = db.query(Director).filter(Director.id == director_id).first()

    if db_director:
        db.delete(db_director)
        db.commit()

    return db_director
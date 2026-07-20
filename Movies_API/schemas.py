from pydantic import BaseModel
from typing import Optional



class MovieRequest(BaseModel):#industry MovieCreate
    title  : str
    genre : Optional[str]=None
    release_year:int
    rating: float

class MovieResponse(BaseModel):
    id:int
    title : str
    genre : Optional[str] = None  #Agar genre optional hai request me, to response me bhi optional rakh sakte ho:
    release_year :int
    rating : float


#"Lekin SQLAlchemy model nahi hai."
# Sahi hai. Abhi schemas.py me SQLAlchemy model nahi hai. Aur hona bhi nahi chahiye.
# Dekho flow:

# models.py (SQLAlchemy)

# Yahan ye hai:

# class Movie(Base):
#     __tablename__ = "movie"

#     id = Column(Integer, primary_key=True)
#     title = Column(String(100))
#     genre = Column(String(100))
#     release_year = Column(Integer)
#     rating = Column(Float)

# Ye SQLAlchemy Model hai.

# =============
# schemas.py (Pydantic)

# Yahan ye hai:

# class MovieResponse(BaseModel):
#     id: int
#     title: str
#     genre: Optional[str]
#     release_year: int
#     rating: float

# Ye Pydantic Schema hai.

# Ab from_attributes = True kyun?

# Abhi tumhe iska use dikh nahi raha kyunki abhi CRUD likha hi nahi hai.

# Baad me jab tum aisa karoge:

# movie = Movie(
#     title="Inception",
#     genre="Sci-Fi",
#     release_year=2010,
#     rating=8.8
# )

# db.add(movie)
# db.commit()
# db.refresh(movie)

# return movie

# Dhyan do:

# return movie

# Ye Movie SQLAlchemy object return kar raha hai.

# FastAPI ka response model hoga:

# response_model=MovieResponse

# Ab FastAPI ko SQLAlchemy object ko Pydantic object me convert karna padega.

# Us conversion ke liye:

# class Config:
#     from_attributes = True

# likhte hain.

# Agar from_attributes=True na likho

# To SQLAlchemy object ko Pydantic parse karne me error aa sakta hai (especially Pydantic v2 ke saath).




class DirectorCreate(BaseModel):
    name  : str
    email : str
    country : str="India"
    age : int


class DirectorResponse(BaseModel):
    id    : int
    name  : str
    email : str
    country : str
    age : int




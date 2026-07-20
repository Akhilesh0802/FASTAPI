from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from schemas import MovieRequest, MovieResponse
from database import get_db

router = APIRouter(
    prefix="/movies",
    tags=["Movies"]
)


@router.post("/", response_model=MovieResponse)
def create_movie(movie: MovieRequest, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)


@router.get("/", response_model=list[MovieResponse])
def get_all_movies(db: Session = Depends(get_db)):
    return crud.get_all_movies(db)


@router.get("/{movie_id}", response_model=MovieResponse)
def get_movie_by_id(movie_id: int, db: Session = Depends(get_db)):
    return crud.get_movie_by_id(db, movie_id)


@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie(
    movie_id: int,
    movie: MovieRequest,
    db: Session = Depends(get_db)
):
    return crud.update_movie(db, movie_id, movie)


@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    crud.delete_movie(db, movie_id)
    return {"message": "Movie deleted successfully"}
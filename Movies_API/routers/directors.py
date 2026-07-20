from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from schemas import DirectorCreate, DirectorResponse
from database import get_db

router = APIRouter(
    prefix="/directors",
    tags=["Directors"]
)


@router.post("/", response_model=DirectorResponse)
def create_director(
    director: DirectorCreate,
    db: Session = Depends(get_db)
):
    return crud.create_director(db, director)


@router.get("/", response_model=list[DirectorResponse])
def get_all_directors(db: Session = Depends(get_db)):
    return crud.get_all_directors(db)


@router.get("/{director_id}", response_model=DirectorResponse)
def get_director_by_id(
    director_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_director_by_id(db, director_id)


@router.put("/{director_id}", response_model=DirectorResponse)
def update_director(
    director_id: int,
    director: DirectorCreate,
    db: Session = Depends(get_db)
):
    return crud.update_director(db, director_id, director)


@router.delete("/{director_id}")
def delete_director(
    director_id: int,
    db: Session = Depends(get_db)
):
    crud.delete_director(db, director_id)
    return {"message": "Director deleted successfully"}
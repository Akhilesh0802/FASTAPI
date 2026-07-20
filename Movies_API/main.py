from fastapi import FastAPI

from database import engine
from models import Base

from routers import movies, directors


# Database me tables create karega
Base.metadata.create_all(bind=engine)


# FastAPI app
app = FastAPI(
    title="Movie & Director API",
    description="CRUD API using FastAPI + PostgreSQL + SQLAlchemy",
    version="1.0.0"
)


# Routers include
app.include_router(movies.router)
app.include_router(directors.router)


# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to Movie & Director API"
    }
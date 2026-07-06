from fastapi import FastAPI
from routers import notes 



app = FastAPI(
    title       = "Notes API",
    description = "Meri notes app",
    version     = "1.0.0"
)

app.include_router(notes.router)


@app.get('/')
def notes_fetch():
  return { "message" : 'Notes Received '}


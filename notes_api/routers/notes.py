# FastAPI()   =  Main app — ek hi hoga
# APIRouter() =  Mini app — har feature ka alag
# include_router() = Dono ko jodo


from fastapi import APIRouter , HTTPException
from models import NoteCreate , NoteResponse 
from storage import notes_db , counter
from datetime import datetime

router=APIRouter(
    prefix = "/notes",
    tags   = ["Notes"]
)
#Matlab is router ke andar jitne bhi routes honge, sabke aage automatically /notes lag jayega.

@router.get('/')
def get_all_notes():
  return list(notes_db.values())

@router.get('/{note_id}')
def get_one_notes(note_id : int):
  note_id=notes_db.get(note_id)

  if note_id is None:
    raise HTTPException (
      status_code=401 ,
      details="nhii mila")
  return note_id
  


@router.post('/',response_model=NoteResponse)
def create_notes(notes:NoteCreate):#Yahan note object hai, aur NoteCreate us object ki class (type/model) hai.  notes - Iske andarnote.title , note.content , note.priority   sab available hai notes  me .
  global counter  # Kyunki tum global variable ki value modify kar rahe ho.  islye 
  note_id=counter
  created = datetime.now().isoformat()
  new_note ={
    "id" : note_id,
    "title" : notes.title,
    "content" : notes.content,
    "priority" : notes.priority,
    "status"   : notes.status,
    "level_of_interesting":notes.level_of_interesting,
    "created_at" : created

  }

  notes_db[note_id]=new_note
  counter+=1
  return new_note
  

@router.delete('/{note_id}')
def delete_one_note(note_id : int):
  note=notes_db.get(note_id)
  if note is None:
     raise HTTPException(
       status_code=404,
       detail="nhii mila"
     )
  del notes_db[note_id]
  return "Delete Succesfully"


@router.put('/{note_id}', response_model=NoteResponse)
def update_note(note_id: int, updated_note: NoteCreate):

    note = notes_db.get(note_id)

    if note is None:
        raise HTTPException(404,"Nhii mila")

    # Fields update karo   but hard code 
    # note["title"]   = "ayush ki photo ka summary"
    # note["content"] = "maje aa gaye "
    # baaki fields bhi...


    note["title"]                = updated_note.title
    note["content"]              = updated_note.content
    note["priority"]             = updated_note.priority
    note["status"]               = updated_note.status
    note["level_of_interesting"] = updated_note.level_of_interesting

    return note
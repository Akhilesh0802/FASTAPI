from pydantic import BaseModel
from typing import Optional


#ye User create krega tb ka blueprint hai 
class NoteCreate(BaseModel): 
  title : str
  content : str 
  priority : str ="Medium"
  status : str ="Pending"
  level_of_interesting : Optional[str]=None



# User kabhi bhi
# id
# created_at
# nahi bhejta.
# Ye server khud banata hai.
class NoteResponse(BaseModel):
  id : int
  created_at : str
  title : str
  content : str 
  priority : str ="Medium"
  status : str ="Pending"
  level_of_interesting : Optional[str]=None
      

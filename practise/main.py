from fastapi import FastAPI
from pydantic import BaseModel

student=[]
app = FastAPI()

class Address(BaseModel):
    address:str
    pincode:int

class Details(BaseModel):
    id:int
    student_name:str
    marks: int
    address:Address
    

"detail variable jo store Details"
@app.post("/add_item")
def add_item(details:Details):
    student.append(details)
    return student
"abhi show nhii hoga data browser docs pe check krte hai  broswer pe get hoga tb check   "


@app.get("/show/{ids}")
def show_item(ids :int):
    for i in student:
        if i.id==ids:
          return i
    return {"message": "NOT" }
    
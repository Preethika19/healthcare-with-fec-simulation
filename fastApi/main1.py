from typing import Union

from fastapi import FastAPI

import main as db
from model import Student
app = FastAPI()

connection = db.connect_db()

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/get-students")
async def get_student() :
    return db.get_students(connection)

@app.post("/register-student")
async def addStudent(student : Student) :
    return db.save_student(student, connection)

@app.get("/search-student")
async def searchStudent(part_name : str) :
    return db.searchStudent(part_name, connection)


@app.delete("/student")
async def deleteStudent(student_id : int) :
    return db.deleteStudent(student_id, connection)

@app.post("/student-phone")
async def addStudentPhone(student_id : int, phone_no : str ) :
    if(phone_no.isdigit) :
        return db.insertStudentPhone(student_id, phone_no, connection)
    else :
        return { "error" : "Validation failed for phone no."} 
    
@app.get("/student/search-by-phone")
async def getStudentByPhoneNo(phone_no : str) :
    return db.searchStudentByPhoneNo(phone_no, connection)
        

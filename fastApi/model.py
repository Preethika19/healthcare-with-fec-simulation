from datetime import date
from oracledb import Date
from pydantic import BaseModel


class Student(BaseModel) :
    student_id : int
    first_name : str
    last_name : str
    dob : date
    gender : str
    major : str
    cgpa    : float
    email   : str
    door_no : str
    street : str
    city    : str
    
    
    
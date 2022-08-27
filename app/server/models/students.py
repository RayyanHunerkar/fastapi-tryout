from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from bson.objectid import ObjectId
from .classes import ClassesSchema, UpdateClassesModel


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(...)
    gpa: float = Field(...)
    student_class: ClassesSchema = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "Jdoe@example.com",
                "course_of_study": "Computer Science",
                "year": 3,
                "gpa": 3.5,
                "student_class": {
                    "_id": "62fdcb302daa56bfb7ac4fcb",
                    "class_name": "Computer Science",
                    "class_code": "CS",
                    "class_description": "Computer Science",
                }
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]
    student_class: Optional[ClassesSchema]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "Jdoe@example.com",
                "course_of_study": "Computer Science",
                "year": 3,
                "gpa": 3.5,
                "student_class": {
                    "_id": "62fdcb302daa56bfb7ac4fcb",
                    "class_name": "Computer Science",
                    "class_code": "CS",
                    "class_description": "Computer Science",
                }
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }

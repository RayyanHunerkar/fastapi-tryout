from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..operations import(
    add_student,
    retrieve_students,
    retrieve_student,
    update_student,
    delete_student,
)
from ..models import (
    error_response_model,
    response_model,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()


@router.post("", response_description="Student added successfully", status_code=201)
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return response_model(new_student, "Student added successfully.")


@router.get("", response_description="Students retrieved successfully", status_code=200)
async def retrieve_students_data():
    students = await retrieve_students()
    if students:
        return response_model(students, "Students retrieved successfully.")
    return error_response_model("No students found.")


@router.get("/{id}", response_description="Student retrieved successfully", status_code=200)
async def retrieve_student_data(id: str):
    student = await retrieve_student(id)
    if student:
        return response_model(student, "Student retrieved successfully.")
    return error_response_model("No student found.")


@router.put("/{id}", response_description="Student updated successfully", status_code=200)
async def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = await update_student(id, req)
    if updated_student:
        return response_model(updated_student, "Student updated successfully.")
    return error_response_model("No student found.")


@router.delete("/{id}", response_description="Student deleted successfully", status_code=200)
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return response_model(deleted_student, "Student deleted successfully.")
    return error_response_model("No student found.")


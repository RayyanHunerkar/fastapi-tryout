from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..operations import(
    add_class,
    retrieve_classes,
)

from ..models.classes import (
    ClassesSchema,
)

from ..models.students import (
    response_model,
    error_response_model,
)

router = APIRouter()


@router.post("", response_description="Class added successfully", status_code=201)
async def add_class_data(class_data: ClassesSchema = Body(...)):
    class_data = jsonable_encoder(class_data)
    new_class = await add_class(class_data)
    return response_model(new_class, "Class added successfully.")


@router.get("", response_description="Classes retrieved successfully", status_code=200)
async def retrieve_classes_data():
    classes = await retrieve_classes()
    if classes:
        return response_model(classes, "Classes retrieved successfully.")
    return error_response_model("No classes found.")



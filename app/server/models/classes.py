from typing import Optional
from pydantic import BaseModel, Field


class ClassesSchema(BaseModel):

    class_name: str = Field(...)
    class_code: str = Field(...)
    class_description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "class_name": "Computer Science",
                "class_code": "CS",
                "class_description": "Computer Science",
            }
        }


class UpdateClassesModel(BaseModel):
    class_name: Optional[str]
    class_code: Optional[str]
    class_description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "class_name": "Computer Science",
                "class_code": "CS",
                "class_description": "Computer Science",
            }
        }

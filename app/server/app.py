from fastapi import FastAPI

from .routes.students import router as student_router
from .routes.classes import router as class_router


app = FastAPI()
app.include_router(student_router, tags=["Students"], prefix='/students')
app.include_router(class_router, tags=["Classes"], prefix='/classes')

from fastapi import APIRouter, Depends, Response
from app.services.classify_students import ClassifyStudents

router = APIRouter()


@router.post("/", status_code=204, response_class=Response)
async def classify_students(
        classify_students: ClassifyStudents = Depends(ClassifyStudents)):
    classify_students.classify()

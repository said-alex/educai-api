from typing import List
from uuid import UUID, uuid4
from app.domain.entities.course import Course
from app.domain.entities.student import Student

class InMemoryStudentsRepository:
    def __init__(self):
        self._students = [
            Student(
                name="John",
                course=Course(name="Matemática"),
                dropout=True,
                monthly_income=1000,
            ),
            Student(
                name="Mary",
                course=Course(name="Matemática"),
                dropout=True,
                monthly_income=4000,
            ),
            Student(
                name="Peter",
                course=Course(name="Matemática"),
            ),
        ]

    def get_students_in_dropout(self) -> List[Student]:
        return list(filter(lambda student: student.dropout, self._students))
    
    def count_students(self) -> int:
        return len(self._students)

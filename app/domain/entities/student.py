from uuid import UUID, uuid4
from app.domain.entities.course import Course

class Student:
    def __init__(
            self, 
            name: str, 
            course: Course,
            student_id: UUID = uuid4(),
            dropout: bool = False,
            monthly_income: float = 0.0,):
        self.id = student_id
        self.name = name
        self.course = course
        self.dropout = dropout
        self.monthly_income = monthly_income

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
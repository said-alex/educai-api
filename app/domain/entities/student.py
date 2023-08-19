from app.domain.entities.course import Course

class Student:
    def __init__(
            self, 
            id: str ,
            name: str, 
            course: Course,
            dropout: bool = False,
            monthly_income: float = 0.0,):
        self.id = id
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

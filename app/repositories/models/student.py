from app.domain.entities.student import Student
from app.repositories.models.course import CourseModel


class StudentModel:
    def __init__(self, data):
        self.id = data["_id"]
        self.name = data["name"]
        self.dropout = data["dropout"]
        self.monthly_income = data["monthly_income"]
        self.course = data["course"]
        self.performance = data["performance"]
        self.attendance = data["attendance"]
        self.engagement = data["engagement"]
        self.payment_status = data["payment_status"]
        self.income = data["income"]

    def to_entity(self):
        return Student(
            id=self.id,
            name=self.name,
            dropout=self.dropout,
            monthly_income=self.monthly_income,
            course=CourseModel(self.course).to_entity(),
            performance=self.performance,
            attendance=self.attendance,
            engagement=self.engagement,
            payment_status=self.payment_status,
            income=self.income
        )

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

    @staticmethod
    def from_entity(student: Student):
        return StudentModel({
            "_id": student.id,
            "name": student.name,
            "dropout": student.dropout,
            "monthly_income": student.monthly_income,
            "course": CourseModel.from_entity(student.course).to_dict(),
            "performance": student.performance,
            "attendance": student.attendance,
            "engagement": student.engagement,
            "payment_status": student.payment_status,
            "income": student.income
        })

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

    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "dropout": self.get_bool_dropout(self.dropout),
            "monthly_income": self.monthly_income,
            "course": CourseModel(self.course).to_dict(),
            "performance": self.performance,
            "attendance": self.attendance,
            "engagement": self.engagement,
            "payment_status": self.payment_status,
            "income": self.income
        }

    def get_bool_dropout(self, dropout):
        if dropout == 0:
            return True
        else:
            return False

from app.domain.entities.student import Student


class StudentModel:
    def __init__(self, data):
        self.id = data["_id"]
        self.name = data["name"]
        self.email = data["email"]
        self.dropout = data["dropout"]
        self.monthly_income = data["monthly_income"]
        self.performance = data["performance"]
        self.attendance = data["attendance"]
        self.engagement = data["engagement"]
        self.payment_status = data["payment_status"]
        self.income = data["income"]
        self.cluster = data["cluster"]

    @staticmethod
    def from_entity(student: Student):
        return StudentModel({
            "_id": student.id,
            "name": student.name,
            "email": student.email,
            "dropout": student.dropout,
            "monthly_income": student.monthly_income,
            "performance": student.performance,
            "attendance": student.attendance,
            "engagement": student.engagement,
            "payment_status": student.payment_status,
            "income": student.income,
            "cluster": student.cluster
        })

    def to_entity(self):
        return Student(
            id=self.id,
            name=self.name,
            email=self.email,
            dropout=self.dropout,
            monthly_income=self.monthly_income,
            performance=self.performance,
            attendance=self.attendance,
            engagement=self.engagement,
            payment_status=self.payment_status,
            income=self.income,
            cluster=self.cluster
        )

    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "email": self.email,
            "dropout": self.get_bool_dropout(self.dropout),
            "monthly_income": self.monthly_income,
            "performance": self.performance,
            "attendance": self.attendance,
            "engagement": self.engagement,
            "payment_status": self.payment_status,
            "income": self.income,
            "cluster": self.cluster
        }

    def get_bool_dropout(self, dropout):
        if dropout == 0:
            return True
        else:
            return False

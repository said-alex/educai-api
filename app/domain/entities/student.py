from app.domain.entities.course import Course


class Student:
    def __init__(
            self,
            id: str,
            name: str,
            email: str,
            dropout: bool = False,
            monthly_income: float = 0.0,
            performance: int = 0,
            attendance: int = 0,
            engagement: int = 0,
            payment_status: int = 0,
            income: int = 0,
            cluster: int = 0,):
        self.id = id
        self.name = name
        self.email = email
        self.dropout = dropout
        self.monthly_income = monthly_income
        self.performance = performance
        self.attendance = attendance
        self.engagement = engagement
        self.payment_status = payment_status
        self.income = income
        self.cluster = cluster

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

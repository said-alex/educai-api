from datetime import datetime
from fastapi import Depends

from app.repositories.in_memory.students_repository import InMemoryStudentsRepository

class GetIncomeRisk:
    def __init__(self, student_repo = Depends(InMemoryStudentsRepository)):
        self.student_repo = student_repo

    def get_risk(self):
        students_in_dropout = self.student_repo.get_students_in_dropout()
        
        monthly_income = sum(map(lambda student: student.monthly_income, students_in_dropout))

        current_month = datetime.now().month
        yearly_income = monthly_income * (12 - current_month)

        return {monthly_income, yearly_income}

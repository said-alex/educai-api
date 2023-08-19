from datetime import datetime
from fastapi import Depends

from app.repositories.mongodb.student_repository import MongoDBStudentRepository

class GetIncomeRisk:
    def __init__(self, student_repo: MongoDBStudentRepository = Depends(MongoDBStudentRepository)):
        self.student_repo = student_repo

    def get_risk(self):
        students_in_dropout = self.student_repo.get_students_in_dropout()

        monthly_income = sum(map(lambda student: student.monthly_income, students_in_dropout))

        current_month = datetime.now().month
        yearly_income = monthly_income * (12 - current_month)


        return monthly_income, yearly_income

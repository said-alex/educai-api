from typing import List

from fastapi import Depends
from app.domain.entities.course import Course
from app.domain.entities.student import Student

from pymongo.database import Database
from app.repositories.models.student import StudentModel

from app.repositories.mongodb.get_database import get_database


class MongoDBStudentRepository:
    def __init__(self, database: Database = Depends(get_database)):
        self.database = database

    def get_students_in_dropout(self) -> List[Student]:
        students_dict = list(self.database.students.find({"dropout": True}))
        students = list(map(lambda student: StudentModel(
            student).to_entity(), students_dict))

        return students

    def get_all_students(self) -> List[Student]:
        students_dict = list(self.database.students.find({}))
        students = list(map(lambda student: StudentModel(
            student).to_entity(), students_dict))

        return students

    def count_students(self) -> int:
        return self.database.students.count_documents({})

    def update(self, student: Student):
        student_dict = {
            "_id": student.id,
            "name": student.name,
            "dropout": student.dropout,
            "monthly_income": student.monthly_income,
            "course": {"name": student.course.name},
            "performance": student.performance,
            "attendance": student.attendance,
            "engagement": student.engagement,
            "payment_status": student.payment_status,
            "income": student.income
        }

        self.database.students.update_one(
            {"_id": student.id}, {"$set": student_dict}, upsert=True)
